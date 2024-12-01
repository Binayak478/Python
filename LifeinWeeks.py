age=input("What is your age? ")
remaining=input("How many year do you think you live? ")
year=int(remaining)
days=year*365
weeks=year*52
months=year*12
current_age=int(age)
days_remaining=days-current_age*365
weeks_remaining=weeks-current_age*52
months_remaining=months-current_age*12
week=round(weeks_remaining)
month=round(months_remaining)
print(f"You have {days_remaining}, {week} Weeks, {month} months left.")
