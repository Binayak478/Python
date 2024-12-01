print("Welcome to love calculator!!")
name1=input("what is your name?\n")
name2=input("what is your name?\n")
first_name=name1.lower()
second_name=name2.lower()
combine=first_name+second_name
t=combine.count("t" )
r=combine.count("r")
u=combine.count("u")
e=combine.count("e")
l=combine.count("l")
o=combine.count("o")
v=combine.count("v")
e=combine.count("e")
s=str(t+u+r+e)+str(l+o+v+e)
score=int(s)
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")