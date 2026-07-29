# Write a Python program to find the factorial 
# of a given number using a while loop.

num = int(input("Enter number :- "))
start = 1

while num>0 :
    start = start*num
    num=num-1
    

print(start)