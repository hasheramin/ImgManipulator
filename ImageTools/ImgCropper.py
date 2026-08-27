from PIL import Image


def crop_image(input_path, output_path, left, top, right, bottom):

    try:
        with Image.open(input_path) as image:
            image_width, image_height = image.size

            if not (
                0 <= left < right <= image_width
                and 0 <= top < bottom <= image_height
            ):
                raise ValueError(
                    f"Crop coordinates must be within the image bounds "
                    f"(0, 0) to ({image_width}, {image_height})."
                )

            cropped_image = image.crop((left, top, right, bottom))
            cropped_image.save(output_path)

            print("\nImage cropped successfully!")
            print(f"Original Size : {image_width} x {image_height}")
            print(
                f"Crop Area     : ({left}, {top}) -> "
                f"({right}, {bottom})"
            )
            print(f"Cropped Size  : {right - left} x {bottom - top}")
            print(f"Saved To      : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Cropper")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        left = int(input("Enter left coordinate: "))
        top = int(input("Enter top coordinate: "))
        right = int(input("Enter right coordinate: "))
        bottom = int(input("Enter bottom coordinate: "))

        crop_image(
            input_path,
            output_path,
            left,
            top,
            right,
            bottom
        )

    except ValueError:
        print("\nError: Coordinates must be integers.")