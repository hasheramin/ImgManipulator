from PIL import Image
from pathlib import Path


def compress_image(input_path, output_path, quality=85):

    try:
        input_path = Path(input_path)
        output_path = Path(output_path)

        if not input_path.exists():
            raise FileNotFoundError(input_path)

        if not 1 <= quality <= 100:
            raise ValueError("Quality must be between 1 and 100.")

        with Image.open(input_path) as image:
            original_size = input_path.stat().st_size

            if output_path.suffix.lower() in (".jpg", ".jpeg"):
                if image.mode in ("RGBA", "LA", "P"):
                    image = image.convert("RGB")

                image.save(
                    output_path,
                    "JPEG",
                    quality=quality,
                    optimize=True
                )

            elif output_path.suffix.lower() == ".webp":
                image.save(
                    output_path,
                    "WEBP",
                    quality=quality,
                    optimize=True
                )

            else:
                raise ValueError(
                    "Output format must be JPG, JPEG, or WEBP."
                )

            compressed_size = output_path.stat().st_size

            reduction = ((original_size - compressed_size) / original_size) * 100

            print("\nImage compressed successfully!")
            print(f"Original Size   : {original_size / 1024:.2f} KB")
            print(f"Compressed Size : {compressed_size / 1024:.2f} KB")
            print(f"Quality         : {quality}")
            print(f"Size Reduction  : {reduction:.2f}%")
            print(f"Saved To        : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Compressor")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path (.jpg, .jpeg, or .webp): ").strip()

    try:
        quality = int(input("Enter quality (1-100, recommended: 70-90): "))

        compress_image(
            input_path,
            output_path,
            quality)

    except ValueError:
        print("\nError: Quality must be an integer.")