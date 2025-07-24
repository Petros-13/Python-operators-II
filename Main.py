x=5
y=9
if x>2 and y==10:
    print("The number is beetween 3-10")
elif x==5 and y<10:
    print("The number is beetween 5-9")
elif x==7 and y<8:
    print("The number is 7")
else:
    print(" The number is above 11")

name=input("Enter my name")
contry=input("Enter my contry")
if (name=="Petros" or contry=="Greece"):
    print("You guessed it right!")
elif (name=="Petros" or contry=="Serbia"):
    print("The name is correct but the contry is incorrect")
elif (name=="Mike" or contry=="Greece"):
    print("The name is incorrect but the contry is correct")
else:
    print("Try again")