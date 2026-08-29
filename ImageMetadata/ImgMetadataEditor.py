from PIL import Image


def edit_metadata(input_path, output_path, title, author, description):

    try:
        with Image.open(input_path) as image:
            metadata = image.getexif()

            metadata[270] = description
            metadata[315] = author
            metadata[40092] = title

            image.save(
                output_path,
                exif=metadata
            )

            print("\nMetadata updated successfully!")
            print(f"Title       : {title}")
            print(f"Author      : {author}")
            print(f"Description : {description}")
            print(f"Saved To    : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Metadata Editor")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    description = input("Enter description: ").strip()

    edit_metadata(
        input_path,
        output_path,
        title,
        author,
        description
    )