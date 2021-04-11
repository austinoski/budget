

class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(self, amount):
        self.amount += amount
    
    def withdraw(self, amount):
        if self.get_balance() >= amount:
            self.amount -= amount
            return amount
        else:
            raise Exception("Insufficient fund")
    
    def get_balance(self):
        return self.amount
    
    def transfer(self, budget, amount):
        self.withdraw(amount)
        budget.deposit(amount)


# instantiate budget objects
food = Budget('Food', 0)
clothing = Budget('Clothing', 0)

print('Food budget balance is %d' %food.get_balance())
print('Clothing budget balance is %d' %clothing.get_balance())

# deposit funds
food.deposit(100000)
clothing.deposit(150000)

print('Food budget balance is %d' %food.get_balance())
print('Clothing budget balance is %d' %clothing.get_balance())

# withdraw funds
food.withdraw(25000)
clothing.withdraw(55000)

print('Food budget balance is %d' %food.get_balance())
print('Clothing budget balance is %d' %clothing.get_balance())

# transfer funds
# lets instantiate a new budget object
# and transfer funds to it
entertainment = Budget('Entertainment', 0)
food.transfer(entertainment, 50000)
clothing.transfer(entertainment, 25000)

print('Food budget balance is %d' %food.get_balance())
print('Clothing budget balance is %d' %clothing.get_balance())
print('Entertainment budget balance is %d' %entertainment.get_balance())
