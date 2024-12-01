print("Welcome to python pizza deliveries")
size=input("whats the size do you want? S,M,L ")
add_pepperoni=input("Do you want pepperoni? Y or N ")
extra_cheese=input("Do you want extra cheese? Y or N ")
ps=2
pml=3
bill=0
c=1
if size=="S":
    bill+=15
    if add_pepperoni=="Y":
     bill+=ps
elif size=="M":
    bill+= 20
    if add_pepperoni=="Y":
     bill+=pml
else:
    bill+=25
    if add_pepperoni=="Y":
     bill+=pml 

if extra_cheese=="Y":
 bill+=c
 print(bill)
          


