from PIL import Image, ImageFilter


def enhance_details(input_path, output_path):

    try:
        with Image.open(input_path) as image:
            enhanced_image = image.filter(
                ImageFilter.DETAIL
            )

            enhanced_image.save(output_path)

            print("\nImage details enhanced successfully!")
            print(f"Saved To: {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Detail Enhancer")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    enhance_details(
        input_path,
        output_path
    )