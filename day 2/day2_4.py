#if we leave till 90 than find out how many day year and month we wll leave





# till=90
# age = input("enter the age ")
# result=till-int(age)
# print("you have "+str(result))

# month = till*12
# print("you have month "+str(month))

# days = till*365
# print("you have "+str(days))



age = input("enter the age ")
age_as_int = int(age)

year_remaining = 90-age_as_int

day_remaining = year_remaining*365
week_remaining = year_remaining*52
month_remaining = year_remaining * 12

print(f"you have {month_remaining} month ,{week_remaining } weeks {day_remaining} days")