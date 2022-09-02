# Lab task 2:
month_31 =['January','March', 'May', 'July', 'August', 'October', 'December']
month_30 =['April', 'June', 'September', 'November']
month_28_29 =['February']

birth_month= input("What is your birth month? ")
if birth_month in month_31:
    print("There are 31 days in",birth_month)
elif birth_month in month_30:
    print("There are 30 days in",birth_month)
elif birth_month in month_28_29:
    print("There are 28 days in",birth_month+", or 29 days on leap year")

# Originally I wrote this code using the 'or' operator, but it looked far too long and messy.
# After some research I discovered I could use a 'list' function and the 'in' operator
# to make it shorter and more comprehensive.
