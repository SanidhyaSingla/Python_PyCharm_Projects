n1 = int(input("Please enter a number 1: "))
n2 = int(input("Please enter a number 2: "))
n3 = int(input("Please enter a number 3: "))


if n1 > n2 > n3 or n1 > n3 > n2:
    print(n1, "is the largest number")

elif n2 > n1 > n3 or n2 > n3 > n1:
    print(n2, "is the largest number")

else:
    print(n3, "is the largest number")
