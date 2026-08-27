from PIL import Image
from pathlib import Path


SUPPORTED_FORMATS = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "webp": "WEBP",
    "bmp": "BMP",
    "tiff": "TIFF",}


def convert_image(input_path, output_path):

    try:
        input_path = Path(input_path)
        output_path = Path(output_path)

        if not input_path.exists():
            raise FileNotFoundError(input_path)

        output_format = output_path.suffix.lower().lstrip(".")

        if output_format not in SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported output format: {output_format}. "
                f"Supported formats: {', '.join(SUPPORTED_FORMATS)}"
            )

        with Image.open(input_path) as image:
            original_format = image.format

            # JPEG does not support transparency.
            if SUPPORTED_FORMATS[output_format] == "JPEG" and image.mode in (
                "RGBA",
                "LA",
                "P",
            ):
                image = image.convert("RGB")

            image.save(
                output_path,
                format=SUPPORTED_FORMATS[output_format]
            )

            print("\nImage converted successfully!")
            print(f"Original Format : {original_format}")
            print(f"New Format      : {SUPPORTED_FORMATS[output_format]}")
            print(f"Saved To        : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")



if __name__ == "__main__":
    print("\nImage Format Converter")

    input_path = input("Enter image path: ").strip()
    output_path = input(
        "Enter output image path with extension: "
    ).strip()

    convert_image(input_path, output_path)