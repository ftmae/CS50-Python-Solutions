name = input("What's your name? ")
if not name or name.isspace():
    print("Goodbye world")
else:
    print(f"Goodbye {name}")
