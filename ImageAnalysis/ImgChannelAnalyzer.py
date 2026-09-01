from PIL import Image

def analyze_channels(input_path):

    try:
        with Image.open(input_path) as image:
            print("\nImage Channel Analyzer")
            print(f"Mode     : {image.mode}")
            print(f"Channels : {len(image.getbands())}")
            print(f"Names    : {', '.join(image.getbands())}")

            if image.mode == "RGB":
                print("\nRed, Green, and Blue channels detected.")

            elif image.mode == "RGBA":
                print("\nRed, Green, Blue, and Alpha channels detected.")

            elif image.mode == "L":
                print("\nGrayscale channel detected.")

            else:
                print("\nAdditional or specialized channels detected.")

    except FileNotFoundError:
        print(f"\nError: Image not found -> {input_path}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage Channel Analyzer")

    input_path = input("Enter image path: ").strip()

    analyze_channels(input_path)