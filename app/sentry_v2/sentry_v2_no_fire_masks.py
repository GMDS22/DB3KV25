from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

from .sentry_v2_config import NoFireMaskConfig, NoFireMaskVertex


def angular_vertex_from_normalized_point(
    norm_x: float,
    norm_y: float,
    anchor_pan: float,
    anchor_tilt: float,
    hfov: float,
    vfov: float,
) -> NoFireMaskVertex:
    pan = float(anchor_pan + ((float(norm_x) - 0.5) * float(hfov)))
    tilt = float(anchor_tilt - ((float(norm_y) - 0.5) * float(vfov)))
    return NoFireMaskVertex(pan=pan, tilt=tilt)


def normalized_point_from_angular_vertex(
    vertex: NoFireMaskVertex,
    current_pan: float,
    current_tilt: float,
    hfov: float,
    vfov: float,
) -> Tuple[float, float]:
    hfov = float(hfov) if abs(float(hfov)) > 1e-6 else 1.0
    vfov = float(vfov) if abs(float(vfov)) > 1e-6 else 1.0
    norm_x = 0.5 + ((float(vertex.pan) - float(current_pan)) / hfov)
    norm_y = 0.5 - ((float(vertex.tilt) - float(current_tilt)) / vfov)
    return norm_x, norm_y


def project_mask_to_frame(
    mask: NoFireMaskConfig,
    current_pan: float,
    current_tilt: float,
    hfov: float,
    vfov: float,
    frame_width: int,
    frame_height: int,
) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = []
    width = max(1, int(frame_width))
    height = max(1, int(frame_height))
    for vertex in mask.vertices:
        norm_x, norm_y = normalized_point_from_angular_vertex(
            vertex,
            current_pan,
            current_tilt,
            hfov,
            vfov,
        )
        px = int(round(norm_x * width))
        py = int(round(norm_y * height))
        points.append((px, py))
    return points


def _polygon_area(polygon: Sequence[Tuple[float, float]]) -> float:
    """Return the absolute area of a polygon via the shoelace formula.

    Returns 0.0 for degenerate inputs (fewer than 3 vertices, all collinear,
    or duplicate points).  Callers should treat area < 1e-6 as degenerate.
    """
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) * 0.5


def polygon_contains_point(
    polygon: Sequence[Tuple[float, float]],
    point: Tuple[float, float],
) -> bool:
    if len(polygon) < 3:
        return False

    px, py = point
    inside = False
    j = len(polygon) - 1
    for i in range(len(polygon)):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        intersects = ((yi > py) != (yj > py)) and (
            px < ((xj - xi) * (py - yi) / ((yj - yi) or 1e-12)) + xi
        )
        if intersects:
            inside = not inside
        j = i
    return inside


def mask_contains_aim(mask: NoFireMaskConfig, pan: float, tilt: float) -> bool:
    polygon = [(float(vertex.pan), float(vertex.tilt)) for vertex in mask.vertices]
    return polygon_contains_point(polygon, (float(pan), float(tilt)))


def find_blocking_mask(
    masks: Iterable[NoFireMaskConfig],
    pan: float,
    tilt: float,
) -> Optional[NoFireMaskConfig]:
    for mask in masks:
        if not bool(mask.enabled):
            continue
        if len(mask.vertices) < 3:
            continue
        polygon = [(float(vertex.pan), float(vertex.tilt)) for vertex in mask.vertices]
        # Skip degenerate masks (collinear/duplicate vertices) — fail closed means
        # a broken mask definition must NOT silently allow fire through.
        if _polygon_area(polygon) < 1e-6:
            continue
        if polygon_contains_point(polygon, (float(pan), float(tilt))):
            return mask
    return None
