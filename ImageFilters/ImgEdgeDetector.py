from PIL import Image, ImageFilter


def detect_edges(input_path, output_path):
  
    try:
        with Image.open(input_path) as image:
            grayscale_image = image.convert("L")

            edge_image = grayscale_image.filter(
                ImageFilter.FIND_EDGES
            )

            edge_image.save(output_path)

            print("\nEdges detected successfully!")
            print(f"Saved To: {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Edge Detector")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    detect_edges(
        input_path,
        output_path
    )