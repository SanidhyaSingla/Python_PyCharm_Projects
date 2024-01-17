'''
import matplotlib.pyplot as mp

games = ["Pubg", "Freefire", "Minecraft", "GTA-V", "Call of duty", "FIFA 22"]
ratings = [4.5, 4.8, 4.7, 4.6, 4.1, 4.3]

mp.bar(games, ratings, color = ["black", "red", "green", "blue", "yellow"])

mp.title("Games ratings")

mp.xlabel("Games")
mp.ylabel("Ratings")

mp.legend()
mp.show()

'''

import matplotlib.pyplot as mp

games = ["Minecraft", "Freefire", "FIFA 22"]
ratings = [4.8, 4.9, 5.0]

mp.bar(games, ratings, color= ("Blue", "Green", "Red"))

mp.xlabel("Games")
mp.ylabel("Ratings")

mp.legend()
mp.show()
