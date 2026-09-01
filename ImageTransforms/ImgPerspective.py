from PIL import Image

def perspective_transform(input_path, output_path, points):

    try:
        with Image.open(input_path) as image:
            width, height = image.size

            source_points = [(0, 0), (width, 0), (width, height), (0, height)]

            destination_points = [(points[0], points[1]),
                                  (points[2], points[3]),
                                  (points[4], points[5]),
                                  (points[6], points[7])]

            transformed_image = image.transform(
                image.size,
                Image.Transform.QUAD,
                destination_points)

            transformed_image.save(output_path)

            print("\nPerspective transformation applied successfully!")
            print(f"Saved To: {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Perspective Transform")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    print("\nEnter four destination points.")
    print("Format: x y")

    points = []

    for index in range(4):
        x, y = map(
            int,
            input(f"Point {index + 1}: ").split()
        )
        points.extend([x, y])

    perspective_transform(
        input_path,
        output_path,
        points)
