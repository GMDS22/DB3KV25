"""
Hybrid Detection Fusion Helpers
===============================

Functions to combine color detection with other detection modes.
Supports AND (intersection) and OR (union) fusion strategies.
"""

from typing import List, Tuple


def fuse_detections_and(boxes1: List[Tuple], boxes2: List[Tuple],
                        overlap_threshold: float = 0.3) -> List[Tuple]:
    """
    Fuse two detection lists using AND logic (intersection).
    Only returns boxes that overlap between both lists.
    
    Args:
        boxes1: First list of (x, y, w, h) boxes
        boxes2: Second list of (x, y, w, h) boxes
        overlap_threshold: Minimum IoU for boxes to be considered matching
        
    Returns:
        Fused list of boxes
    """
    if not boxes1 or not boxes2:
        return []
    
    fused = []
    used_b2 = set()
    
    for b1 in boxes1:
        x1, y1, w1, h1 = b1
        best_iou = 0
        best_box = None
        best_idx = -1
        
        for idx, b2 in enumerate(boxes2):
            if idx in used_b2:
                continue
                
            x2, y2, w2, h2 = b2
            
            # Calculate intersection
            xi = max(x1, x2)
            yi = max(y1, y2)
            wi = min(x1 + w1, x2 + w2) - xi
            hi = min(y1 + h1, y2 + h2) - yi
            
            if wi > 0 and hi > 0:
                inter_area = wi * hi
                union_area = w1 * h1 + w2 * h2 - inter_area
                iou = inter_area / union_area if union_area > 0 else 0
                
                if iou > best_iou and iou >= overlap_threshold:
                    best_iou = iou
                    # Return the larger box
                    best_box = b1 if w1 * h1 >= w2 * h2 else b2
                    best_idx = idx
        
        if best_box is not None:
            fused.append(best_box)
            used_b2.add(best_idx)
    
    return fused


def fuse_detections_or(boxes1: List[Tuple], boxes2: List[Tuple],
                       merge_overlapping: bool = True,
                       merge_threshold: float = 0.5) -> List[Tuple]:
    """
    Fuse two detection lists using OR logic (union).
    Returns all boxes from both lists, optionally merging overlapping ones.
    
    Args:
        boxes1: First list of (x, y, w, h) boxes
        boxes2: Second list of (x, y, w, h) boxes
        merge_overlapping: If True, merge significantly overlapping boxes
        merge_threshold: IoU threshold for merging
        
    Returns:
        Fused list of boxes
    """
    all_boxes = list(boxes1) + list(boxes2)
    
    if not merge_overlapping or len(all_boxes) <= 1:
        return all_boxes
    
    # Simple non-max suppression
    merged = []
    used = [False] * len(all_boxes)
    
    for i, b1 in enumerate(all_boxes):
        if used[i]:
            continue
        
        x1, y1, w1, h1 = b1
        merged_box = [x1, y1, w1, h1]
        
        for j in range(i + 1, len(all_boxes)):
            if used[j]:
                continue
            
            x2, y2, w2, h2 = all_boxes[j]
            
            # Calculate IoU
            xi = max(merged_box[0], x2)
            yi = max(merged_box[1], y2)
            wi = min(merged_box[0] + merged_box[2], x2 + w2) - xi
            hi = min(merged_box[1] + merged_box[3], y2 + h2) - yi
            
            if wi > 0 and hi > 0:
                inter_area = wi * hi
                area1 = merged_box[2] * merged_box[3]
                area2 = w2 * h2
                union_area = area1 + area2 - inter_area
                iou = inter_area / union_area if union_area > 0 else 0
                
                if iou >= merge_threshold:
                    # Merge: take bounding box of both
                    new_x = min(merged_box[0], x2)
                    new_y = min(merged_box[1], y2)
                    new_w = max(merged_box[0] + merged_box[2], x2 + w2) - new_x
                    new_h = max(merged_box[1] + merged_box[3], y2 + h2) - new_y
                    merged_box = [new_x, new_y, new_w, new_h]
                    used[j] = True
        
        merged.append(tuple(merged_box))
        used[i] = True
    
    return merged


def calculate_iou(box1: Tuple, box2: Tuple) -> float:
    """
    Calculate Intersection over Union (IoU) between two boxes.
    
    Args:
        box1: First box as (x, y, w, h)
        box2: Second box as (x, y, w, h)
        
    Returns:
        IoU value between 0 and 1
    """
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    
    # Calculate intersection
    xi = max(x1, x2)
    yi = max(y1, y2)
    wi = min(x1 + w1, x2 + w2) - xi
    hi = min(y1 + h1, y2 + h2) - yi
    
    if wi <= 0 or hi <= 0:
        return 0.0
    
    inter_area = wi * hi
    union_area = w1 * h1 + w2 * h2 - inter_area
    
    return inter_area / union_area if union_area > 0 else 0.0


def filter_by_size(boxes: List[Tuple], min_area: float = 0,
                   max_area: float = float('inf')) -> List[Tuple]:
    """
    Filter boxes by area.
    
    Args:
        boxes: List of (x, y, w, h) boxes
        min_area: Minimum area in pixels
        max_area: Maximum area in pixels
        
    Returns:
        Filtered list of boxes
    """
    return [
        box for box in boxes
        if min_area <= box[2] * box[3] <= max_area
    ]


def get_largest_box(boxes: List[Tuple]) -> Tuple:
    """
    Get the largest box by area.
    
    Args:
        boxes: List of (x, y, w, h) boxes
        
    Returns:
        The largest box, or None if list is empty
    """
    if not boxes:
        return None
    return max(boxes, key=lambda b: b[2] * b[3])


def get_centroid(box: Tuple) -> Tuple[int, int]:
    """
    Get the centroid of a box.
    
    Args:
        box: Box as (x, y, w, h)
        
    Returns:
        Centroid as (cx, cy)
    """
    x, y, w, h = box
    return (x + w // 2, y + h // 2)
