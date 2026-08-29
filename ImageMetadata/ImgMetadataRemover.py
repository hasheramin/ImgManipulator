from PIL import Image


def remove_metadata(input_path, output_path):

    try:
        with Image.open(input_path) as image:
            clean_image = Image.new(image.mode, image.size)
            clean_image.putdata(list(image.getdata()))

            clean_image.save(output_path)

            print("\nMetadata removed successfully!")
            print(f"Saved To: {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Metadata Remover")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    remove_metadata(
        input_path,
        output_path
    )