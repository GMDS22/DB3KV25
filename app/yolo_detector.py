import os
import time

# CHANGE WARNING:
# Keep this module's YOLO inference behavior in sync with
# app/MAIN_FILE_SINGLE_CAM.py (async/threading, ROI usage, class filters,
# confidence handling). If you change one, update the other or document why.

# Do not import ultralytics at module import time. Import lazily inside
# load_model so we can attempt a CPU-only import on systems where GPU
# drivers/PyTorch CUDA support may be missing (common on some AMD/Windows setups).
YOLO = None
_HAS_ULTRALYTICS = False


class YoloDetector:
    """
    A class to handle YOLO model loading and object detection.

    This detector optionally accepts an `enhancer` object (the
    TurretEnhancements instance) so it can play detect sounds when
    a new detection appears. Sound playback is debounced to avoid
    spamming audio when YOLO runs at high frame rates.
    """

    def __init__(self, models_dir="YOLO_MODELS", enhancer=None):
        self.models_dir = models_dir
        self.model = None
        self.model_name = None
        # Indicates whether a model was successfully loaded
        self.model_loaded = False
        self.target_classes = []
        # Optional enhancer (TurretEnhancements) for playing sounds
        self.enhancer = enhancer
        # Debounce for detect sound (seconds)
        self._last_detect_sound_time = 0.0
        self._detect_sound_debounce = 0.6

    def find_models(self):
        """Finds all .pt files in the models directory."""
        if not os.path.exists(self.models_dir):
            os.makedirs(self.models_dir)
            return []
        return [f for f in os.listdir(self.models_dir) if f.endswith(".pt")]

    def load_model(self, model_name):
        """
        Loads a YOLO model.

        Args:
            model_name (str): The filename of the model to load (e.g., 'yolov8n.pt').

        Returns:
            bool: True if the model was loaded successfully, False otherwise.
        """
        # Allow callers to pass either a plain model filename (located in
        # self.models_dir) or a full/relative path to a .pt file. If the
        # requested model matches the currently-loaded path, treat as a no-op.
        try:
            # Lazy-import ultralytics here so we can control environment
            # variables (for example forcing CPU) before the import occurs.
            global YOLO, _HAS_ULTRALYTICS
            # Respect an explicit environment opt-in to use the GPU. By
            # default we force CPU-only to maximize compatibility on systems
            # (like many AMD/Windows machines) where CUDA is not available.
            use_gpu = str(os.environ.get("TURRET_USE_GPU", "0")).lower() in (
                "1",
                "true",
                "yes",
            )
            saved_cuda_vis = os.environ.get("CUDA_VISIBLE_DEVICES", None)
            if not use_gpu:
                # Force CPU-only import path for PyTorch by hiding CUDA devices.
                os.environ["CUDA_VISIBLE_DEVICES"] = ""
            try:
                from ultralytics import YOLO as _YOLO  # type: ignore

                YOLO = _YOLO
                _HAS_ULTRALYTICS = True
            except Exception as e:
                # Restore environment before returning
                if saved_cuda_vis is None:
                    os.environ.pop("CUDA_VISIBLE_DEVICES", None)
                else:
                    os.environ["CUDA_VISIBLE_DEVICES"] = saved_cuda_vis
                print(f"[YOLO] ultralytics import failed: {e}")
                self.model = None
                self.model_name = None
                self.model_loaded = False
                self.model_path = None
                return False
            # restore original CUDA_VISIBLE_DEVICES now that import completed
            if saved_cuda_vis is None:
                os.environ.pop("CUDA_VISIBLE_DEVICES", None)
            else:
                os.environ["CUDA_VISIBLE_DEVICES"] = saved_cuda_vis
            # Determine candidate model path
            candidate = model_name or ""
            # If model_name looks like a path or the file exists as given, use it
            if (
                os.path.isabs(candidate)
                or os.path.exists(candidate)
                or os.path.sep in candidate
            ):
                model_path = candidate
            else:
                model_path = os.path.join(self.models_dir, candidate)

            # Normalize path for comparison
            model_path = os.path.normpath(model_path)

            # If the same model path is already loaded, nothing to do
            if (
                getattr(self, "model_path", None) == model_path
                and self.model is not None
            ):
                return True

            if not os.path.exists(model_path):
                print(f"[YOLO] Error: Model file not found at {model_path}")
                self.model = None
                self.model_name = None
                self.model_loaded = False
                self.model_path = None
                return False

            try:
                print(f"[YOLO] Loading model: {model_path}...")
                # Type-narrowing: ensure static checkers know YOLO is available here
                assert YOLO is not None
                # Create the model instance. ultralytics will pick device based
                # on available torch/CUDA state; because we attempted a CPU-only
                # import above by default, this will prefer CPU which is safest
                # for AMD/Windows users. If the user explicitly set
                # TURRET_USE_GPU=1, they accept GPU risk.
                self.model = YOLO(model_path)  # type: ignore[call-arg]
                # record both path and a friendly name
                self.model_path = model_path
                self.model_name = os.path.basename(model_path)
                # Set model_loaded flag so callers can detect successful load
                self.model_loaded = True
                print("[YOLO] Model loaded successfully.")
                return True
            except Exception as e:
                print(f"[YOLO] Error loading model: {e}")
                self.model = None
                self.model_name = None
                self.model_loaded = False
                self.model_path = None
                return False
        except Exception as e:
            print(f"[YOLO] Unexpected error in load_model: {e}")
            self.model = None
            self.model_name = None
            self.model_loaded = False
            self.model_path = None
            return False

    def set_target_classes(self, classes_str):
        """Sets the target classes to detect.

        Accepts either a comma-separated string (e.g. 'person,cat') or a
        list/iterable of class names. Normalizes to a list of lowercase names.
        """
        try:
            if classes_str is None:
                self.target_classes = []
                return
            # If caller passed a list/iterable of strings, handle that
            if isinstance(classes_str, (list, tuple, set)):
                self.target_classes = [
                    str(c).strip().lower() for c in classes_str if str(c).strip()
                ]
                return
            # Otherwise assume a comma-separated string
            s = str(classes_str)
            if not s.strip():
                self.target_classes = []
            else:
                self.target_classes = [
                    c.strip().lower() for c in s.split(",") if c.strip()
                ]
        except Exception:
            # On any error, fall back to empty list
            self.target_classes = []

    def detect(self, frame, confidence=0.5, ignore_target_classes=False, return_class_names=False):
        """
        Runs object detection on a single frame.

        Args:
            frame: The image frame to process.
            confidence (float): The confidence threshold for detections.
            ignore_target_classes (bool): If True, detects all objects regardless
                                          of the self.target_classes list.
            return_class_names (bool): If True, returns a tuple (detections, class_names).
                                       If False (default), returns only the detections list
                                       for backward compatibility.
        """
        if self.model is None:
            return ([], []) if return_class_names else []

        results = self.model(frame, stream=True, verbose=False)
        detections = []
        class_names_detected = []
        for r in results:
            for box in r.boxes:
                # Get class name
                cls_id = int(box.cls[0])
                class_name = self.model.names[cls_id].lower()

                # Filter by confidence and optionally by target class
                if box.conf[0] > confidence:
                    if ignore_target_classes or (not self.target_classes or class_name in self.target_classes):
                        x1, y1, x2, y2 = box.xyxy[0]
                        detections.append((int(x1), int(y1), int(x2 - x1), int(y2 - y1)))
                        class_names_detected.append(class_name)
        try:
            if detections:
                now = time.time()
                enh = getattr(self, "enhancer", None)
                # Narrow the enhancer variable so static analyzers recognize it's not None
                if enh is not None and hasattr(enh, "play_detect"):
                    try:
                        if now - getattr(
                            self, "_last_detect_sound_time", 0.0
                        ) >= getattr(self, "_detect_sound_debounce", 0.6):
                            try:
                                enh.play_detect()
                            except Exception as e:
                                print(f"[YOLO] Audio play failed: {e}")
                            self._last_detect_sound_time = now
                    except Exception as e:
                        print(f"[YOLO] Debounce check failed: {e}")
            else:
                # reset the rising-edge logic when no detections are present
                try:
                    self._last_detect_sound_time = getattr(
                        self, "_last_detect_sound_time", 0.0
                    )
                except Exception as e:
                    print(f"[YOLO] Reset detect time failed: {e}")
        except Exception as e:
            print(f"[YOLO] Detection audio handling failed: {e}")

        if return_class_names:
            return detections, class_names_detected
        return detections
