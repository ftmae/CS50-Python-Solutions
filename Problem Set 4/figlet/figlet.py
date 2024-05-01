from random import choice
from sys import exit,argv
from pyfiglet import Figlet,FigletError

f = Figlet()
fonts = f.getFonts()

def available_fonts():
    for font in fonts:
        print(font)

def main():

    if len(argv)==1:
        use_font =  choice(fonts)
    elif len(argv)==3 and argv[1] in ['-f','--font'] and argv[2] in fonts:
        use_font = argv[2]
    else:
        exit("Invalid Number of Arguments")
    text = input("Input: ")
    try:
        print(f"Output: {Figlet(font = use_font).renderText(text)}")
    except FigletError:
        available_fonts()

if __name__ == "__main__":
    main()



