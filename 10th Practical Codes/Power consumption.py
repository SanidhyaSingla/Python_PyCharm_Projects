"""
To print:
Customer number
Power consumed
Amount to be paid
"""

customer_number = int(input("Please enter customer number: "))
power = int(input("Please enter the power consumed(in units): "))
amount = 0

if power <= 100:
    amount = power

elif 100 < power <= 300:
    amount = 100 + ((power-100)*1.25)

elif 300 < power <= 500:
    amount = 350 + ((power-300)*1.50)

else:
    amount = 650 + ((power-500)*1.75)

print("Customer number: ", customer_number,"\nPower Consumed: ", power, "\nAmount to be paid", amount)
