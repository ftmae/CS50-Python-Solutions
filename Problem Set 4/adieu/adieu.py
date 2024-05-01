from inflect import engine

def is_empty(input):
    for _ in input:
        if _ == " ":
            return True

p = engine()
names = []
while True:
    try:
        name = input("Name: ")
        if not name or is_empty(name):
            raise ValueError
        else:
            names.append(name)
    except EOFError:
        break
    except ValueError:
        print("Invalid Input")


print(f"\nAdieu, adieu, to {p.join(names)}")
