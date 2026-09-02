from PIL import Image
from pathlib import Path


def optimize_image(input_path, output_path):

    try:
        input_file = Path(input_path)

        if not input_file.exists():
            raise FileNotFoundError

        with Image.open(input_file) as image:
            original_size = input_file.stat().st_size

            image.save(
                output_path,
                optimize=True)

            optimized_size = Path(output_path).stat().st_size

            print("\nImage optimized successfully!")
            print(f"Original Size  : {original_size / 1024:.2f} KB")
            print(f"Optimized Size : {optimized_size / 1024:.2f} KB")
            print(f"Saved To       : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Optimizer")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    optimize_image(
        input_path,
        output_path)