import string
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if 2<=len(plate)<=6:
        if not plate[0:1].isalpha():
            return False
        for i in range(2,len(plate)-1):
            if plate[i] in string.punctuation:
                return False
            if plate[i].isdigit() and plate[i+1].isalpha():
                return False
            if plate[i:].isdigit() and plate[i].startswith("0"):
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()
