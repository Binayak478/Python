height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
bmi=round(weight/height**2)
if bmi<18.5:
    print(f"Your bmi is {bmi}, You are under weight")
elif bmi<25:
    print(f"Your bmi is {bmi}, You have normal weight")
elif bmi<30:
    print(f"Your bmi is {bmi}, you have over weight")
elif bmi<35:
    print(f"your bmi is{bmi} and obese")
else:
    print(f"your bmi is {bmi} and clinically obese")