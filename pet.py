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
