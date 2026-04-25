class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)

Raymond = Hero("Raymond",100,["Poop"])

Raymond.buy({"2024 Glasses": "Glasses", "Vision": 24})

print(Raymond.__dict__)

import random
Guess = random.randint(1,10)


class Pet:
    def __init__(self, name, happy):
        self.name = name
        self.__happy = happy
    def play(self):
        self.__happy += Guess
        print(f"{self.name} is having fun")

    def show_status(self):
         print(f"{self.name}'s happiness is {self.__happy}")
        
One = Pet("Jayden", 10)
One.play()
One.show_status()




