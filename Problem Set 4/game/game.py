import random as r
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (level<0):raise ValueError
            return r.randrange(1,level+1)
        except ValueError:
            pass

def guessing_game():
    generated = get_level()
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == generated:
                print("Just right!")
                break
            elif guess > generated:
                print("Too large!")
            elif guess < generated:
                print("Too small!")
            else:
                raise ValueError
        except ValueError:
            pass

def main():
    guessing_game()

if __name__ == "__main__":
    main()

