def is_leap_year(year):
    # Leap year is divisible by 4
    # Exception: Years divisible by 100 are not leap years, unless they are also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year_to_check = int(input("Enter a year to check: "))
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
