from PIL import Image
from pathlib import Path


def reduce_quality(input_path, output_path, quality):

    try:
        input_file = Path(input_path)

        if not input_file.exists():
            raise FileNotFoundError

        with Image.open(input_file) as image:
            original_size = input_file.stat().st_size

            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")

            image.save(
                output_path,
                "JPEG",
                quality=quality,
                optimize=True)

            reduced_size = Path(output_path).stat().st_size

            print("\nImage quality reduced successfully!")
            print(f"Original Size : {original_size / 1024:.2f} KB")
            print(f"New Size      : {reduced_size / 1024:.2f} KB")
            print(f"Quality       : {quality}")
            print(f"Saved To      : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError:
        print("\nError: Quality must be between 1 and 95.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Quality Reducer")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        quality = int(input("Enter quality (1-95): "))

        if not 1 <= quality <= 95:
            raise ValueError

        reduce_quality(
            input_path,
            output_path,
            quality)

    except ValueError:
        print("\nError: Quality must be between 1 and 95.")