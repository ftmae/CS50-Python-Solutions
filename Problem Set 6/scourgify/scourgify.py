import csv
from sys import argv, exit

# take before file
# split name string into first and last
# write this new format into after

def validate_argv():
    if len(argv) > 3:
        exit("Too many arguments")
    elif len(argv) < 3:
        exit("Too few arguments")
    elif not argv[1].endswith(".csv"):
        exit("Not a CSV file")

def scourgify():
    try:
        with open(argv[1]) as before:
            reader = csv.DictReader(before)
            with open(argv[2], "w") as after:
                writer = csv.DictWriter(after, fieldnames = ['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    last, first = row['name'].split(",")
                    writer.writerow({'first':first.strip() , 'last': last.strip(), 'house': row['house'].strip()})
    except FileNotFoundError:
        exit("File does not exist")
def main():
    validate_argv()
    scourgify()
if __name__ == "__main__":
    main()
