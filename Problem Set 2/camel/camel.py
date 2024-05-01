def main():
    camel = input("camelCase:  ")
    print("snake_case: "+snake_case(camel))

def snake_case(camel):
    snake = ""
    for _ in camel:
        if _.isupper():
            _ = "_" + f"{_.lower()}"
        snake = snake + _
    return snake
main()
