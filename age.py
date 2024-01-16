from datetime import datetime
def calc_age():
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    birthday=input("Please enter your birthday in dd/mm/yyyy format: ")
    birthday = birthday.split("/")
    birth_day = int(birthday[0])
    birth_month = int(birthday[1])
    birth_year = int(birthday[2])
 
    approx_age = year - birth_year
    if month == birth_month:
        if day < birth_day:
            print(f"Your age is {approx_age-1} years")
        else:
            print(f"Your age is {approx_age} years")
    elif month < birth_month:
        print(print(f"Your age is {approx_age-1} years"))
    else:
        print(f"Your age is {approx_age} years")
calc_age()