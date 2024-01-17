import matplotlib.pyplot as plt

month = ['March', 'April', 'May', 'June', 'July', 'August']
jeans = [1500, 3500, 6500, 6700, 6000, 6800]
tshirt = [4400, 4500, 5500, 6000, 5600, 6300]
shirt = [6500, 5000, 5800, 6300, 6200, 4500]

plt.plot(month, jeans, label="Jeans", color="red", marker="o", markerfacecolor="yellow", markersize=10, linewidth=3,
         linestyle="-")

plt.plot(month, tshirt, label="T-Shirt", color="blue", marker="o", markerfacecolor="violet", markersize=10, linewidth=3,
         linestyle="-.")

plt.plot(month, shirt, label="Shirt", color="green", marker="o", markerfacecolor="red", markersize=10, linewidth=3,
         linestyle="-.")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly garment sales")
plt.grid(True)
plt.legend()
plt.show()
