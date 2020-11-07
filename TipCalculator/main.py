# number = input("Enter a two digit numer. \n")

# first_digit = int(number[0])
# second_digit = int(number[1])

# total = first_digit+second_digit

# print("The total is: " + str(total))

# height = input("Enter your height in m: ")

# weight = input("Enter your weight in kg: ")

# BMI = int(weight) / float(height)**2
# print (int(BMI))

# age = int(input("What is your current age in years?  "))

# weeksLived = age * 52
# daysLived = age * 365
# monthsLived = age * 12

# TOTAL_WEEKS = 100*52
# TOTAL_DAYS = 100*365
# TOTAL_MONTHS = 100*12

# weeksLeft = TOTAL_WEEKS - weeksLived
# daysLeft = TOTAL_DAYS - daysLived
# monthsLeft = TOTAL_MONTHS - monthsLived

# print(f"You have {weeksLeft} weeks left, {daysLeft} days left, and {monthsLeft} months left")

print("Welcome to the Bill & Tip Calculator\n")

billTotal = float(input("What is the bill total? $"))

split = int(input("How many people are splitting the bill? "))

tip = int(input("What percentage tip do you want to give? "))

tipPercent = tip/100

totalTip = billTotal * tipPercent

totalBill = billTotal + totalTip

splitBill = round(totalBill/split, 2)

print(f"\nEach person should pay ${splitBill}.")

