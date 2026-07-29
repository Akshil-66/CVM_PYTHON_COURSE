# Write a Python program to display 
# all prime numbers between two given numbers.

num1 = int(input("Enter 1st Number :- "))
num2 = int(input("Enter 2nd Number :- "))

print(f"Prime numbers between {num1} to {num2} :- ")

for num in range(num1,num2+1):
    if num>1:
        count=0
        for i in range(1,num+1):
            if num % i ==0:
                count+=1
        if count==2:
            print(num)
        

