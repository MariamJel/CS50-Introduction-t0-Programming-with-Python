from PIL import Image
from PIL import ImageOps
import sys
def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguements")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguements")
        name1, ext1 = sys.argv[1].lower().split(".")
        name2, ext2 = sys.argv[2].lower().split(".")
        if ext1 != "png" and ext1 != "jpeg" and ext1 != "jpg":
            sys.exit("Invalid input")
        if ext2 != "png" and ext2 != "jpeg" and ext2 != "jpg":
            sys.exit("Invalid input")
        if ext1 != ext2:
            sys.exit("Input and output have different extensions")
        with Image.open(sys.argv[1]) as im:
            shirt= Image.open("shirt.png")
            shirt_size = shirt.size
            resized = ImageOps.fit(im, shirt_size)
            resized.paste(shirt, shirt)
            resized= resized.convert('RGB')
            resized.save(sys.argv[2])
    except (ValueError, FileNotFoundError):
        sys.exit("Invalid input")

main()
