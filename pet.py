'''class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)

Raymond = Hero("Raymond",100,["Poop"])

Raymond.buy({"2024 Glasses": "Glasses", "Vision": 24})

print(Raymond.__dict__)'''

import random
Guess = random.randint(1,10)

name = input("Name Your Pet: ")

energy_types = ["High", "Low", "Sleepy"]
hungry_types = ["Stuffed","Full","Empty","Starving"]

class Pet:
    def __init__(self, name, happy, health, hunger, energy):
        self.name = name
        self.__happy = happy
        self.__health = health
        self.__hunger = hunger
        self.__energy = energy
    

    def play(self):
        asker_1 = input("Play with", name,"?").lower()
        if asker_1 == "yes":
            how = input("How Much? ")
            self.__happy += how
            print(f"{self.name} is having fun")

    def feed(self):
        asker = input("Feed Pet?").lower()
        if asker == "yes":
            user = int(input("Feed How Much?"))
            self.__hunger += user 
    
    


        
    def show_status(self):
         print(f"{self.name}'s happiness is {self.__happy}. Health is {self.__health}. Hunger is {self.__hunger}. Energy is {self.__energy}")

        
One = Pet(name, 10, 100,100,100)
One.feed()
One.show_status()


