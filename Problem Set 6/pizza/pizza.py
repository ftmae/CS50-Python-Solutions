import csv
from sys import argv,exit
from tabulate import tabulate

def validate_argv():
    if len(argv) < 2:
        exit("Too few command line arguments")
    elif len(argv) > 2:
        exit("Too many command line arguments")
    elif not argv[1].endswith(".csv"):
        exit("Not a csv file")

def open_menu():
    try:
        with open(argv[1]) as menu:
            return tabulate(csv.DictReader(menu), headers = "keys", tablefmt = "grid")
    except FileNotFoundError:
        exit("File does not exist")

def main():
    validate_argv()
    print(open_menu())

if __name__ == "__main__":
    main()

