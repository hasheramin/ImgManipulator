from PIL import Image


def flip_image(input_path, output_path, direction):

    try:
        with Image.open(input_path) as image:

            if direction == "horizontal":
                flipped_image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

            elif direction == "vertical":
                flipped_image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

            else:
                print("\nError: Direction must be horizontal or vertical.")
                return

            flipped_image.save(output_path)

            print("\nImage flipped successfully!")
            print(f"Direction : {direction}")
            print(f"Saved To  : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Flip Tool")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    direction = input("Enter direction (horizontal/vertical): ").strip().lower()

    flip_image(
        input_path,
        output_path,
        direction)
