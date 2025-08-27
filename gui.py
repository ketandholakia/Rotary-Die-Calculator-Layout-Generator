import tkinter as tk
from tkinter import messagebox
from cylinders import get_cylinder_fits_with_gap
from svg_preview import generate_svg_with_repeats

def run_calculation():
    try:
        label_height = float(entry_height.get())
        label_width = float(entry_width.get())
        repeats = int(entry_repeats.get())
        min_gap = 3.0

        fits = get_cylinder_fits_with_gap(label_height, min_total_gap_mm=min_gap)
        if not fits:
            messagebox.showinfo("Result", "No suitable cylinders found.")
            return

        result_text.delete("1.0", tk.END)
        for fit in fits:
            result_text.insert(tk.END, f"Teeth: {fit['teeth']}, Labels: {fit['labels']}, Gap: {fit['gap_per_label_mm']} mm\n")
            generate_svg_with_repeats(
                fit['circumference_mm'],
                label_height,
                fit['labels'],
                fit['gap_per_label_mm'],
                label_width,
                repeats,
                f"layout_{fit['teeth']}T.svg"
            )
        messagebox.showinfo("SVG", "SVG files generated successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Rotary Die Calculator")

tk.Label(root, text="Label Around Size (mm):").grid(row=0, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1)

tk.Label(root, text="Label Across (mm):").grid(row=1, column=0)
entry_width = tk.Entry(root)
entry_width.grid(row=1, column=1)

tk.Label(root, text="Across Repeat Count:").grid(row=2, column=0)
entry_repeats = tk.Entry(root)
entry_repeats.grid(row=2, column=1)

tk.Button(root, text="Calculate & Preview", command=run_calculation).grid(row=3, column=0, columnspan=2)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, column=0, columnspan=2)

root.mainloop()