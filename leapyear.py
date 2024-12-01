year=int(input("which year you want to check "))
if year%4!=0:
    print("not leap 1")
else:
 if year%100!=0:
    print("leap 1")
 else:
    if year%400==0:
        print("leap 2")
    else:
        print("not leap 2")