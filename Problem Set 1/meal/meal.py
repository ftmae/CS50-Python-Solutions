from sys import exit
def main():
    input_time = input("What is the time? ")
    if valid_time(input_time):
        time = convert(input_time)
        meal_time_check(time)
    else:
        print("Invalid time format input")

def convert(time):
    hours, minutes = split_input(time)
    return (hours+(minutes/60))

def meal_time_check(time):
    if 7<=time<=8:
        print("Breakfast Time")
    elif 12<=time<=13:
        print("Lunch Time")
    elif 18<=time<=19:
        print("Dinner Time")
    else:
        print("Not a meal time")

def valid_time(time):
    hours, minutes = split_input(time)
    return 0<=hours<24 and 0<=minutes<60

def split_input(userInput):
    try:
        h, m = userInput.split(":")
        hours = float(h)
        minutes = float(m)
        return hours, minutes
    except ValueError:
        exit("Couldn't process time input")

if __name__ == "__main__":
    main()
