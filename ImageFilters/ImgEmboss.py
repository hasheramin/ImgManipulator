from PIL import Image, ImageFilter


def emboss_image(input_path, output_path):

    try:
        with Image.open(input_path) as image:
            embossed_image = image.filter(
                ImageFilter.EMBOSS
            )

            embossed_image.save(output_path)

            print("\nEmboss effect applied successfully!")
            print(f"Saved To: {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Emboss Effect")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    emboss_image(
        input_path,
        output_path
    )