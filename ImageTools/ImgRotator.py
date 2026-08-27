from PIL import Image


def rotate_image(input_path, output_path, angle):

    try:
        with Image.open(input_path) as image:
            original_size = image.size

            rotated_image = image.rotate(
                angle,
                expand=True,
                resample=Image.Resampling.BICUBIC
            )

            rotated_image.save(output_path)

            print("\nImage rotated successfully!")
            print(f"Original Size : {original_size[0]} x {original_size[1]}")
            print(f"Rotation      : {angle}°")
            print(f"New Size      : {rotated_image.size[0]} x {rotated_image.size[1]}")
            print(f"Saved To      : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("=== Image Rotator ===")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        angle = float(input("Enter rotation angle: "))

        rotate_image(
            input_path,
            output_path,
            angle
        )

    except ValueError:
        print("\nError: Rotation angle must be a number.")