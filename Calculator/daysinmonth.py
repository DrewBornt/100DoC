def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def days_in_month(year, month):
    """Take a month and year and determine the number of days in that year.""" # this is a docstring, what shows up when the code is moused over/typed
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month entry"
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

# Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)