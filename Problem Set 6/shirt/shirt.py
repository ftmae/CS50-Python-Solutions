from PIL import Image, ImageOps
from sys import argv, exit
from os.path import splitext

def validate_len_argv():
    if len(argv) < 3:
        exit("Too few arguments")
    elif len(argv) > 3:
        exit("Too many arguments")

def validate_IO_file_name():
    for arg in argv[1:]:
        if not (arg.endswith(".png") or arg.endswith(".jpg") or arg.endswith(".jpeg")):
            exit("Not an image file")
    _1 , extension1 = splitext(argv[1])
    _2, extension2 = splitext(argv[2])
    if extension1 != extension2:
        exit("Input and output have different extensions")

#resize and crop muppet to fit shirt image
def give_tshirt():
    try:
        muppet = Image.open(argv[1])
        shirt = Image.open("shirt.png") # open given shirt image
        muppet = ImageOps.fit(muppet,shirt.size)
        muppet.paste(shirt,shirt)
        muppet.save(argv[2])
    except FileNotFoundError:
        exit("File does not exist")

def main():
    validate_len_argv()
    validate_IO_file_name()
    give_tshirt()

if __name__ == "__main__":
    main()

