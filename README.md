# PDF Compare

A local web app for viewing and comparing PDFs, spreadsheets (XLSX), and CSVs
side by side. Upload individual files, or a ZIP archive whose top-level
folders are grouped as columns (e.g. one folder per source app). Upload
multiple ZIPs to compare several "users" at once: each ZIP becomes its own
vertically-scrolling column of app-folders, with users laid out side by side.

## Setup

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## Run

```bash
./venv/bin/python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Then open http://127.0.0.1:8000 in a browser.

## Features

- Upload PDF / XLSX / CSV files individually, or drop a ZIP to import many
  at once, grouped by folder.
- Drop multiple ZIPs to compare several users side by side — each ZIP's
  app-folders stack and scroll vertically within that user's column.
- Side-by-side PDF viewing with independent zoom and pan per document.
- Spreadsheet preview (all sheets, with a row/column cap for very large files).
- Sync scrolling, either across every open document or per folder.
- Full-screen focus view for a single document or an entire folder.
- Per-folder review marks (✓ / ✗), download, and remove.

## Standalone macOS app

`launcher.py` wraps the same server into a double-clickable macOS app (starts
the server on a free local port, opens the browser, and adds a menu-bar icon
with an Open/Quit control). Build it with:

```bash
./venv/bin/pip install pyinstaller rumps
./venv/bin/pyinstaller --name "PDF Compare" --windowed --add-data "static:static" launcher.py
hdiutil create -volname "PDF Compare" -srcfolder "dist/PDF Compare.app" -ov -format UDZO "PDF Compare.dmg"
```

The build is unsigned, so recipients need to right-click → Open the first
time (or allow it via System Settings → Privacy & Security) to get past
Gatekeeper.

## Also in this repo

`pdf_viewer.py` is an earlier, separate desktop prototype (PySide6 + PyMuPDF)
for viewing multiple PDFs side by side. It predates and is unrelated to the
web app above.

```bash
./venv/bin/python pdf_viewer.py               # empty, then use "Add PDFs" or drag & drop
./venv/bin/python pdf_viewer.py a.pdf b.pdf   # open with files preloaded
```
