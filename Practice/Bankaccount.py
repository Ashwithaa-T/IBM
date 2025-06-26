class bankaccount:
    def __init__(self,account_no,account_holder,balance):
        self._account_no = account_no
        self._account_holder = account_holder
        self._balance = balance

    def get_account_no(self):
        return self._account_no
    def get_account_holder(self):
        return self._account_holder
    def get_balance(self):
        return self._balance
    
    def set_account_no(self,number):
        self._account_no = number
    def set_account_holder(self,name):
        self._account_holder = name
    def set_balance(self,amount):
        self._balance = amount

    def deposit(self,amount):
        if amount<0:
            print("Cannot deposit")
        else:
            self._balance += amount
        print(self._balance)

    def withdraw(self,amount):
        if amount>0 and amount<=self._balance:
            self._balance -= amount
            print(self._balance)
        else:
            print("Enter valid amount")

    def display(self):
        print(f"Account no is {self._account_no}, Account holder is {self._account_holder},Balance is {self._balance}")

bank = bankaccount(43215677,"Radha",4000)
bank.deposit(2000)
bank.withdraw(4000)
print(bank.get_account_no())
bank.deposit(3000)
print(bank.get_balance())
bank.display()
acc1 = bankaccount(4325678,"Rajesh",9000)
print(acc1.get_account_no())
print(acc1.get_balance())
acc1.set_balance(4000)
acc1.display()
