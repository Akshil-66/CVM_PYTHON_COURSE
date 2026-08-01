# Write a Python program to define a function that 
# calculates simple interest using parameters and return values.

def simple_interest(p,r,t):
    si = (p*r*t)/100
    return si

p = float(input("Enter Principal Amount :- " ))
r = float(input("Enter Rate of Interest :- "))
t = float(input("Enter Time (in years) :- "))

print("Simple Interest = " , simple_interest(p,r,t) )