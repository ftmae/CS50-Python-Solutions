def main():
    while True:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        if percentage is not None:
            break
    print(gauge(percentage))

def convert(fraction):
    try:
        x,y = map(int,fraction.split("/"))
        if x>y:
            raise ValueError
        if y==0:
            raise ZeroDivisionError
        return round((x/y)*100)
    except (ValueError,ZeroDivisionError):
        return None

def gauge(percentage):
    if 0<=percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
