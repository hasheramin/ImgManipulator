from pathlib import Path


def analyze_file_size(input_path):

    try:
        image_path = Path(input_path)

        if not image_path.exists():
            raise FileNotFoundError(input_path)

        if not image_path.is_file():
            raise ValueError("The provided path is not a file.")

        file_size = image_path.stat().st_size

        print("\nImage File Size")
        print(f"File       : {image_path.name}")
        print(f"Size       : {file_size / 1024:.2f} KB")
        print(f"Size       : {file_size / (1024 * 1024):.2f} MB")

    except FileNotFoundError:
        print(f"\nError: File not found -> {input_path}")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    print("\nImage File Size Analyzer")

    input_path = input("Enter image path: ").strip()

    analyze_file_size(input_path)