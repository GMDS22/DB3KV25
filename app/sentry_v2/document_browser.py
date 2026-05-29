from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path
from typing import Callable, List, Optional

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices, QTextDocument
from PyQt5.QtWidgets import (
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QLineEdit,
    QPushButton,
    QSplitter,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


DOCUMENT_BROWSER_SUFFIXES = {".md", ".txt"}
DOCUMENT_BROWSER_SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "arduino",
    "build",
    "dist",
    "logs",
    "models",
    "platformio",
    "snapshots",
    "sounds",
    "YOLO_MODELS",
}


_DOCUMENT_BROWSER_FALLBACK_THEME = {
    "root_bg": "#15120f",
    "panel_bg": "#17120f",
    "surface_bg": "#1f1914",
    "surface_alt_bg": "#241c17",
    "field_bg": "#1f1914",
    "field_text": "#f2eadf",
    "border": "#544032",
    "text": "#f0e7dc",
    "muted": "#d7c5b4",
    "subtle": "#bca694",
    "title": "#fff4e5",
    "accent": "#cfae88",
    "accent_strong": "#f3ad63",
    "accent_soft": "#6f523e",
    "accent_mid": "#7b5632",
    "hero_bg": "#2b2018",
    "hero_text": "#fff5e8",
    "hero_subtle": "#dcc6af",
    "button_bg": "#2e241d",
    "button_hover": "#413126",
    "button_text": "#f2eadf",
    "selected_bg": "#3a2b1f",
    "selected_text": "#fff0d9",
    "link": "#8ed8ff",
    "code_text": "#8be0d2",
}


@dataclass(frozen=True)
class DocumentBrowserEntry:
    title: str
    relative_path: str
    absolute_path: Path
    category: str
    preview: str
    search_text: str
    file_search_text: str
    content_search_text: str
    body_text: str
    priority: int


def _normalize_search_text(text: str) -> str:
    lowered = str(text or "").lower()
    lowered = re.sub(r"[^a-z0-9_./ -]+", " ", lowered)
    return re.sub(r"\s+", " ", lowered).strip()


def _humanize_title(path: Path) -> str:
    name = path.stem.replace("_", " ").replace("-", " ").strip()
    return re.sub(r"\s+", " ", name).title() or path.name


def _infer_category(path: Path) -> tuple[str, int]:
    name = path.name.lower()
    relative = path.as_posix().lower()
    if ("documentation" in name and any(token in name for token in ("hub", "index", "standard"))) or name == "readme.md":
        return "Overview", -1
    if "manual" in name:
        return "Manual", 0
    if "quick" in name or "reference" in name:
        return "Reference", 1
    if "guide" in name:
        return "Guide", 1
    if "checklist" in name:
        return "Checklist", 2
    if any(token in name for token in ("report", "summary", "update", "log")):
        return "Report", 3
    if any(token in name for token in ("blueprint", "proposal", "protocol", "architecture", "implementation")):
        return "Design", 4
    if relative.startswith("docs/"):
        return "Docs", 5
    return "Document", 6


def _preview_excerpt(text: str, *, max_chars: int = 420) -> str:
    sections = [chunk.strip() for chunk in re.split(r"\n\s*\n", text) if chunk.strip()]
    for section in sections:
        if not section.startswith("#"):
            return section[:max_chars].strip()
    return text[:max_chars].strip()


def _build_search_results(
    entries: List[DocumentBrowserEntry],
    *,
    query: str,
    selected_category: str,
) -> tuple[List[DocumentBrowserEntry], List[str]]:
    normalized_query = _normalize_search_text(query)
    tokens = [token for token in normalized_query.split(" ") if token]

    results: List[DocumentBrowserEntry] = []
    for entry in entries:
        if selected_category != "All" and entry.category != selected_category:
            continue
        if not tokens:
            results.append(entry)
            continue

        file_match = all(token in entry.file_search_text for token in tokens)
        content_match = all(token in entry.content_search_text for token in tokens)
        if not file_match and not content_match:
            continue

        results.append(entry)

    return results, tokens


def _format_doc_timestamp(path: Path) -> str:
    try:
        return datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return "Unknown"


