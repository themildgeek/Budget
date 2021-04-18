class Budget:
    def __init__ (self, category, amount):
        self.category = category 
        self.amount = amount 
    def deposit(self):
        depositamount= input ("Enter deposit amount:\n")
        depositamount = int(depositamount)
        print ("You have deposited: %d" %depositamount)
    def withdraw(self):
        withdrawamount = input ("Enter withdraw amount \n")
        withdrawamount = int(withdrawamount)
        print ("You have withdrawn: %d" %withdrawamount)
    def transfer(self):
        transferamount = input ("Enter transfer amount \n")
        transferamount = int(transferamount)
        print ("You have transferred %d" %transferamount)
    def balance(self):
        print ("This is your current Clothing balance:")
        


cat1 = Budget ("Clothing", 5000)
cat2 = Budget ("Entertainment", 3000)
cat3 = Budget ("Food", 7000)

cat1.deposit()
cat1.balance()

