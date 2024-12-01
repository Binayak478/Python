import random

test_seed=int(input("create s seed number"))
random.seed(test_seed)
nameAsCSV=input("give me everybody's names,seperated by a comma. ")
names=nameAsCSV.split(", ")
#name=random.choice(names)
name=len(names)
choice=()
print(name)