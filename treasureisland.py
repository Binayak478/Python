print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to treasure island.\n Your mission is to find the treasure")
first=input("You\'re at cross road.Where do you want to go.'left' or 'right'\n").lower()



if first=="right":
    second=input("You have reach the pond. Want to 'swim' or 'wait'\n").lower()
    if second=="swim":
        third=input("You are at house with three door.'Red''Blue''Yellow'. Where you want to go?\n").lower()
        if third=="blue"or third=="yellow":
            print("you are in fire")
        elif third=="yellow":
            print("Congratulations, You got the treasure")
        else:
            print(f"There is no {third} door")
    elif second=="wait":
        print("There is no boat coming. Game over")
    else:
        print(f"{second} is not an option")
elif first=="left":
    print("You have reached the jungle.failed ")
else:
    print(f"There is no road {first}")