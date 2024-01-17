import numpy as np

l = []

n = int(input("Enter the total number of elements: "))

for i in range(n):
    value = int(input("Please enter value " + str(i+1) + ": "))
    l.append(value)
    arrey = np.array(l)

print("Array:", arrey)

