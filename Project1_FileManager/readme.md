# 📂 Smart File Manager (OS Automation)

## 🎯 Project Goal
This Python-based utility automates the organization of cluttered directories by intelligently sorting files into categorized folders based on their extensions.

## 🛠 Features
- **Auto-Categorization:** Sorts files into `Documents`, `Images`, `Media`, and `Archives`.
- **Extension Mapping:** Recognizes common formats like `.pdf`, `.docx`, `.jpg`, `.zip`, etc.
- **Safety First:** Skips existing folders to prevent recursive loops.

## 💻 Tech Stack
- **Language:** Python 3
- **Libraries:** `os`, `shutil` (Standard Library)

## 📊 Sample Output
**Before running:**
`Downloads/` contains `report.pdf`, `vacation.jpg`, `script.py`, `data.zip`

**After running:**
- `Downloads/Documents/report.pdf`
- `Downloads/Images/vacation.jpg`
- `Downloads/Archives/data.zip`
