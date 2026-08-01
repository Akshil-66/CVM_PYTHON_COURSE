# Write a Python program to define a function that 
# returns the maximum and minimum values from a list.

def find_max_min(lst):
    return max(lst),min(lst)

numbers = [12,45,7,89,23]

maximum,minimum = find_max_min(numbers)

print("Maximum value :- " , maximum)
print("Minimum value :- " , minimum)

