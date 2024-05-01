from sys import exit,argv

def count_lines():
    try:
        count = 0
        with open(argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") or line.isspace():
                    continue
                count+=1
            return count
    except FileNotFoundError:
        exit("File does not exist")

def validate_arg():
    if len(argv) < 2:
        exit("Too few arguments")
    elif len(argv) > 2:
        exit("Too many arguments")
    elif not argv[1].endswith(".py"):
        exit("Not a Python file")


def main():
    validate_arg()
    print(count_lines())

if __name__ == "__main__":
    main()



