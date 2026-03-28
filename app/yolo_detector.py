import os
import time
import sys
import site
from pathlib import Path

# CHANGE WARNING:
# Keep this module's YOLO inference behavior in sync with
# app/MAIN_FILE_SINGLE_CAM.py (async/threading, ROI usage, class filters,
# confidence handling). If you change one, update the other or document why.

# Do not import ultralytics at module import time. Import lazily inside
# load_model so we can attempt a CPU-only import on systems where GPU
# drivers/PyTorch CUDA support may be missing (common on some AMD/Windows setups).
YOLO = None
_HAS_ULTRALYTICS = False
SUPPORTED_MODEL_SUFFIXES = (".pt", ".onnx", ".engine", ".torchscript")


def _prepare_windows_torch_runtime_env() -> None:
    """Set conservative CPU/OpenMP environment defaults for torch stability."""
    try:
        if os.name != "nt":
            return
        os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")
        os.environ.setdefault("OMP_NUM_THREADS", "1")
        os.environ.setdefault("MKL_NUM_THREADS", "1")
        os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")
        os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")
    except Exception:
        pass


def _prepare_windows_torch_dll_path() -> None:
    """Best-effort DLL search path setup for torch on Windows.

    Some environments fail with WinError 1114 while importing torch/ultralytics
    unless torch's native DLL folder is explicitly added.
    """
    try:
        if os.name != "nt":
            return

        candidate_dirs = []

        # Interpreter-local venv path first
        try:
            exe = Path(sys.executable)
            candidate_dirs.append(exe.parent.parent / "Lib" / "site-packages" / "torch" / "lib")
        except Exception:
            pass

        # Site package locations
        try:
            for sp in list(site.getsitepackages()) + [site.getusersitepackages()]:
                candidate_dirs.append(Path(sp) / "torch" / "lib")
        except Exception:
            pass

        seen = set()
        for dll_dir in candidate_dirs:
            try:
                p = str(Path(dll_dir).resolve())
            except Exception:
                p = str(dll_dir)
            if not p or p in seen:
                continue
            seen.add(p)
            if not os.path.isdir(p):
                continue

            try:
                if hasattr(os, "add_dll_directory"):
                    os.add_dll_directory(p)
            except Exception:
                pass

            try:
                cur_path = os.environ.get("PATH", "")
                parts = cur_path.split(os.pathsep) if cur_path else []
                if p not in parts:
                    os.environ["PATH"] = p + os.pathsep + cur_path if cur_path else p
            except Exception:
                pass
    except Exception:
        pass


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

    def _repo_root_path(self) -> Path:
        try:
            return Path(__file__).resolve().parent.parent
        except Exception:
            return Path.cwd()

    def _candidate_model_dirs(self) -> list[Path]:
        candidates: list[Path] = []
        raw_models_dir = str(getattr(self, "models_dir", "YOLO_MODELS") or "YOLO_MODELS").strip()

        def _add(path_value: Path | str) -> None:
            try:
                path_obj = Path(path_value).expanduser()
                if not path_obj.is_absolute():
                    path_obj = (self._repo_root_path() / path_obj).resolve()
                else:
                    path_obj = path_obj.resolve()
                if path_obj not in candidates:
                    candidates.append(path_obj)
            except Exception:
                pass

        if raw_models_dir:
            _add(raw_models_dir)
            try:
                if not Path(raw_models_dir).is_absolute():
                    _add(Path.cwd() / raw_models_dir)
            except Exception:
                pass

        _add(self._repo_root_path() / "YOLO_MODELS")
        _add(Path.cwd() / "YOLO_MODELS")
        return candidates

    def _discover_models(self) -> list[tuple[str, str]]:
        discovered: dict[str, str] = {}
        for models_dir in self._candidate_model_dirs():
            try:
                if not models_dir.is_dir():
                    continue
            except Exception:
                continue

            try:
                entries = sorted(models_dir.iterdir(), key=lambda item: item.name.lower())
            except Exception:
                continue

            for entry in entries:
                try:
                    if not entry.is_file():
                        continue
                    if entry.suffix.lower() not in SUPPORTED_MODEL_SUFFIXES:
                        continue
                    discovered.setdefault(entry.name, str(entry.resolve()))
                except Exception:
                    continue

        return sorted(discovered.items(), key=lambda item: item[0].lower())

    def resolve_model_path(self, model_name: str) -> str:
        candidate = str(model_name or "").strip()
        if not candidate:
            return ""

        try:
            if os.path.isabs(candidate) or os.path.exists(candidate) or os.path.sep in candidate:
                return os.path.abspath(candidate)
        except Exception:
            pass

        try:
            for name, path in self._discover_models():
                if name == candidate or os.path.basename(candidate) == name:
                    return path
        except Exception:
            pass

        try:
            configured_dir = str(getattr(self, "models_dir", "YOLO_MODELS") or "YOLO_MODELS")
            return os.path.abspath(os.path.join(configured_dir, candidate))
        except Exception:
            return candidate

    def find_models(self):
        """Find supported YOLO model files from configured and repo-local model folders."""
        try:
            return [name for name, _ in self._discover_models()]
        except Exception:
            return []

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
            try:
                _prepare_windows_torch_runtime_env()
            except Exception:
                pass
            try:
                _prepare_windows_torch_dll_path()
            except Exception:
                pass
            # Lazy-import ultralytics here so we can control environment
            # variables (for example forcing CPU) before the import occurs.
            global YOLO, _HAS_ULTRALYTICS
            # Respect explicit opt-in for GPU behavior.
            use_gpu = str(os.environ.get("TURRET_USE_GPU", "0")).lower() in (
                "1",
                "true",
                "yes",
            )
            saved_cuda_vis = os.environ.get("CUDA_VISIBLE_DEVICES", None)

            # Try normal import first (most stable on Windows/CPU-only setups).
            import_exc = None
            try:
                from ultralytics import YOLO as _YOLO  # type: ignore

                YOLO = _YOLO
                _HAS_ULTRALYTICS = True
            except Exception as e:
                import_exc = e

            # Fallback: CPU-forced import path only when normal import failed.
            if YOLO is None and (not use_gpu):
                try:
                    os.environ["CUDA_VISIBLE_DEVICES"] = ""
                    from ultralytics import YOLO as _YOLO  # type: ignore

                    YOLO = _YOLO
                    _HAS_ULTRALYTICS = True
                    import_exc = None
                except Exception as e:
                    import_exc = e
                finally:
                    if saved_cuda_vis is None:
                        os.environ.pop("CUDA_VISIBLE_DEVICES", None)
                    else:
                        os.environ["CUDA_VISIBLE_DEVICES"] = saved_cuda_vis

            if YOLO is None:
                print(f"[YOLO] ultralytics import failed: {import_exc}")
                self.model = None
                self.model_name = None
                self.model_loaded = False
                self.model_path = None
                return False
            # Determine candidate model path
            candidate = model_name or ""
            model_path = os.path.normpath(self.resolve_model_path(candidate))

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
            if isinstance(classes_str, (list, tuple, set)):
                self.target_classes = [
                    str(c).strip().lower() for c in classes_str if str(c).strip()
                ]
                return
            s = str(classes_str)
            if not s.strip():
                self.target_classes = []
            else:
                self.target_classes = [
                    c.strip().lower() for c in s.split(",") if c.strip()
                ]
        except Exception:
            self.target_classes = []

    def detect(self, frame, confidence=0.5, ignore_target_classes=False, return_class_names=False):
        """Run object detection on a single frame."""
        if self.model is None:
            return ([], []) if return_class_names else []

        results = self.model(frame, stream=True, verbose=False)

        # Build a normalized set of class names available in the current model.
        # If user-configured target classes do not exist in this model, fall back
        # to all classes so detection never appears "dead" after model/settings changes.
        use_class_filter = (not bool(ignore_target_classes)) and bool(self.target_classes)
        target_class_set = set()
        try:
            model_names = getattr(self.model, "names", {})
            if isinstance(model_names, dict):
                available_class_set = {
                    str(v).strip().lower() for v in model_names.values() if str(v).strip()
                }
            else:
                available_class_set = {
                    str(v).strip().lower() for v in model_names if str(v).strip()
                }
            target_class_set = {
                str(v).strip().lower() for v in self.target_classes if str(v).strip()
            }
            if use_class_filter:
                valid_target_set = target_class_set & available_class_set
                if valid_target_set:
                    target_class_set = valid_target_set
                else:
                    use_class_filter = False
                    try:
                        warn_key = (
                            tuple(sorted(target_class_set)),
                            tuple(sorted(available_class_set)),
                        )
                        if getattr(self, "_last_invalid_class_warn_key", None) != warn_key:
                            self._last_invalid_class_warn_key = warn_key
                            print(
                                "[YOLO] Target classes not found in current model; "
                                "falling back to all classes"
                            )
                    except Exception:
                        pass
        except Exception:
            use_class_filter = False

        detections = []
        class_names_detected = []
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                class_name = self.model.names[cls_id].lower()
                if box.conf[0] > confidence:
                    if (not use_class_filter) or (class_name in target_class_set):
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
