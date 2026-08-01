# Write a Python program to compute the factorial 
# of a given number using a recursive function.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter a number : "))

print("Factorial = " , factorial(num))