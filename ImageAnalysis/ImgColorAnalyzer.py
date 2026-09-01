from PIL import Image
from collections import Counter

def analyze_colors(input_path, color_count):

    try:
        with Image.open(input_path) as image:
            image = image.convert("RGB")
            colors = Counter(image.getdata())

            print("\nColor Analysis")
            print(f"Image Size: {image.width} x {image.height}")
            print(f"Analyzing Top {color_count} Colors:\n")

            for index, (color, count) in enumerate(
                colors.most_common(color_count),
                start=1
            ):
                print(f"{index}. RGB{color} "f"- {count} pixels")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError:
        print("\nError: Color count must be a positive integer.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Color Analyzer")

    input_path = input("Enter image path: ").strip()

    try:
        color_count = int(input("Enter number of colors to display: "))

        if color_count <= 0:
            raise ValueError

        analyze_colors(input_path, color_count)

    except ValueError:
        print("\nError: Enter a positive integer.")