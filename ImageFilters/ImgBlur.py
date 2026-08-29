from PIL import Image, ImageFilter


def blur_image(input_path, output_path, radius):

    try:
        with Image.open(input_path) as image:
            blurred_image = image.filter(
                ImageFilter.GaussianBlur(radius)
            )

            blurred_image.save(output_path)

            print("\nImage blurred successfully!")
            print(f"Blur Radius : {radius}")
            print(f"Saved To    : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Blur")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        radius = float(input("Enter blur radius (recommended: 1-10): "))

        if radius < 0:
            raise ValueError("Blur radius cannot be negative.")

        blur_image(
            input_path,
            output_path,
            radius
        )

    except ValueError as error:
        print(f"\nError: {error}")