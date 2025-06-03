class atm:
    def _init__(self):
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        print("balance2")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("balance")
        else:
            print("insufficient funds")
    def check_balance(self):
        print("selfbalance")
ATM = atm()
while True:
    print("1.deposit")
    print("2.withdraw")
    print("3.checkbalance")
    print("4.exit")
    choice = input("choose option:")
    if choice == "1":
        atm.deposit(float(input("enter balance:")))
    elif choice =="2":
        atm.withdraw(float(input("enter balance:")))
    elif choice =="3":
        atm.check_balance()
    elif choice == "4":
        atm.exit()



        

    
    
    
    
                
            