🌀 Rotary Die Calculator
A modular Python application for selecting rotary die cylinders based on label dimensions, calculating optimal fit with minimum gap, and generating realistic SVG previews—including multi-repeat layouts and rounded corners.

https://img.shields.io/badge/python-3.8%252B-blue
https://img.shields.io/badge/license-MIT-green

🔧 Features
✅ Calculates best-fit cylinder from teeth-based inventory

✅ Supports label height (around) and width (across)

✅ Ensures minimum gap between labels (≥ 3 mm)

✅ Generates multi-repeat layouts across the die

✅ SVG previews with rounded corners and hairline strokes

✅ GUI interface for quick input and visualization

📦 Installation
bash
git clone https://github.com/your-username/rotary_die_calc.git
cd rotary_die_calc
pip install -r requirements.txt
Requires Python 3.8+

🖥️ CLI Usage
bash
python cli.py <label_height_mm> --width <label_width_mm> --repeats <repeat_count> --svg
Example:
bash
python cli.py 60 --width 45 --repeats 3 --svg
This will:

Select cylinders that fit 60 mm tall × 45 mm wide labels

Repeat the full-around layout 3 times across the die

Generate SVG previews like layout_96T.svg

🖼️ GUI Usage
bash
python gui.py
Launches a simple Tkinter interface to:

Input label dimensions and repeat count

View best-fit cylinder options

Generate SVG previews with one click

📁 Project Structure
text
rotary_die_calc/
├── cli.py               # Command-line interface
├── gui.py               # GUI interface (Tkinter)
├── cylinders.py         # Core logic: cylinder fit calculation
├── svg_preview.py       # SVG layout generator with repeat support
├── requirements.txt     # Python dependencies
└── README.md           # This file
🧠 Logic Overview
Teeth count → circumference (8 teeth = 1 inch)

Circumference → max label count with gap ≥ 3 mm

Repeat count → full-around layout duplication across die

SVG → stacked vertical labels with rounded corners and hairline stroke

📸 Preview Example
https://via.placeholder.com/400x200?text=SVG+Layout+Preview

📜 License
MIT License

Built by Ketan — pragmatic builder of modular manufacturing tools.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 Changelog
v1.0.0 (2023-11-15)

Initial release

Core cylinder calculation logic

CLI and GUI interfaces

SVG preview generation

🐛 Reporting Issues
If you encounter any problems, please open an issue on GitHub.
