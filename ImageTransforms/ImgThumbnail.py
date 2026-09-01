from PIL import Image

def create_thumbnail(input_path, output_path, max_width, max_height):

    try:
        with Image.open(input_path) as image:
            original_size = image.size

            image.thumbnail((max_width, max_height))
            image.save(output_path)

            print("\nThumbnail created successfully!")
            print(f"Original Size : {original_size[0]} x {original_size[1]}")
            print(f"Thumbnail Size: {image.width} x {image.height}")
            print(f"Saved To      : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError:
        print("\nError: Width and height must be positive numbers.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Thumbnail Generator")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        max_width = int(input("Enter maximum width: "))
        max_height = int(input("Enter maximum height: "))

        if max_width <= 0 or max_height <= 0:
            raise ValueError

        create_thumbnail(
            input_path,
            output_path,
            max_width,
            max_height)

    except ValueError:
        print("\nError: Width and height must be positive integers.")