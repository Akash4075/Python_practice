class ATM:
    def __init__(self,balance):
        self.__balance=balance
        
    def deposite(self,amount):
        self.__balance+=amount
        print(f"Amount deposited : {amount}, new balance : {self.__balance}")
        
        
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"amount withdrawn : {amount}, new balance :{self.__balance}")
        else:
            print("insufficient balance")
            
            
account=ATM(1000)
account.deposite(500)
account.withdraw(200)