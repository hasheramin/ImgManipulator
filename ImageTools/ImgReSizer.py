from PIL import Image

def resize_image(input_path, output_path, width, height):

    try:
        with Image.open(input_path) as image:
            original_size = image.size

            resized_image = image.resize(
                (width, height),
                Image.Resampling.LANCZOS
            )

            resized_image.save(output_path)

            print("\nImage resized successfully!")
            print(f"Original Size : {original_size[0]} x {original_size[1]}")
            print(f"New Size      : {width} x {height}")
            print(f"Saved To      : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError:
        print("\nError: Width and height must be positive integers.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Resizer")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))

        if width <= 0 or height <= 0:
            raise ValueError

        resize_image(input_path, output_path, width, height)

    except ValueError:
        print("\nError: Width and height must be positive integers.")