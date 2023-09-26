import datetime

def friday(month, year):
    date=datetime.date(year,month,13)
    return date.weekday()==4
try:
    month =int(input("Enter a month: "))
    year = int(input("Enter a year: "))
    
    if month <1 or month >12:
        print("Invalid month")
    elif year <1000 or year >9999:
        print("Invalid year")
    else:
        if friday(month,year):
            print(f"13th of {datetime.date(year,month,1).strftime('%B')} {year} is a Friday.")
        else:
            print(f"13th of {datetime.date(year,month,1).strftime('%B')} {year} is NOT a Friday.")
except ValueError:
    print("Invalid Inputs")