from PIL import Image
from PIL.ExifTags import TAGS


def read_exif(input_path):

    try:
        with Image.open(input_path) as image:
            exif_data = image.getexif()

            if not exif_data:
                print("\nNo EXIF metadata found.")
                return

            print("\nEXIF Metadata")

            for tag_id, value in exif_data.items():
                tag_name = TAGS.get(tag_id, tag_id)
                print(f"{tag_name}: {value}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nEXIF Metadata Reader")

    input_path = input("Enter image path: ").strip()

    read_exif(input_path)