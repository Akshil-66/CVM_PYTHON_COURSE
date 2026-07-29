# Write a Python program to generate the 
# Fibonacci series up to n terms entered by the user.

num1 = 0
num2 = 1
count = 0

n = int(input("Enter a number :- "))
print(num1)
while count<n-1:
    num = num1+num2 
    print(num)
    num1 = num2
    num2 = num
    count+=1