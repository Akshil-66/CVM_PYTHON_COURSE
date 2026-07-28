# Write a Python program to find the largest of 
# three numbers entered by the user using 
# nested if - else statements.

num1 = float(input("Enter 1st Number :- "))
num2 = float(input("Enter 2nd Number :- "))
num3 = float(input("Enter 3rd Number :- "))

if num2 > num3 :

    if num2 > num1:
        print("Number 2 is Biggest")

    elif num3 < num1:
        print("Number 1 is Biggest")

else :
        print("Number 3 is Biggest") 
