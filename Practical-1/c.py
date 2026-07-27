# Write a Python program to convert temperature 
# from Celsius to Fahrenheit and Fahrenheit to Celsius 
# based on user choice.

print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
choice = int(input("Enter any choice :- "))

if choice==1:
    cel = float(input("Enter Celsius values :- "))
    print("Fehrenheit value is :- " , (cel*(9/5))+32)

if choice==2:
    feh = float(input("Enter Fehrenheit values :- "))
    print("Celsius value is :- " , (feh-32)*5/9)

