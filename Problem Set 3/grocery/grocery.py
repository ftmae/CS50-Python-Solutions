grocery_list = {}

while True:
    try:
        grocery_item = input("").upper()
        grocery_list[grocery_item] = grocery_list.get(grocery_item,0)+1
    except EOFError:
        break

for item,count in sorted(grocery_list.items()):
    print(f"{count} {item}")

