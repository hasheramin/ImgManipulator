from PIL import Image, ImageEnhance


def enhance_image(input_path,
                  output_path,
                  grayscale=False,
                  brightness=1.0,
                  contrast=1.0):

    try:
        with Image.open(input_path) as image:
            original_mode = image.mode

            # Convert the image to grayscale if requested.
            if grayscale:
                image = image.convert("L")

            # Adjust brightness.
            if brightness != 1.0:
                brightness_enhancer = ImageEnhance.Brightness(image)
                image = brightness_enhancer.enhance(brightness)

            # Adjust contrast.
            if contrast != 1.0:
                contrast_enhancer = ImageEnhance.Contrast(image)
                image = contrast_enhancer.enhance(contrast)

            image.save(output_path)

            print("\nImage enhanced successfully!")
            print(f"Original Mode : {original_mode}")
            print(f"Grayscale     : {'Yes' if grayscale else 'No'}")
            print(f"Brightness    : {brightness}")
            print(f"Contrast      : {contrast}")
            print(f"Saved To      : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Enhancer")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    grayscale_input = input("Convert to grayscale? (y/n): ").strip().lower()
    grayscale = grayscale_input == "y"

    try:
        brightness = float(
            input("Enter brightness factor (1.0 => original): ")
        )

        contrast = float(
            input("Enter contrast factor (1.0 => original): ")
        )

        if brightness < 0 or contrast < 0:
            raise ValueError("Brightness and contrast cannot be negative.")

        enhance_image(
            input_path,
            output_path,
            grayscale,
            brightness,
            contrast
        )

    except ValueError as error:
        print(f"\nError: {error}")