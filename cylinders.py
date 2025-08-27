import math

TEETH_OPTIONS = [66, 68, 72, 76, 82, 86, 90, 94, 96, 98, 102, 106, 112, 132, 120, 126]
TEETH_PER_INCH = 8
INCH_TO_MM = 25.4

def get_cylinder_fits_with_gap(label_height_mm, min_total_gap_mm=3.0):
    results = []

    for teeth in TEETH_OPTIONS:
        circumference = (teeth / TEETH_PER_INCH) * INCH_TO_MM
        max_labels = int(circumference / label_height_mm)

        for label_count in range(max_labels, 0, -1):
            used_space = label_count * label_height_mm
            total_gap = circumference - used_space
            gap_per_label = total_gap / label_count

            if total_gap >= min_total_gap_mm and gap_per_label >= 0.1:
                results.append({
                    'teeth': teeth,
                    'circumference_mm': round(circumference, 2),
                    'labels': label_count,
                    'gap_per_label_mm': round(gap_per_label, 2),
                    'total_gap_mm': round(total_gap, 2)
                })
                break  # Only best fit per cylinder

    return sorted(results, key=lambda x: x['gap_per_label_mm'])