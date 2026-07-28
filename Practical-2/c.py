# Write a Python program to calculate 
# the grade of a student based on marks entered by the user.

mark = float(input("Enter your mark :- "))

if 90 <= mark <=100 :
    print("O Grade")
elif 80 <= mark < 90 :
    print("A+ Grade")
elif 70 <= mark < 80 :
    print("A Grade")
elif 60 <= mark <70 :
    print("B+ Grade")
elif 50 <= mark < 60 :
    print("B Grade")
elif 40 <= mark < 50 :
    print("C Grade")
else :
    print("Fail")
