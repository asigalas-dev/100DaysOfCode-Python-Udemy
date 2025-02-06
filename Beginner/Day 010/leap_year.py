def is_leap_year(year):
# Write your code here.
# Don't change the function name.
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return "Leap year"
    return "Not a leap year"

year_to_check = int(input("What is the year you would like to check?: "))
print(is_leap_year(year_to_check))