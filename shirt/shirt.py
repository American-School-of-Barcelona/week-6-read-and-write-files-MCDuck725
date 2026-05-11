import sys
import os
from PIL import Image, ImageOps

def main():
    # 1. Validate Command-Line Arguments
    check_arguments()

    try:
        # 2. Open the shirt overlay
        shirt = Image.open("shirt.png")
        # Get the size of the shirt to resize the input image later
        size = shirt.size

        # 3. Open the input image
        with Image.open(sys.argv[1]) as input_img:
            # 4. Resize and crop the input to match the shirt's dimensions
            # ImageOps.fit handles the cropping and resizing automatically
            photo = ImageOps.fit(input_img, size)

            # 5. Overlay the shirt (it has a transparent background)
            # The second 'shirt' argument acts as a mask for transparency
            photo.paste(shirt, shirt)

            # 6. Save the final result
            photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_arguments():
    """Validates the count and format of command-line arguments."""
    # Check count
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check extensions
    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(sys.argv[1].lower())[1]
    output_ext = os.path.splitext(sys.argv[2].lower())[1]

    if output_ext not in valid_extensions:
        sys.exit("Invalid output")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()