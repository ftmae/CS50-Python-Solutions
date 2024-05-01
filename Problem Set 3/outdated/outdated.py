months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ")
            formatted_date = input_type_check(date)
            if formatted_date:
                print(formatted_date)
                break
        except ValueError:
            pass
        
def input_type_check(d):
    try:
        if "/" in d:
            return parse_date_slash(d)
        elif "," in d:
            return parse_date_comma(d)
        else:
            raise ValueError
    except ValueError:
        pass

def parse_date_slash(d):
    if len(d.split("/"))==3:
        d = d.split("/")
        month,day,year = map(int,d)
        if 1<=month<=12 and 1<=day<=31:
            return f"{year:04d}-{month:02d}-{day:02d}"

def parse_date_comma(d):
    if len(d.split(","))==2:
        d = d.split(",")
        month,day=d[0].split()
        month = months.index(month)+1
        day = int(day)
        year = int(d[1])
        if 1<=month<=12 and 1<=day<=31:
            return f"{year:04d}-{month:02d}-{day:02d}"
        return None
main()
