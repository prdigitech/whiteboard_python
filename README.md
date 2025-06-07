````markdown
# 🖌️ Python Whiteboard

A simple cross-platform whiteboard application built with Python and Tkinter.  
You can draw with different brush sizes, choose colors, use an eraser, and save your work as PNG.

## 📦 Requirements

- Python 3.8 or higher
- `tkinter` (usually comes with Python)
- `Pillow` (for saving images)

## 🛠️ Installation

```bash
python3 -m venv whiteboard-env
source whiteboard-env/bin/activate  # On Windows: whiteboard-env\Scripts\activate
pip install pillow
````

## 🚀 Run the Application

```bash
python whiteboard.py
```

## 🖥️ Create as Desktop Application

### 🐧 For Ubuntu / Linux

```ini
[Desktop Entry]
Name=Python Whiteboard
Exec=/home/your-username/PratikR/Whiteboard/whiteboard-env/bin/python /home/your-username/PratikR/Whiteboard/whiteboard.py
Icon=/home/your-username/PratikR/Whiteboard/whiteboard.png
Terminal=false
Type=Application
Categories=Utility;
```

```bash
chmod +x whiteboard.desktop
sudo mv whiteboard.desktop /usr/share/applications/
```

### 🪟 For Windows

Target:

```
"C:\Path\To\whiteboard-env\Scripts\python.exe" "C:\Path\To\whiteboard.py"
```

Start in:

```
C:\Path\To\
```

### 🍏 For macOS

Automator → New Application → Run Shell Script:

```bash
source /path/to/whiteboard-env/bin/activate
python /path/to/whiteboard.py
```

Save as `Whiteboard.app`, then customize icon via Finder.

## 🧱 Features

* Draw with variable brush sizes
* Select any color
* Erase with background color
* Save your drawing as a PNG image
* Lightweight and easy to use

## 📄 License

MIT License

```
```
