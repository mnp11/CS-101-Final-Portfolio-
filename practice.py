import os 
import random 
import time 

animals = ["Peps", "Peanut", "Hannah", "Tommy"]
foods = ["Dry Food", "Wet Food", "Fancy Feast", "Dog Treats", "Water", "Cat Treats" ]
portions = {"Dry Food": 2, "Wet Food": 1, "Fancy Feast": 1, "Dog Treats": 3, "Cat Treats": 2}


class Diet: 
    def __init__(self, animal, food, portion): 
        self.animal = animal 
        self.food = food
        self.portion = portion
    def __str__(self): 
        return self.animal + " can eat " + self.portion + " portion(s) of " + self.food + " per day."

peps_eat = Eat("Peps", "Wet Food", portions["Wet Food"])
print(peps_eat)