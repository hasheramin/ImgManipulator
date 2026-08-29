from PIL import Image


def get_image_info(input_path):

    try:
        with Image.open(input_path) as image:
            print("\nImage Information")
            print(f"Format      : {image.format}")
            print(f"Mode        : {image.mode}")
            print(f"Width       : {image.width}")
            print(f"Height      : {image.height}")
            print(f"Resolution  : {image.size}")

            if image.info:
                print("\nAdditional Information:")
                for key, value in image.info.items():
                    print(f"{key}: {value}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Information Tool")

    input_path = input("Enter image path: ").strip()

    get_image_info(input_path)