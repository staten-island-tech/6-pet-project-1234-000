import random


class Pet:
     def __init__(self, name, happy, health, hunger, energy):
        self.name = name
        self.__happy = happy
        self.__health = health
        self.__hunger = hunger
        self.__energy = energy
     
     def play(self):
          Guess = random.randint(1,10)
          if self.__energy < 20:
            print(f"---{self.name} is too tired to play.---")
            return # If true, stops the rest from running
          self.__happy += Guess
          self.__energy -= 20
          print(f"---{self.name} had fun!---")

     def feed(self):
            user = int(input("---Feed How Much?---"))
            self.__hunger += user 
            self.__happy += 10
    
     def sleep(self):
         self.__energy += 30
         self.__happy += 5
         print(f"---{self.name} woke up feeling nice---")
    
     def show_status(self):
         print(f"---{name}'s stats:---")
         print(f"Happy: {self.__happy}")
         print(f"Energy:: {self.__energy}")
         print(f"Hunger: {self.__hunger}")
         print(f"Health: {self.__health}")
    
     def days(self):
         self.__hunger -= 5
         self.__energy -= 5
         self.__happy -= 5
         if self.__hunger <= 0:
            self.__health += 20
            print(f"{self.__name} is feeling fat")
         if self.__hunger > 100:
              self.__health -= 10
              self.__happy += 5
              print(f"{self.__name} loves being stuffed but is feeling sick")
         self.__happy = max(0, min(100, self.__happy))
         self.__energy = max(0, min(100, self.__energy))
         self.__health = max(0, min(100, self.__health))
         self.__hunger = max(0, min(100, self.__hunger))
        
     def checker(self):
          return self.__health > 0
     def health_c(self):
          if self.__health < 0:
              return False
          else:
              return True
     def goodbye(self):
         return self.__health == 0
    
    
name = input("Name Your Pet: ")
pet = Pet(name, happy = random.randint(50,100), hunger = random.randint(20,100), health = random.randint(10,100), energy = random.randint(60,100))

if pet.health_c() < 50:
     print(f"{name} is frail lol")
else:
     print(f"{name} is strong. Take care!")

while pet.health_c() == True:
     print("What Would You Like To Do?")
     print("Play")
     print("Sleep")
     print("Feed")
     print("Kill")
     asker = input("---What Would You Like To Do?--- ").lower()

     if asker == "play":
         pet.play()



     
     