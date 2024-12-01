bottle="water"
#Printing
print(bottle)
print(f"Bottle contains {bottle}")

#list
name1="Binayak"
name2="Nipesh"
name3="Ram"

name=["Binayak","Nipesh","suprekshya","Anju"]
print(name[0])
print(name[-1])#-1 le last ko linxa -2 le second last ko linxa
print(name[0:3])# certain range samma print garda
print(len(name)) #calculate length of the list
name.append("prekshya")#append le array ma item add garxa(last ma)
print(name)
name.pop()
print(name)
name.insert(3,"Sujan")#insert le aafuli required thau ma item add garna milxa
print(name)
#dictionary, js ko object hoo but keys ma ni inverted comma hunchha

me={
    "name":"binayak",
    "age":22
}
me["address"]="Itahari" #dictionary ma aad garcha
print(me)
print(me["age"])
#del me['age']#deletes
print(me.keys())
print(me.values())