age = int(input("Please enter your age: "))

if age > 100:
    print("sorry you are dead")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40: 
    print("You are over the hill!")
elif age == 21:
    print("Congrats on being 21!")
elif age < 13:
    print("you qualify for the childrens discount")
else: 
    print("age is just a number.")
    