def _extract_leading_metadata(text: str) -> tuple[str, list[tuple[str, str]]]:
    lines = text.splitlines()
    if not lines:
        return text, []

    start_index = 0
    if lines[0].lstrip().startswith("#"):
        start_index = 1

    probe_index = start_index
    while probe_index < len(lines) and not lines[probe_index].strip():
        probe_index += 1

    metadata: list[tuple[str, str]] = []
    end_index = probe_index
    while end_index < len(lines):
        line = lines[end_index].strip()
        if not line:
            break
        match = re.match(r"^([A-Za-z][A-Za-z0-9 /_-]{1,40}):\s+(.+)$", line)
        if not match:
            metadata = []
            return text, metadata
        metadata.append((match.group(1).strip(), match.group(2).strip()))
        if len(metadata) >= 6:
            break
        end_index += 1

    if not metadata:
        return text, metadata

    body_lines = lines[:probe_index] + lines[end_index + 1 :]
    return "\n".join(body_lines).strip(), metadata


def _extract_html_body(html_text: str) -> str:
    match = re.search(r"<body[^>]*>(.*)</body>", html_text, flags=re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return html_text


def _markdown_to_html_fragment(text: str) -> str:
    document = QTextDocument()
    if hasattr(document, "setMarkdown"):
        document.setMarkdown(text)
        return _extract_html_body(document.toHtml())
    document.setPlainText(text)
    return f"<pre class=\"plain-text\">{escape(text)}</pre>"


def _plain_text_to_html_fragment(text: str) -> str:
    return f"<pre class=\"plain-text\">{escape(text)}</pre>"


def _resolve_document_browser_theme(theme_tokens: Optional[dict] = None) -> dict:
    tokens = dict(theme_tokens or {})
    fallback = dict(_DOCUMENT_BROWSER_FALLBACK_THEME)
    return {
        "root_bg": str(tokens.get("surface_rgba") or fallback["root_bg"]),
        "panel_bg": str(tokens.get("panel_rgba") or fallback["panel_bg"]),
        "surface_bg": str(tokens.get("surface_alt_rgba") or tokens.get("surface_rgba") or fallback["surface_bg"]),
        "surface_alt_bg": str(tokens.get("status_subframe_bg") or tokens.get("button_bg") or fallback["surface_alt_bg"]),
        "field_bg": str(tokens.get("field_rgba") or fallback["field_bg"]),
        "field_text": str(tokens.get("field_text") or fallback["field_text"]),
        "border": str(tokens.get("border") or fallback["border"]),
        "text": str(tokens.get("text") or fallback["text"]),
        "muted": str(tokens.get("muted") or fallback["muted"]),
        "subtle": str(tokens.get("status_meta") or fallback["subtle"]),
        "title": str(tokens.get("hero_text") or tokens.get("text") or fallback["title"]),
        "accent": str(tokens.get("status_card_title") or tokens.get("accent") or fallback["accent"]),
        "accent_strong": str(tokens.get("accent") or fallback["accent_strong"]),
        "accent_soft": str(tokens.get("accent_soft") or tokens.get("border") or fallback["accent_soft"]),
        "accent_mid": str(tokens.get("accent_mid") or fallback["accent_mid"]),
        "hero_bg": str(tokens.get("hero_mid") or tokens.get("hero_start") or fallback["hero_bg"]),
        "hero_text": str(tokens.get("hero_text") or fallback["hero_text"]),
        "hero_subtle": str(tokens.get("hero_subtle") or fallback["hero_subtle"]),
        "button_bg": str(tokens.get("button_bg") or fallback["button_bg"]),
        "button_hover": str(tokens.get("button_hover") or fallback["button_hover"]),
        "button_text": str(tokens.get("button_text") or fallback["button_text"]),
        "selected_bg": str(tokens.get("button_checked") or tokens.get("accent_mid") or fallback["selected_bg"]),
        "selected_text": str(tokens.get("hero_text") or fallback["selected_text"]),
        "link": str(tokens.get("status_info") or tokens.get("accent") or fallback["link"]),
        "code_text": str(tokens.get("status_progress_tilt") or tokens.get("status_ok") or fallback["code_text"]),
        "radius": int(tokens.get("radius") or 14),
    }


def _build_document_browser_stylesheet(theme: dict) -> str:
    radius = max(10, int(theme.get("radius", 14)))
    radius_small = max(8, radius - 4)
    radius_large = radius + 2
    return (
        f"QWidget#smartSentryDocumentBrowser {{ background-color: {theme['root_bg']}; color: {theme['text']}; }}"
        f"QWidget#smartSentryDocumentBrowser QWidget#documentBrowserPane {{ background-color: {theme['panel_bg']}; border: 1px solid {theme['border']}; border-radius: {radius_large}px; }}"
        f"QWidget#smartSentryDocumentBrowser QLabel#documentBrowserIntro {{ color: {theme['muted']}; font-size: 13px; }}"
        f"QWidget#smartSentryDocumentBrowser QLabel#documentBrowserStatus {{ color: {theme['subtle']}; font-size: 12px; }}"
        f"QWidget#smartSentryDocumentBrowser QLabel#documentBrowserTitle {{ color: {theme['title']}; font-size: 20px; font-weight: 700; }}"
        f"QWidget#smartSentryDocumentBrowser QLabel#documentBrowserMeta {{ color: {theme['accent']}; font-size: 12px; }}"
        "QWidget#smartSentryDocumentBrowser QLineEdit,"
        "QWidget#smartSentryDocumentBrowser QComboBox,"
        "QWidget#smartSentryDocumentBrowser QListWidget,"
        "QWidget#smartSentryDocumentBrowser QTextBrowser {"
        f"background-color: {theme['field_bg']}; color: {theme['field_text']}; border: 1px solid {theme['border']}; border-radius: {radius_small}px;"
        "}"
        "QWidget#smartSentryDocumentBrowser QLineEdit,"
        f"QWidget#smartSentryDocumentBrowser QComboBox {{ padding: 8px 10px; min-height: 18px; }}"
        f"QWidget#smartSentryDocumentBrowser QListWidget::item {{ padding: 8px 10px; border-bottom: 1px solid {theme['border']}; }}"
        f"QWidget#smartSentryDocumentBrowser QListWidget::item:selected {{ background-color: {theme['selected_bg']}; color: {theme['selected_text']}; }}"
        f"QWidget#smartSentryDocumentBrowser QTextBrowser {{ padding: 14px; selection-background-color: {theme['accent_mid']}; selection-color: {theme['selected_text']}; }}"
        "QWidget#smartSentryDocumentBrowser QPushButton {"
        f"background-color: {theme['button_bg']}; color: {theme['button_text']}; border: 1px solid {theme['accent_soft']}; border-radius: {radius_small}px; padding: 8px 14px;"
        "}"
        f"QWidget#smartSentryDocumentBrowser QPushButton:hover {{ background-color: {theme['button_hover']}; border-color: {theme['accent_strong']}; }}"
        f"QWidget#smartSentryDocumentBrowser QSplitter::handle:horizontal {{ background-color: {theme['border']}; width: 6px; margin: 10px 2px; border-radius: 3px; }}"
        f"QWidget#smartSentryDocumentBrowser QSplitter::handle:horizontal:hover {{ background-color: {theme['accent_soft']}; }}"
    )


def _render_document_html(entry: DocumentBrowserEntry, text: str, theme: dict) -> str:
    metadata: list[tuple[str, str]] = []
    body_source = text.strip()
    if entry.absolute_path.suffix.lower() == ".md":
        body_source, metadata = _extract_leading_metadata(body_source)
        body_html = _markdown_to_html_fragment(body_source or text)
    else:
        body_html = _plain_text_to_html_fragment(body_source or text)

    meta_pairs: list[tuple[str, str]] = [("Category", entry.category)]
    meta_pairs.extend(metadata)
    meta_pairs.extend(
        [
            ("Path", entry.relative_path),
            ("Updated", _format_doc_timestamp(entry.absolute_path)),
        ]
    )

    meta_html = "".join(
        (
            "<div class=\"meta-chip\">"
            f"<span class=\"meta-key\">{escape(key)}</span>"
            f"<span class=\"meta-value\">{escape(value)}</span>"
            "</div>"
        )
        for key, value in meta_pairs
        if str(value).strip()
    )

    preview_text = entry.preview or "Live Smart Sentry repository documentation."
    radius = max(10, int(theme.get("radius", 14)))
    radius_small = max(8, radius - 4)
    radius_large = radius + 2
    return (
        "<!DOCTYPE html>"
        "<html><head><meta charset=\"utf-8\">"
        "<style>"
        f"body {{ margin: 0; padding: 0; background: {theme['panel_bg']}; color: {theme['text']}; font-family: 'Segoe UI', 'Trebuchet MS', sans-serif; }}"
        ".doc-shell { padding: 18px 18px 24px 18px; }"
        f".doc-header {{ padding: 18px; border: 1px solid {theme['accent_soft']}; border-radius: {radius_large}px; background: {theme['hero_bg']}; margin-bottom: 18px; }}"
        f".doc-eyebrow {{ color: {theme['accent_strong']}; font-size: 11px; font-weight: 700; letter-spacing: 1.4px; text-transform: uppercase; }}"
        f".doc-header h1 {{ margin: 10px 0 8px 0; color: {theme['hero_text']}; font-size: 28px; font-weight: 700; }}"
        f".doc-preview {{ margin: 0 0 14px 0; color: {theme['hero_subtle']}; font-size: 13px; line-height: 1.55; }}"
        ".doc-meta { margin-top: 8px; }"
        f".meta-chip {{ display: inline-block; margin: 0 8px 8px 0; padding: 7px 10px; border-radius: 999px; background: {theme['surface_alt_bg']}; border: 1px solid {theme['accent_soft']}; }}"
        f".meta-key {{ color: {theme['accent_strong']}; font-size: 11px; font-weight: 700; text-transform: uppercase; margin-right: 8px; }}"
        f".meta-value {{ color: {theme['hero_text']}; font-size: 12px; }}"
        f".doc-body {{ color: {theme['text']}; font-size: 14px; line-height: 1.62; }}"
        f".doc-body h1, .doc-body h2, .doc-body h3, .doc-body h4 {{ color: {theme['title']}; font-weight: 700; margin-top: 20px; margin-bottom: 10px; }}"
        f".doc-body h1 {{ font-size: 24px; border-bottom: 1px solid {theme['border']}; padding-bottom: 8px; }}"
        f".doc-body h2 {{ font-size: 20px; color: {theme['accent_strong']}; }}"
        f".doc-body h3 {{ font-size: 17px; color: {theme['accent']}; }}"
        f".doc-body h4 {{ font-size: 15px; color: {theme['accent']}; }}"
        f".doc-body p, .doc-body li {{ color: {theme['text']}; }}"
        f".doc-body a {{ color: {theme['link']}; text-decoration: none; font-weight: 600; }}"
        f".doc-body strong {{ color: {theme['title']}; }}"
        f".doc-body em {{ color: {theme['accent']}; }}"
        f".doc-body blockquote {{ margin: 14px 0; padding: 10px 14px; background: {theme['surface_alt_bg']}; border-left: 4px solid {theme['accent_strong']}; color: {theme['text']}; border-radius: {radius_small}px; }}"
        ".doc-body ul, .doc-body ol { margin: 8px 0 12px 18px; }"
        f".doc-body code {{ background: {theme['surface_alt_bg']}; color: {theme['code_text']}; padding: 2px 6px; border-radius: 6px; font-family: 'Consolas', 'Cascadia Mono', monospace; }}"
        f".doc-body pre, .plain-text {{ white-space: pre-wrap; background: {theme['field_bg']}; color: {theme['field_text']}; padding: 14px; border-radius: {radius_large}px; border: 1px solid {theme['border']}; font-family: 'Consolas', 'Cascadia Mono', monospace; }}"
        f".doc-body table {{ width: 100%; border-collapse: collapse; margin: 14px 0; background: {theme['surface_bg']}; }}"
        f".doc-body th {{ background: {theme['surface_alt_bg']}; color: {theme['accent_strong']}; font-weight: 700; }}"
        f".doc-body th, .doc-body td {{ border: 1px solid {theme['border']}; padding: 8px 10px; text-align: left; }}"
        f".doc-body hr {{ border: none; border-top: 1px solid {theme['border']}; margin: 18px 0; }}"
        "</style></head><body>"
        "<div class=\"doc-shell\">"
        "<div class=\"doc-header\">"
        "<div class=\"doc-eyebrow\">Smart Sentry Documentation</div>"
        f"<h1>{escape(entry.title)}</h1>"
        f"<p class=\"doc-preview\">{escape(preview_text)}</p>"
        f"<div class=\"doc-meta\">{meta_html}</div>"
        "</div>"
        f"<div class=\"doc-body\">{body_html}</div>"
        "</div></body></html>"
    )


def _scan_documents(root: Path) -> List[DocumentBrowserEntry]:
    entries: List[DocumentBrowserEntry] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in DOCUMENT_BROWSER_SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in DOCUMENT_BROWSER_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
        except Exception:
            continue
        relative_path = path.relative_to(root).as_posix()
        category, priority = _infer_category(Path(relative_path))
        title = _humanize_title(path)
        preview = _preview_excerpt(text)
        headings = " ".join(re.findall(r"^#+\s+(.+)$", text, flags=re.MULTILINE)[:8])
        search_blob = " ".join((title, relative_path, category, headings, text[:6000]))
        file_blob = " ".join((title, relative_path, category))
        content_blob = " ".join((headings, text[:12000]))
        entries.append(
            DocumentBrowserEntry(
                title=title,
                relative_path=relative_path,
                absolute_path=path,
                category=category,
                preview=preview,
                search_text=_normalize_search_text(search_blob),
                file_search_text=_normalize_search_text(file_blob),
                content_search_text=_normalize_search_text(content_blob),
                body_text=text,
                priority=priority,
            )
        )
    entries.sort(key=lambda item: (item.priority, item.category, item.relative_path.lower()))
    return entries


_DOCUMENT_BROWSER_STYLE = (
    "QWidget#smartSentryDocumentBrowser { background-color: #15120f; color: #f0e7dc; }"
    "QWidget#smartSentryDocumentBrowser QLabel#documentBrowserIntro { color: #d7c5b4; font-size: 13px; }"
    "QWidget#smartSentryDocumentBrowser QLabel#documentBrowserStatus { color: #bca694; font-size: 12px; }"
    "QWidget#smartSentryDocumentBrowser QLabel#documentBrowserTitle { color: #fff4e5; font-size: 20px; font-weight: 700; }"
    "QWidget#smartSentryDocumentBrowser QLabel#documentBrowserMeta { color: #cfae88; font-size: 12px; }"
    "QWidget#smartSentryDocumentBrowser QLineEdit,"
    "QWidget#smartSentryDocumentBrowser QComboBox,"
    "QWidget#smartSentryDocumentBrowser QListWidget,"
    "QWidget#smartSentryDocumentBrowser QTextBrowser {"
    "background-color: #1f1914; color: #f2eadf; border: 1px solid #544032; border-radius: 10px;"
    "}"
    "QWidget#smartSentryDocumentBrowser QLineEdit,"
    "QWidget#smartSentryDocumentBrowser QComboBox { padding: 8px 10px; min-height: 18px; }"
    "QWidget#smartSentryDocumentBrowser QListWidget::item { padding: 8px 10px; border-bottom: 1px solid #2b241e; }"
    "QWidget#smartSentryDocumentBrowser QListWidget::item:selected { background-color: #3a2b1f; color: #fff0d9; }"
    "QWidget#smartSentryDocumentBrowser QTextBrowser { padding: 14px; selection-background-color: #7b5632; }"
    "QWidget#smartSentryDocumentBrowser QPushButton {"
    "background-color: #2e241d; color: #f2eadf; border: 1px solid #6f523e; border-radius: 9px; padding: 8px 14px;"
    "}"
    "QWidget#smartSentryDocumentBrowser QPushButton:hover { background-color: #413126; }"
)


class SmartSentryDocumentBrowserWidget(QWidget):
    def __init__(
        self,
        *,
        root: Path,
        parent: Optional[QWidget] = None,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        super().__init__(parent)
        self._root = Path(root).resolve()
        self._on_log = on_log or (lambda _msg: None)
        self._entries: List[DocumentBrowserEntry] = []
        self._visible_entries: List[DocumentBrowserEntry] = []
        self._current_entry: Optional[DocumentBrowserEntry] = None
        self._active_search_tokens: List[str] = []
        self._theme = _resolve_document_browser_theme()

        self.setObjectName("smartSentryDocumentBrowser")
        self.setMinimumHeight(520)

        root_lay = QVBoxLayout(self)
        root_lay.setContentsMargins(14, 14, 14, 14)
        root_lay.setSpacing(10)

        controls_row = QHBoxLayout()
        controls_row.setContentsMargins(0, 0, 0, 0)
        controls_row.setSpacing(8)

        self._search_edit = QLineEdit()
        self._search_edit.setPlaceholderText("Quick search docs, filenames, and content")
        self._search_edit.setClearButtonEnabled(True)
        self._search_edit.textChanged.connect(self._apply_filters)
        controls_row.addWidget(self._search_edit, 1)

        self._category_combo = QComboBox()
        self._category_combo.currentIndexChanged.connect(self._apply_filters)
        controls_row.addWidget(self._category_combo)

        self._refresh_button = QPushButton("Refresh")
        self._refresh_button.clicked.connect(self.refresh_documents)
        controls_row.addWidget(self._refresh_button)

        root_lay.addLayout(controls_row)

        intro = QLabel(
            "Browse Smart Sentry manuals, guides, reports, and validation notes from one searchable window. "
            "Quick search matches filenames and document content while keeping the file list compact."
        )
        intro.setWordWrap(True)
        intro.setObjectName("documentBrowserIntro")
        root_lay.addWidget(intro)

        self._status_label = QLabel("")
        self._status_label.setObjectName("documentBrowserStatus")
        root_lay.addWidget(self._status_label)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)

        left_host = QWidget()
        left_host.setObjectName("documentBrowserPane")
        left_lay = QVBoxLayout(left_host)
        left_lay.setContentsMargins(0, 0, 0, 0)
        left_lay.setSpacing(8)

        self._document_list = QListWidget()
        self._document_list.currentRowChanged.connect(self._on_document_selected)
        self._document_list.itemDoubleClicked.connect(lambda _item: self._open_current_document_externally())
        left_lay.addWidget(self._document_list, 1)

        splitter.addWidget(left_host)

        right_host = QWidget()
        right_host.setObjectName("documentBrowserPane")
        right_lay = QVBoxLayout(right_host)
        right_lay.setContentsMargins(0, 0, 0, 0)
        right_lay.setSpacing(8)

        self._title_label = QLabel("Select a document")
        self._title_label.setObjectName("documentBrowserTitle")
        self._title_label.setWordWrap(True)
        right_lay.addWidget(self._title_label)

        self._meta_label = QLabel("")
        self._meta_label.setObjectName("documentBrowserMeta")
        self._meta_label.setWordWrap(True)
        right_lay.addWidget(self._meta_label)

        action_row = QHBoxLayout()
        action_row.setContentsMargins(0, 0, 0, 0)
        action_row.setSpacing(8)

        self._open_file_button = QPushButton("Open File")
        self._open_file_button.clicked.connect(self._open_current_document_externally)
        action_row.addWidget(self._open_file_button)

        self._open_folder_button = QPushButton("Open Folder")
        self._open_folder_button.clicked.connect(self._open_current_document_folder)
        action_row.addWidget(self._open_folder_button)

        action_row.addStretch(1)
        right_lay.addLayout(action_row)

        self._browser = QTextBrowser()
        self._browser.setOpenExternalLinks(True)
        self._browser.setReadOnly(True)
        self._browser.setLineWrapMode(QTextBrowser.WidgetWidth)
        right_lay.addWidget(self._browser, 1)

        splitter.addWidget(right_host)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([340, 920])

        root_lay.addWidget(splitter, 1)

        self.apply_theme_tokens()

        self.refresh_documents()

    def apply_theme_tokens(self, theme_tokens: Optional[dict] = None) -> None:
        self._theme = _resolve_document_browser_theme(theme_tokens)
        self.setStyleSheet(_build_document_browser_stylesheet(self._theme))
        if self._current_entry is not None:
            self._browser.setHtml(_render_document_html(self._current_entry, self._current_entry.body_text, self._theme))
            self._browser.moveCursor(self._browser.textCursor().Start)

    def set_search_query(self, query: str, *, focus_search: bool = False) -> None:
        search_text = str(query or "").strip()
        current_text = str(self._search_edit.text() or "")
        if current_text != search_text:
            self._search_edit.setText(search_text)
        else:
            self._apply_filters()
        if focus_search:
            self._search_edit.setFocus(Qt.OtherFocusReason)
            self._search_edit.selectAll()

    def refresh_documents(self) -> None:
        self._entries = _scan_documents(self._root)
        categories = sorted({entry.category for entry in self._entries})
        current_category = str(self._category_combo.currentText() or "All")
        self._category_combo.blockSignals(True)
        self._category_combo.clear()
        self._category_combo.addItem("All")
        for category in categories:
            self._category_combo.addItem(category)
        category_index = max(0, self._category_combo.findText(current_category))
        self._category_combo.setCurrentIndex(category_index)
        self._category_combo.blockSignals(False)
        self._apply_filters()

    def _apply_filters(self) -> None:
        selected_category = str(self._category_combo.currentText() or "All")
        self._visible_entries, self._active_search_tokens = _build_search_results(
            self._entries,
            query=self._search_edit.text(),
            selected_category=selected_category,
        )

        previous_path = self._current_entry.relative_path if self._current_entry is not None else ""
        self._document_list.blockSignals(True)
        self._document_list.clear()
        selected_row = -1
        for index, entry in enumerate(self._visible_entries):
            item = QListWidgetItem(entry.absolute_path.name)
            item.setToolTip(entry.relative_path)
            item.setData(Qt.UserRole, entry.relative_path)
            self._document_list.addItem(item)
            if entry.relative_path == previous_path:
                selected_row = index
        self._document_list.blockSignals(False)

        if self._active_search_tokens:
            self._status_label.setText(
                f"{len(self._visible_entries)} matching file(s) from {len(self._entries)} indexed document(s) under {self._root.as_posix()}"
            )
        else:
            self._status_label.setText(
                f"{len(self._visible_entries)} document(s) shown from {len(self._entries)} indexed file(s) under {self._root.as_posix()}"
            )

        if self._visible_entries:
            if selected_row < 0:
                selected_row = 0
            self._document_list.setCurrentRow(selected_row)
            self._on_document_selected(selected_row)
            return

        self._current_entry = None
        self._title_label.setText("No matching documentation results")
        self._meta_label.setText("Try a broader search or switch the category filter.")
        self._browser.setPlainText("")

    def _on_document_selected(self, row: int) -> None:
        if row < 0 or row >= len(self._visible_entries):
            self._current_entry = None
            return
        entry = self._visible_entries[row]
        self._current_entry = entry
        self._title_label.setText(entry.title)
        self._meta_label.setText(f"{entry.category} | {entry.relative_path}")
        try:
            text = entry.absolute_path.read_text(encoding="utf-8-sig", errors="ignore")
        except Exception as exc:
            self._browser.setPlainText(f"Unable to read document:\n{exc}")
            self._on_log(f"Document browser read failed for {entry.relative_path}: {exc}")
            return
        self._browser.setSearchPaths([str(self._root), str(entry.absolute_path.parent)])
        self._browser.setHtml(_render_document_html(entry, text, self._theme))
        self._browser.moveCursor(self._browser.textCursor().Start)
        if self._active_search_tokens:
            self._scroll_browser_to_active_match()

    def _scroll_browser_to_active_match(self) -> None:
        if not self._active_search_tokens:
            return
        self._browser.moveCursor(self._browser.textCursor().Start)
        for token in self._active_search_tokens:
            if self._browser.find(token):
                return
        self._browser.moveCursor(self._browser.textCursor().Start)

    def _open_current_document_externally(self) -> None:
        entry = self._current_entry
        if entry is None:
            return
        if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(entry.absolute_path))):
            self._on_log(f"Document browser open file failed: {entry.relative_path}")

    def _open_current_document_folder(self) -> None:
        entry = self._current_entry
        if entry is None:
            return
        folder_path = entry.absolute_path.parent
        if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(folder_path))):
            self._on_log(f"Document browser open folder failed: {folder_path.as_posix()}")


class SmartSentryDocumentBrowserDialog(QDialog):
    def __init__(
        self,
        *,
        root: Path,
        parent: Optional[QWidget] = None,
        on_log: Optional[Callable[[str], None]] = None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("Smart Sentry Document Browser")
        self.resize(1260, 820)
        self.setModal(False)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._browser_widget = SmartSentryDocumentBrowserWidget(
            root=root,
            parent=self,
            on_log=on_log,
        )
        layout.addWidget(self._browser_widget)

    def apply_theme_tokens(self, theme_tokens: Optional[dict] = None) -> None:
        self._browser_widget.apply_theme_tokens(theme_tokens)

    def set_search_query(self, query: str, *, focus_search: bool = False) -> None:
        self._browser_widget.set_search_query(query, focus_search=focus_search)

    def refresh_documents(self) -> None:
        self._browser_widget.refresh_documents()