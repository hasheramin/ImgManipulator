from PIL import Image, ImageStat

def analyze_brightness(input_path):

    try:
        with Image.open(input_path) as image:
            grayscale = image.convert("L")
            average_brightness = ImageStat.Stat(grayscale).mean[0]

            print("\nImage Brightness Analyzer")
            print(f"Average Brightness : {average_brightness:.2f} / 255")

            if average_brightness < 85:
                level = "Dark"
            elif average_brightness < 170:
                level = "Moderate"
            else:
                level = "Bright"

            print(f"Brightness Level   : {level}")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Brightness Analyzer")

    input_path = input("Enter image path: ").strip()

    analyze_brightness(input_path)