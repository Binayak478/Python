#tuple
name=("bainayak","Bikash")
#name.append("nipesh")

#list-->[],  dictionary-->{}, tuple-->(), ser-->{} without key

# firstName-->camel case
# first_name-->snake
# FIRSTNAME-->pascle
# first-name->kabab

#set

my_name={"binayak","binayak","dhungana"}
print(my_name)

#conditional

is_raining=True
if is_raining:
    print("Carry  umbrella")
else:
    print("Dont carry umbrella")



#for loop

days=["Sunday","monday","Tuuesday"]
for d in days:
    print(d)

fruits=("apple","banana","mango")
for f in fruits:
    print(f)

def sayHello(days):
    print(f"Hello {days}")

sayHello(days)