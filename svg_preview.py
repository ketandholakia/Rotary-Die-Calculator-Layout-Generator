import svgwrite

def generate_svg_with_repeats(circumference_mm, label_height_mm, label_count, gap_mm, label_width_mm, repeat_count, filename):
    repeat_gap_mm = 3.0
    corner_radius_mm = 3.0

    dwg_width = (repeat_count * label_width_mm) + ((repeat_count - 1) * repeat_gap_mm)
    dwg_height = (label_count * label_height_mm) + ((label_count - 1) * gap_mm) + 40

    dwg = svgwrite.Drawing(filename, size=(dwg_width, dwg_height))

    for r in range(repeat_count):
        x_offset = r * (label_width_mm + repeat_gap_mm)
        y = 20
        for i in range(label_count):
            dwg.add(dwg.rect(
                insert=(x_offset, y),
                size=(label_width_mm, label_height_mm),
                rx=corner_radius_mm,
                ry=corner_radius_mm,
                fill='lightblue',
                stroke='black',
                stroke_width=0.01  # Hairline stroke

            ))
            y += label_height_mm + gap_mm

    dwg.save()