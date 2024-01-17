'''
n = int(input("Please enter a number to check: "))

for i in range(1, n):

    if n % i == 0:
        print(i)
        print("The number entered is not a prime number")

    else:
        print("The number entered is a prime number")
'''

'''
num = int(input("Enter a number: "))

if num > 1:
    if num == 2:
        print(num, "is a prime number")

    if num == 3:
        print(num, "is a prime number")

    for i in range(2, num-1):
        if (num % 2 or 3 == 0):
            print('hi')
            print(num, "is not a prime number")
            break

        else:
            print(num, "is a prime number")
            break
'''

num = int(input("Please enter a number: "))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num / 2) + 1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
