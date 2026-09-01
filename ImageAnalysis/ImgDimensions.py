from PIL import Image

def analyze_dimensions(input_path):

    try:
        with Image.open(input_path) as image:
            width, height = image.size
            aspect_ratio = width / height

            print("\nImage Dimensions")
            print(f"Width        : {width} px")
            print(f"Height       : {height} px")
            print(f"Aspect Ratio : {aspect_ratio:.2f}")
            print(f"Total Pixels : {width * height:,}")
            print(f"Orientation  : ", end="")

            if width > height:
                print("Landscape")
            elif height > width:
                print("Portrait")
            else:
                print("Square")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Dimensions Analyzer")

    input_path = input("Enter image path: ").strip()

    analyze_dimensions(input_path)