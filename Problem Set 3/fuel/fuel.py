def get_fraction():
    while True:
        try:
            x,y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if x>y:
                raise ValueError
            elif y==0:
                raise ZeroDivisionError
            return x/y
        except(ZeroDivisionError, ValueError):
            pass

def meter_output(fuel_percentage):
    if fuel_percentage<=1:
        return "E"
    elif fuel_percentage>=99:
        return "F"
    elif 1<fuel_percentage<99:
        return f"{fuel_percentage}%"

def main():
    fuel_percentage = round(get_fraction()*100)
    print(meter_output(fuel_percentage))

main()
