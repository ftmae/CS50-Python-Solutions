from random import randint
def main():
    attempt = 0
    score = 0
    level = get_level()
    for _ in range(1, 11):
        x, y = generate_integer(level)
        while attempt < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempt += 1
                    if attempt == 3:
                        print(f"{x} + {y} = ", x + y)
            except ValueError:
                print("Please enter a valid integer.")
        attempt = 0
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            l = int(input("Level: "))
            if 1 <= l <= 3:
                return l
            else:
                print("Please enter a level between 1 and 3.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_integer(level):
    match level:
        case 1:
            return randint(0, 9), randint(0, 9)
        case 2:
            return randint(10, 99), randint(10, 99)
        case 3:
            return randint(100, 999), randint(100, 999)
if __name__ == "__main__":
    main()
