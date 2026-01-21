from __future__ import annotations

import argparse
from pathlib import Path


def _enhance(im, *, scale: float = 2.0):
    from PIL import Image, ImageEnhance, ImageFilter

    if scale != 1.0:
        resample = getattr(getattr(Image, "Resampling", Image), "LANCZOS", Image.LANCZOS)
        im = im.resize(
            (int(im.size[0] * scale), int(im.size[1] * scale)),
            resample=resample,
        )

    im = ImageEnhance.Contrast(im).enhance(1.35)
    im = ImageEnhance.Sharpness(im).enhance(2.0)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=175, threshold=3))
    return im


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate enhanced PNG crops from a source image to help read servo model text."
    )
    parser.add_argument(
        "--src",
        type=Path,
        default=Path(
            r"D:\GM_REVIT_TOOLBOX\DB3000V4.1-main\1efe7e1c372359451be7058f9abeda0e.jpg_2200x2200q80.jpg_.webp"
        ),
        help="Source image path (webp/jpg/png).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(
            r"D:\GM_REVIT_TOOLBOX\DB3000V4.1-main\artifacts\servo_label_crops"
        ),
        help="Output directory for crops.",
    )
    args = parser.parse_args()

    try:
        from PIL import Image
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "Pillow is required (pip install pillow). Error: %s" % (exc,)
        )

    try:
        import numpy as np
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "NumPy is required (pip install numpy). Error: %s" % (exc,)
        )

    src: Path = args.src
    out_dir: Path = args.out

    if not src.exists():
        raise SystemExit(f"Source image not found: {src}")

    out_dir.mkdir(parents=True, exist_ok=True)

    img = Image.open(src).convert("RGB")
    w, h = img.size

    # Score horizontal bands by simple edge energy to guess where printed text is.
    arr = np.asarray(img.convert("L"), dtype=np.float32)
    sx = np.abs(arr[:, 1:] - arr[:, :-1])
    sy = np.abs(arr[1:, :] - arr[:-1, :])
    edge = np.zeros_like(arr)
    edge[:, :-1] += sx
    edge[:-1, :] += sy

    win_h = max(200, h // 6)
    step = max(50, win_h // 4)

    scores: list[tuple[float, int, int]] = []
    for y0 in range(0, h - win_h + 1, step):
        y1 = y0 + win_h
        score = float(edge[y0:y1, :].mean())
        scores.append((score, y0, y1))

    scores.sort(reverse=True)

    picked: list[tuple[float, int, int]] = []
    for score, y0, y1 in scores:
        if all(abs(y0 - py0) > win_h // 2 for _, py0, _ in picked):
            picked.append((score, y0, y1))
        if len(picked) >= 4:
            break

    # Add deterministic regions (top/mid/bottom) in case heuristic misses.
    picked.extend(
        [
            (0.0, 0, min(h, h // 3)),
            (0.0, h // 3, min(h, 2 * h // 3)),
            (0.0, 2 * h // 3, h),
        ]
    )

    center_x0 = int(w * 0.15)
    center_x1 = int(w * 0.85)

    seen: set[tuple[int, int, int, int, str]] = set()
    idx = 1

    for _, y0, y1 in picked:
        for variant, (x0, x1) in [
            ("full", (0, w)),
            ("center", (center_x0, center_x1)),
        ]:
            key = (x0, x1, y0, y1, variant)
            if key in seen:
                continue
            seen.add(key)

            crop = img.crop((x0, y0, x1, y1))
            crop_enh = _enhance(crop, scale=2.0)
            name = f"crop_{idx:02d}_{variant}_y{y0}-{y1}.png"
            crop_enh.save(out_dir / name)
            idx += 1

    _enhance(img, scale=1.5).save(out_dir / "full_enhanced_1p5x.png")

    print(f"Wrote {idx - 1} crops to: {out_dir}")
    print(f"Wrote enhanced full image: {out_dir / 'full_enhanced_1p5x.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
