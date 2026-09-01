from PIL import Image

def analyze_histogram(input_path):

    try:
        with Image.open(input_path) as image:
            image = image.convert("RGB")
            histogram = image.histogram()

            red = histogram[0:256]
            green = histogram[256:512]
            blue = histogram[512:768]

            print("\nImage Histogram")
            print(f"Image Size: {image.width} x {image.height}")

            print("\nRed Channel:")
            print(f"Minimum Frequency : {min(red)}")
            print(f"Maximum Frequency : {max(red)}")

            print("Green Channel:")
            print(f"Minimum Frequency : {min(green)}")
            print(f"Maximum Frequency : {max(green)}")

            print("Blue Channel:")
            print(f"Minimum Frequency : {min(blue)}")
            print(f"Maximum Frequency : {max(blue)}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Histogram Analyzer")

    input_path = input("Enter image path: ").strip()

    analyze_histogram(input_path)