

name = "YASMIN"
print(name.lower())

Name = "yasmin"
print(name.upper())

list = ["I",1, "Love", 2,"New", 3,"York",4, 5.1, "The", "End"]
list[4] = "NeW"
print(list)

list.insert(4, "City")
print(list)

list.append("Apple")
print(list)
list.append("Good")
print(list)


list.remove(1)
print(list)


list1 = ["I",1, "Love", 2,"New", 3,"York",4, 5.1, "The", "End"]
del list1[6]
print(list1)


dict = {"FirstName": "Usmon", "LastName": "Sharipov", "Age": 7, "Height": 122}
print(dict)

new_dict = {"Age": 8}
change = dict.update(new_dict)
print(dict["Age"])
New_dict = { "Height": 124}
Change = dict.update(New_dict)
print(dict["Height"])

dict.update({"Age": 8, "Height": 124})
print(dict)

Age = 25
Height = 6.1
Time = 11
if Age >= 21 and Height >= 6.0 and Time >10:
    print ("You can enter the club")
elif Age < 21 and Height >= 6.0 and Time > 10:
    print ("The time of entry and height match the entry criteria but age does not. You're not allowed to enter the club")
else:
    print("None of the requirements for entry met")


if Age >= 21 and Height < 6.0 or Time > 10:
    print("You age and time for entry match the criteria,but height does not")
if Age >= 21 and Height > 6.0 and Time > 10:
    print("You can enter the club")
elif Age >= 21 and Height > 6.0 and Time < 10:
    print("Your age and height meet the entry criteria,however you should come back when it's 10pm")
else:
    print("None of the requirements for entry are met")


if Age >= 21 and Height > 6.0 and Time < 10:
    print("Your age and height meet the entry criteria,however you should come back when it's 10pm")
elif Age >= 21 and Height < 6.0 and Time > 10:
    print ("You age and time for entry match the criteria,but height does not")
else:
    print(" None of the requirements for entry are met")

























































