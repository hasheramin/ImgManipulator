from PIL import Image

def shear_image(input_path, output_path, shear_factor):

    try:
        with Image.open(input_path) as image:
            width, height = image.size

            offset = abs(shear_factor) * height

            new_width = int(width + offset)

            transformed_image = image.transform(
                (new_width, height),
                Image.Transform.AFFINE,
                (1, shear_factor, -offset if shear_factor < 0 else 0, 0, 1, 0),
                resample=Image.Resampling.BICUBIC)

            transformed_image.save(output_path)

            print("\nImage sheared successfully!")
            print(f"Shear Factor : {shear_factor}")
            print(f"New Size     : {new_width} x {height}")
            print(f"Saved To     : {output_path}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except ValueError:
        print("\nError: Shear factor must be a valid number.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Shear Tool")

    input_path = input("Enter image path: ").strip()
    output_path = input("Enter output image path: ").strip()

    try:
        shear_factor = float(input("Enter shear factor: "))

        shear_image(
            input_path,
            output_path,
            shear_factor)

    except ValueError:
        print("\nError: Shear factor must be a valid number.")