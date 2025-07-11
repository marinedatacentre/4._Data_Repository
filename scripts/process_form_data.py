import pandas as pd
from pathlib import Path

# === CONFIG ===
EXCEL_PATH = Path("data/Template for Processes.xlsx")
# Point at the repo root, not a subfolder
OUTPUT_DIR = Path(".")

# === LOAD & NORMALIZE ===
df = pd.read_excel(EXCEL_PATH)
df.columns = [c.replace("\xa0", " ").strip() for c in df.columns]

for idx, row in df.iterrows():
    # Read your key fields
    folder_type     = row.get("Pick a Folder", "").strip()
    section1        = row.get("Section/Category3", "").strip()
    process_title   = row.get("Process Title", "").strip()
    process_number  = row.get("Process Number", "").strip()
    created_by      = row.get("Created by", "").strip()
    review_period   = row.get("Review Period", "").strip()
    purpose         = row.get("Purpose", "").strip()

    # Only use the Section/Category folder
    section_folder = section1 or "Uncategorized"

    # Build the filename
    safe_number = process_number.replace(" ", "_").replace("/", "-")
    safe_title  = process_title.replace(" ", "_").replace("/", "-")
    filename    = f"{safe_number}_{safe_title}.md"

    # THIS IS THE CRITICAL LINE:
    folder_path = Path(section_folder)  # NOT OUTPUT_DIR / section_category
    file_path   = folder_path / filename

    # Debug logging
    print(f"→ Writing to: {file_path}")

    # Skip if already exists
    if file_path.exists():
        print(f"  • Skipped (already exists)")
        continue

    # Create folder if needed
    folder_path.mkdir(parents=True, exist_ok=True)

    # Build your Markdown
    md = f"""---
title: {process_title}
author: {created_by}
date: {row.get('Start time', '')}
review_period: {review_period or '3 years'}
---

## Purpose
{purpose}

## Steps

| Step | Major Activity | References, Forms and Details |
|------|----------------|-------------------------------|
"""
    for i in range(1, 21):
        major = row.get(f"Step {i}: Major Activity", "")
        detail = row.get(f"Step {i}: References, Forms and Details", "")
        if isinstance(major, str) and major.strip():
            md += f"| {i} | {major.strip()} | {str(detail).strip() or 'N/A'} |\n"

    # Write out the file
    file_path.write_text(md, encoding="utf-8")
    print(f"✅ Created: {file_path}")
