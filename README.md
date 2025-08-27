# 🌀 Rotary Die Calculator

A modular Python application for selecting rotary die cylinders based on label dimensions, calculating optimal fit with minimum gap, and generating realistic SVG previews—including multi-repeat layouts and rounded corners.

## 🔧 Features

- ✅ Calculates best-fit cylinder from teeth-based inventory
- ✅ Supports label height (around) and width (across)
- ✅ Ensures minimum gap between labels (≥ 3 mm)
- ✅ Generates multi-repeat layouts across the die
- ✅ SVG previews with rounded corners and hairline strokes
- ✅ GUI interface for quick input and visualization

## 📦 Installation

```bash
git clone https://github.com/your-username/rotary_die_calc.git
cd rotary_die_calc
pip install -r requirements.txt

```bash

Requires Python 3.8+

## 🖥️ CLI Usage
python cli.py <label_height_mm> --width <label_width_mm> --repeats <repeat_count> --svg


# Example:

```bash
python cli.py 60 --width 45 --repeats 3 --svg


This will:
- Select cylinders that fit 60 mm tall × 45 mm wide labels
- Repeat the full-around layout 3 times across the die
- Generate SVG previews like layout_96T.svg

## 🖼️ GUI Usage

```bash
python gui.py


Launches a simple Tkinter interface to:
- Input label dimensions and repeat count
- View best-fit cylinder options
- Generate SVG previews with one click
## 📁 Project Structure
rotary_die_calc/
├── cli.py               # Command-line interface
├── gui.py               # GUI interface (Tkinter)
├── cylinders.py         # Core logic: cylinder fit calculation
├── svg_preview.py       # SVG layout generator with repeat support


## 🧠 Logic Overview
- Teeth count → circumference (8 teeth = 1 inch)
- Circumference → max label count with gap ≥ 3 mm
- Repeat count → full-around layout duplication across die
- SVG → stacked vertical labels with rounded corners and hairline stroke
## 📜 License
MIT License

Built by Ketan — pragmatic builder of modular manufacturing tools.

---

Let me know if you'd like a badge section (e.g. Python version, license), or a GIF preview of the SVG layout. I can also help write a changelog or contribution guide if you're planning to open-source it.
