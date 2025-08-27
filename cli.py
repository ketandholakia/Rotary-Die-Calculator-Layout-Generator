import argparse
from cylinders import get_cylinder_fits_with_gap
from svg_preview import generate_svg_with_repeats

def main():
    parser = argparse.ArgumentParser(description="Rotary Die Cylinder Selector")
    parser.add_argument("label_height", type=float, help="Label height (along cylinder) in mm")
    parser.add_argument("--width", type=float, default=50.0, help="Label width (across die) in mm")
    parser.add_argument("--repeats", type=int, default=1, help="Number of full-around repeats across die")
    parser.add_argument("--svg", action="store_true", help="Generate SVG preview")
    parser.add_argument("--min-gap", type=float, default=3.0, help="Minimum total gap in mm")
    args = parser.parse_args()

    fits = get_cylinder_fits_with_gap(args.label_height, min_total_gap_mm=args.min_gap)
    if not fits:
        print("No suitable cylinders found.")
        return

    print("\nBest cylinder options:")
    for fit in fits:
        print(f"Teeth: {fit['teeth']}, Labels: {fit['labels']}, Total gap: {fit['total_gap_mm']} mm, Gap per label: {fit['gap_per_label_mm']} mm")
        if args.svg:
            generate_svg_with_repeats(
                fit['circumference_mm'],
                args.label_height,
                fit['labels'],
                fit['gap_per_label_mm'],
                args.width,
                args.repeats,
                f"layout_{fit['teeth']}T.svg"
            )

if __name__ == "__main__":
    main()