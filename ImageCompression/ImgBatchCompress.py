from PIL import Image
from pathlib import Path


def compress_images(input_folder, output_folder, quality):

    input_dir = Path(input_folder)
    output_dir = Path(output_folder)

    try:
        if not input_dir.exists():
            raise FileNotFoundError

        output_dir.mkdir(parents=True, exist_ok=True)

        supported_formats = {".jpg", ".jpeg", ".png", ".webp"}
        processed = 0

        for image_path in input_dir.iterdir():
            if image_path.suffix.lower() not in supported_formats:
                continue

            try:
                with Image.open(image_path) as image:
                    if image.mode in ("RGBA", "P"):
                        image = image.convert("RGB")

                    output_path = output_dir / f"{image_path.stem}.jpg"

                    image.save(
                        output_path,
                        "JPEG",
                        quality=quality,
                        optimize=True)

                    processed += 1
                    print(f"Compressed: {image_path.name} -> {output_path.name}")

            except Exception as error:
                print(f"Skipped {image_path.name}: {error}")

        print(f"\nCompleted: {processed} image(s) compressed.")

    except FileNotFoundError:
        print(f"\nError: Input folder not found -> {input_folder}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nBatch Image Compressor")

    input_folder = input("Enter input folder: ").strip()
    output_folder = input("Enter output folder: ").strip()

    try:
        quality = int(input("Enter quality (1-95): "))

        if not 1 <= quality <= 95:
            raise ValueError

        compress_images(
            input_folder,
            output_folder,
            quality)

    except ValueError:
        print("\nError: Quality must be between 1 and 95.")