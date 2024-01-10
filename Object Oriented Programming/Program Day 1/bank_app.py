# write a program to create a bank application with static, non static and local variables, Constructor and non static method
# conndition
#     1. before withdraw if the bal is < 2000 don't perform the transaction
#     2. befor withdraw check the balance properly(sufficient funds are available or not)
class Customer:
    bank_name = "Bank of India"
    def __init__(self,name,accno,add,bal):
        self.bal = bal
        self.name = name
        self.accno = accno
        self.add = add
    
    def display(self):
        print(Customer.bank_name)
        print(self.name)
        print(self.accno)
        print(self.add)
    
    def self_bal(self):
        print("Balance:",self.bal)
    
    def deposit(self,amt):
        self.bal += amt
        print("Balance after Deposit:",self.bal)
    
    def withdraw(self, amt):
        if(amt < self.bal):
            if self.bal - amt>=2000:
                self.bal = self.bal - amt
                print("Balance after Withdrawl:",self.bal)
            else:
                print("Maintain minimum balance.")
        else:
            print("Insufficient Balance.")

cust1 = Customer("Rohit",101,"Nagpur",5000)
cust1.display()
cust1.self_bal()
cust1.deposit(5000)
cust1.withdraw(6000)



# o/p:
# Bank of India
# Rohit
# 101
# Nagpur
# Balance: 5000
# Balance after Deposit: 10000
# Balance after Withdrawl: 4000