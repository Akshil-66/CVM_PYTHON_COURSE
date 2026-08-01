# Write a Python program to define a function 
# that checks whether a number is a palindrome.

def palindrome(num):
    temp = num
    rev = 0

    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10

    if temp==rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

n = int(input("Enter a number : "))
palindrome(n)