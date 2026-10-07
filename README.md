# Medical App

A desktop application that speeds up the writing of **frottis** (cervical smear) and **cytology** reports. Instead of typing every sentence, the user picks ready-made phrases from drop-down menus, fills in the details, and saves the report straight into a Word document.

## Features

- **Phrase menus organized by report section**, each with several equivalent wordings:
  - Header (exocervical, junctional and endocervical smears, with 2 or 3 slides, FCV, and other sampling sites)
  - Inflammation, graded from 0/10 to more than 7/10
  - Background of the slide (clean, granular, dirty, and mixed aspects)
  - Mucus, with or without blood
  - Flora (lactobacilli)
  - Germs and parasites (trichomonas, mycosis, actinomycosis)
  - Epithelial population (squamous cells by layer, abundance and morphology; glandular cells; metaplasia)
- **Insert at cursor**: the chosen phrase is added where the cursor is in the text editor.
- **Export to Word**: `Ctrl + S` appends the written text to an existing `.docx` file.
- **Unsaved-changes prompt** when closing the window.
- **Standalone executable** in the `dist` folder, no Python installation needed.

## Usage

1. Open the application (the executable in `dist`, or `python app.py`).
2. Click a section button (for example *En-tete* or *Inflammation*) to open its phrase menu, then choose a phrase. It is inserted in the text editor.
3. Complete the phrases directly in the editor. Keyboard shortcuts are available.
4. Press `Ctrl + S`, pick the Word document to use, and the text is appended to it.

On a laptop, scroll the button panel with two fingers on the trackpad.

## Repository structure

```
.
├── app.py               # Application source code (Tkinter)
├── app.spec             # PyInstaller build configuration
├── app_logo.ico         # Application icon (executable)
├── app_logo.png         # Application logo
├── groups.txt           # Phrase groups list
├── Test_document.docx   # Sample Word document to try the export
├── build/               # PyInstaller build files
└── dist/                # Ready-to-use executable
```

## Run from source

```bash
git clone https://github.com/sarahmoussaoui/Medical-App.git
cd Medical-App

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install python-docx

python app.py
```

`tkinter` ships with Python. On some Linux distributions install it separately (`sudo apt install python3-tk`).

## Build the executable

```bash
pip install pyinstaller
pyinstaller app.spec
```

The executable is generated in the `dist` folder.

## Note

The application only helps with writing and formatting report text. The content of each report remains the responsibility of the practitioner.
