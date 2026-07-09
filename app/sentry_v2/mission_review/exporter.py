from __future__ import annotations

import csv
import json
import shutil
import zipfile
from pathlib import Path
from typing import Any, Dict, Iterable, List

import cv2
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrinter

from .repository import MissionEvent, MissionRepository
from .statistics import compute_mission_statistics


def export_csv_events(path: Path, events: Iterable[MissionEvent]) -> Path:
    fields = [
        "sequence",
        "occurred_at",
        "event_type",
        "category",
        "source",
        "frame_number",
        "tracker_id",
        "object_class",
        "confidence",
        "threat_score",
        "decision",
        "planner_state",
        "motion_policy_state",
        "safety_state",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fields)
        writer.writeheader()
        for e in events:
            writer.writerow(
                {
                    "sequence": e.sequence,
                    "occurred_at": e.occurred_at,
                    "event_type": e.event_type,
                    "category": e.category,
                    "source": e.source,
                    "frame_number": e.frame_number,
                    "tracker_id": e.tracker_id,
                    "object_class": e.object_class,
                    "confidence": e.confidence,
                    "threat_score": e.threat_score,
                    "decision": e.decision,
                    "planner_state": e.planner_state,
                    "motion_policy_state": e.motion_policy_state,
                    "safety_state": e.safety_state,
                }
            )
    return path


def export_json_metadata(path: Path, payload: Dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")
    return path


def export_html_report(path: Path, mission_id: str, manifest: Dict[str, Any], stats: Dict[str, Any], events: List[MissionEvent]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(
        f"<tr><td>{e.sequence}</td><td>{e.event_type}</td><td>{e.category}</td><td>{e.object_class}</td><td>{e.decision}</td></tr>"
        for e in events[:4000]
    )
    html = f"""
<!doctype html>
<html>
<head><meta charset=\"utf-8\"><title>Mission Report {mission_id}</title></head>
<body>
<h1>Mission Report: {mission_id}</h1>
<h2>Manifest</h2>
<pre>{json.dumps(manifest, ensure_ascii=True, indent=2)}</pre>
<h2>Statistics</h2>
<pre>{json.dumps(stats, ensure_ascii=True, indent=2)}</pre>
<h2>Events</h2>
<table border=\"1\" cellspacing=\"0\" cellpadding=\"4\">
<tr><th>#</th><th>Type</th><th>Category</th><th>Class</th><th>Decision</th></tr>
{rows}
</table>
</body>
</html>
""".strip()
    path.write_text(html, encoding="utf-8")
    return path


def export_pdf_report(path: Path, html_text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    printer = QPrinter(QPrinter.HighResolution)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName(str(path))
    doc = QTextDocument()
    doc.setHtml(html_text)
    doc.print_(printer)
    return path


def zip_directory(source_dir: Path, output_zip: Path) -> Path:
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    output_zip_resolved = output_zip.resolve()
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in source_dir.rglob("*"):
            if not path.is_file():
                continue
            try:
                path_resolved = path.resolve()
            except Exception:
                path_resolved = path
            # Avoid self-including the zip being written.
            if path_resolved == output_zip_resolved:
                continue
            zf.write(path, arcname=str(path.relative_to(source_dir)))
    return output_zip


def export_annotated_images(repo: MissionRepository, mission_id: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    events = repo.load_mission_events(mission_id)
    written = 0
    for event in events:
        media_refs = list(event.media_refs or [])
        if not media_refs:
            continue
        src = repo.archive_root / str(media_refs[0])
        if not src.exists():
            continue
        frame = cv2.imread(str(src))
        if frame is None:
            continue
        bbox = event.data.get("bbox")
        if isinstance(bbox, list) and len(bbox) == 4:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (30, 220, 100), 2, cv2.LINE_AA)
            label = f"{event.object_class} id={event.tracker_id} conf={event.confidence:.2f}"
            cv2.putText(frame, label, (x, max(18, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (20, 20, 20), 2, cv2.LINE_AA)
            cv2.putText(frame, label, (x, max(18, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (230, 230, 230), 1, cv2.LINE_AA)
        dst = output_dir / f"{event.sequence:06d}_{src.name}"
        cv2.imwrite(str(dst), frame)
        written += 1
    return output_dir


def export_complete_package(repo: MissionRepository, mission_id: str, output_dir: Path) -> Dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = repo.load_manifest(mission_id)
    annotations = repo.load_annotations(mission_id)
    events = repo.load_mission_events(mission_id)
    stats = compute_mission_statistics(events)

    csv_path = export_csv_events(output_dir / f"{mission_id}_events.csv", events)
    metadata_path = export_json_metadata(
        output_dir / f"{mission_id}_metadata.json",
        {"manifest": manifest, "annotations": annotations, "stats": stats},
    )
    html_path = export_html_report(output_dir / f"{mission_id}_report.html", mission_id, manifest, stats, events)
    pdf_path = export_pdf_report(output_dir / f"{mission_id}_report.pdf", html_path.read_text(encoding="utf-8"))

    mission_dir = repo.archive_root / mission_id
    archive_zip_path = output_dir / f"{mission_id}_archive.zip"
    archive_zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive_zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in mission_dir.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(mission_dir)
            # Exclude generated exports from archive payload to prevent recursion.
            if rel.parts and rel.parts[0] == "exports":
                continue
            try:
                if path.resolve() == archive_zip_path.resolve():
                    continue
            except Exception:
                pass
            zf.write(path, arcname=str(rel))
    archive_zip = archive_zip_path

    img_zip = output_dir / f"{mission_id}_images.zip"
    snapshots_dir = mission_dir / "snapshots"
    if snapshots_dir.exists():
        zip_directory(snapshots_dir, img_zip)

    annotated_dir = output_dir / f"{mission_id}_annotated_images"
    export_annotated_images(repo, mission_id, annotated_dir)
    annotated_zip = output_dir / f"{mission_id}_annotated_images.zip"
    if annotated_dir.exists():
        zip_directory(annotated_dir, annotated_zip)

    package_zip = output_dir / f"{mission_id}_complete_package.zip"
    with zipfile.ZipFile(package_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in [csv_path, metadata_path, html_path, pdf_path, archive_zip]:
            if file_path.exists():
                zf.write(file_path, arcname=file_path.name)
        if img_zip.exists():
            zf.write(img_zip, arcname=img_zip.name)
        if annotated_zip.exists():
            zf.write(annotated_zip, arcname=annotated_zip.name)

    return {
        "csv": str(csv_path),
        "json": str(metadata_path),
        "html": str(html_path),
        "pdf": str(pdf_path),
        "archive_zip": str(archive_zip),
        "images_zip": str(img_zip) if img_zip.exists() else "",
        "annotated_images_zip": str(annotated_zip) if annotated_zip.exists() else "",
        "complete_package": str(package_zip),
    }
