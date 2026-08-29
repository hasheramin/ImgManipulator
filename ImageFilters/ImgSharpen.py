from PIL import Image, ImageFilter


def sharpen_image(input_path, output_path, radius=2, percent=150, threshold=3):

    try:
        with Image.open(input_path) as image:
            sharpened_image = image.filter(
                ImageFilter.UnsharpMask(
                    radius=radius,
                    percent=percent,
                    threshold=threshold
                )
            )

            sharpened_image.save(output_path)

            print("\nImage sharpened successfully!")
            print(f"Radius    : {radius}")
            print(f"Percent   : {percent}")
            print(f"Threshold : {threshold}")
            print(f"Saved To  : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Sharpening")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        radius = float(input("Enter radius (recommended: 1-3): "))
        percent = int(input("Enter sharpening percent (recommended: 100-200): "))
        threshold = int(input("Enter threshold (recommended: 2-5): "))

        if radius < 0:
            raise ValueError("Radius cannot be negative.")

        if percent < 0:
            raise ValueError("Percent cannot be negative.")

        if threshold < 0:
            raise ValueError("Threshold cannot be negative.")

        sharpen_image(
            input_path,
            output_path,
            radius,
            percent,
            threshold
        )

    except ValueError as error:
        print(f"\nError: {error}")