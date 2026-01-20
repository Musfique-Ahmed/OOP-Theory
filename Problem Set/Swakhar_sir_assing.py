class SavingsAccount:
    """This is the Parent class of this program."""
    def __init__(self, account_no):
        """Initialize attributes.
            The initial balance is 1000 taka when an account is opened."""
        self.account_no = account_no
        self.balance = 1000
        self.withdrawals = 0

    def withdraw(self, amount):
        """
        1. Checks if more than 3 times of withdrawals have been done this month.
        2. If [1] is true then an additional 10 taka fee will be charged.
        3. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        4. If [3] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if (self.withdrawals >= 3):
            if ((self.balance - amount) >= 1010):
                self.withdrawals += 1
                self.balance -= (amount + 10 )
                print(f"An additional 10 taka has been charged as this is \nyour {self.withdrawals}th withdraw this month!")
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!")
        else:
            if ((self.balance - amount) >= 1000):
                self.withdrawals += 1
                self.balance -= amount
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!!!")
    
    def deposite(self, amount):
        """Deposits the required amount to the account and incriment the balance."""
        self.balance += amount
        print(f"[{amount} taka] has been deposited to [Account no:{self.account_no}]")

    def profit(self):
        """ 5% per year profit!
            [Profit = Deposit x Interest Rate x Time]
            Interest Rate = 5%
            Time = 1 year """
        profit = self.balance * 0.05 * 1
        self.balance += profit
        return f"Your profit for this year is {profit}"

    def reset_withdrawals(self):
        """Resets withdrwals attributes every month."""
        self.withdrawals = 0

    def __str__(self):
        return f"Account No: {self.account_no} \nBalance: {self.balance}"


class CurrentAccount(SavingsAccount):
    """This is the Child class of (SavingsAccount) class."""
    def __init__(self, account_no):
        """Calls the super().__init__ function to get access to all the methods and attributes of the parent class"""
        super().__init__(account_no)

    def withdraw(self, amount):
        """
        ## This method overrid the method form the parent class ##
        1. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        2. If [1] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if ((self.balance - amount) >= 1000):
            self.balance -= amount
        else:
            print(f"Transaction failed!!! You don't have sufficient balance!!!")

    def profit(self):
        """ 
        ## This method overrid the method form the parent class ##
        3% per year profit!
        [Profit = Deposit x Interest Rate x Time]
        Interest Rate = 5%
        Time = 1 year
        """
        profit = self.balance * 0.03 * 1
        self.balance += profit
        return f"Your profit for this year is {profit}"
    
"""
Here - the SavingsAccount class is the parent class and
the CurrentAccount class is the child class.
The withdraw and profit methods will overrid the parent class
methods and will be used from the child class if called by the
intences of the child class.
"""


account_1 = SavingsAccount("0152330101")
print(account_1)
# account_1.deposite(50000)
# print(account_1)
# account_1.withdraw(10000)
# print(account_1)
# account_1.withdraw(10000)
# print(account_1)
# account_1.withdraw(10000)
# print(account_1)
# account_1.withdraw(10000)
# print(account_1)
# account_1.withdraw(5000)
# print(account_1)
# account_1.withdraw(5000)
# print(account_1)
# print(account_1.profit())
# print(account_1)
# account_1.withdraw(5000)
# print(account_1)
# account_1.deposite(10000)
# print(account_1)
# account_1.reset_withdrawals()
# account_1.withdraw(5000)
# print(account_1)


# print("\n2nd Account:=>\n")
# account_2 = CurrentAccount("0152330116")
# print(account_2)
# account_2.deposite(100000)
# print(account_2)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# print(account_2)
# print(account_2.profit())
# print(account_2)







## Using Name mangling (Not Pythonic) to creat privacy layer for the balance attribute.
"""
=> To creat a privacy layer for an attribute (private attribute) we use double underscore infront of the attribute name.

=> To access a private attribute of a parent class from a child class in Python, you can follow these approaches:

Name Mangling (Not Recommended):
->Python uses name mangling to make private attributes more difficult to access from outside the class.
->You can access the parent’s private attribute by explicitly using the mangled form of its name in the child class.
->However, this approach is not recommended because it breaks encapsulation and makes the code less readable.

Here, (self._SavingsAccount__balance) is an example of name mangling.
"""

class SavingsAccount:
    """This is the Parent class of this program."""
    def __init__(self, account_no, pin):
        """Initialize attributes.
            The initial balance is 1000 taka when an account is opened."""
        self.account_no = account_no
        self.password = pin
        self.__balance = 1000
        self.withdrawals = 0

    def withdraw(self, amount):
        """
        1. Checks if more than 3 times of withdrawals have been done this month.
        2. If [1] is true then an additional 10 taka fee will be charged.
        3. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        4. If [3] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if (self.withdrawals >= 3):
            if ((self.__balance - amount) >= 1010):
                self.withdrawals += 1
                self.__balance -= (amount + 10 )
                print(f"An additional 10 taka has been charged as this is \nyour {self.withdrawals}th withdraw this month!")
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!")
        else:
            if ((self.__balance - amount) >= 1000):
                self.withdrawals += 1
                self.__balance -= amount
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!!!")
    
    def deposite(self, amount):
        """Deposits the required amount to the account and incriment the balance."""
        self.__balance += amount
        print(f"[{amount} taka] has been deposited to [Account no:{self.account_no}]")

    def profit(self):
        """ 5% per year profit!
            [Profit = Deposit x Interest Rate x Time]
            Interest Rate = 5%
            Time = 1 year """
        profit = self.__balance * 0.05 * 1
        self.__balance += profit
        return f"Your profit for this year is {profit}"

    def reset_withdrawals(self):
        """Resets withdrwals attributes every month."""
        self.withdrawals = 0

    def checkbalance(self):
        """Checks if the account no and the pin no matches or not before revealing the balance."""
        account = input("Enter Account No: ")
        password = int(input("Enter Pin No: "))
        if (account == self.account_no) and (password == self.password):
            return self.__balance
        else:
            print("Your Account No and Pin didn't match!!!")



class CurrentAccount(SavingsAccount):
    """This is the Child class of (SavingsAccount) class."""
    def __init__(self, account_no, pin):
        """Calls the super().__init__ function to get access to all the methods and attributes of the parent class"""
        super().__init__(account_no, pin)

    def withdraw(self, amount):
        """
        ## This method overrid the method form the parent class ##
        1. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        2. If [1] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if ((self._SavingsAccount__balance - amount) >= 1000):
            self._SavingsAccount__balance -= amount
        else:
            print(f"Transaction failed!!! You don't have sufficient balance!!!")

    def profit(self):
        """ 
        ## This method overrid the method form the parent class ##
        3% per year profit!
        [Profit = Deposit x Interest Rate x Time]
        Interest Rate = 5%
        Time = 1 year
        """
        profit = self._SavingsAccount__balance * 0.03 * 1
        self._SavingsAccount__balance += profit
        return f"Your profit for this year is {profit}"









### Final Code:=>

## Using Single Underscore (Recommended) to creat privacy layer for the balance attribute.
"""
=> To creat a privacy layer for an attribute (private attribute) we use double underscore infront of the attribute name.

=> To access a private attribute of a parent class from a child class in Python, you can follow these approaches:

Single Underscore (Recommended):
->Instead of using double underscores for private attributes, use a single underscore (e.g., _field).
->This convention indicates that the attribute is intended to be private, without enabling name mangling.
->It’s a cleaner and more Pythonic way to achieve encapsulation.

Here, (self._balance) is an example of name mangling.
"""

class SavingsAccount:
    """This is the Parent class of this program."""
    def __init__(self, account_no, pin):
        """Initialize attributes.
            The initial balance is 1000 taka when an account is opened."""
        self.account_no = account_no
        self.password = pin
        self._balance = 1000
        self.withdrawals = 0
 
    def withdraw(self, amount):
        """
        1. Checks if more than 3 times of withdrawals have been done this month.
        2. If [1] is true then an additional 10 taka fee will be charged.
        3. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        4. If [3] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if (self.withdrawals >= 3):
            if ((self._balance - amount) >= 1010):
                self.withdrawals += 1
                self._balance -= (amount + 10 )
                print(f"An additional 10 taka has been charged as this is \nyour {self.withdrawals}th withdraw this month!")
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!")
        else:
            if ((self._balance - amount) >= 1000):
                self.withdrawals += 1
                self._balance -= amount
            else:
                print(f"Transaction failed!!! You don't have sufficient balance!!!")
    
    def deposite(self, amount):
        """Deposits the required amount to the account and incriment the balance."""
        self._balance += amount
        print(f"[{amount} taka] has been deposited to [Account no:{self.account_no}]")

    def profit(self):
        """ 5% per year profit!
            [Profit = Deposit x Interest Rate x Time]
            Interest Rate = 5%
            Time = 1 year """
        profit = self._balance * 0.05 * 1
        self._balance += profit
        return f"Your profit for this year is {profit}"

    def reset_withdrawals(self):
        """Resets withdrwals attributes every month."""
        self.withdrawals = 0

    def checkbalance(self):
        """Checks if the account no and the pin no matches or not before revealing the balance."""
        account = input("Enter Account No: ")
        password = int(input("Enter Pin No: "))
        if (account == self.account_no) and (password == self.password):
            return self._balance
        else:
            return "Your Account No and Pin didn't match!!!"



class CurrentAccount(SavingsAccount):
    """This is the Child class of (SavingsAccount) class."""
    def __init__(self, account_no, pin):
        """Calls the super().__init__ function to get access to all the methods and attributes of the parent class"""
        super().__init__(account_no, pin)

    def withdraw(self, amount):
        """
        ## This method overrid the method form the parent class ##
        1. Checks if the balance after the withdrawal and the fees fall below the minimum balance.
        2. If [1] is false then it allows to withdraw the required amount. Else it denies the transaction.
        """
        if ((self._balance - amount) >= 1000):
            self._balance -= amount
        else:
            print(f"Transaction failed!!! You don't have sufficient balance!!!")

    def profit(self):
        """ 
        ## This method overrid the method form the parent class ##
        3% per year profit!
        [Profit = Deposit x Interest Rate x Time]
        Interest Rate = 5%
        Time = 1 year
        """
        profit = self._balance * 0.03 * 1
        self._balance += profit
        return f"Your profit for this year is {profit}"




# account_1 = SavingsAccount("0152330101", 1234)
# print(account_1.checkbalamce())
# account_1.deposite(50000)
# print(account_1.checkbalamce())
# account_1.withdraw(10000)
# print(account_1.checkbalamce())
# account_1.withdraw(10000)
# print(account_1.checkbalamce())
# account_1.withdraw(10000)
# print(account_1.checkbalamce())
# account_1.withdraw(10000)
# print(account_1.checkbalamce())
# account_1.withdraw(5000)
# print(account_1.checkbalamce())
# account_1.withdraw(5000)
# print(account_1.checkbalamce())
# print(account_1.checkbalamce().profit())
# print(account_1.checkbalamce())
# account_1.withdraw(5000)
# print(account_1.checkbalamce())
# account_1.deposite(10000)
# print(account_1.checkbalamce())
# account_1.reset_withdrawals()
# account_1.withdraw(5000)
# print(account_1.checkbalamce())


# print("\n2nd Account:=>\n")
# account_2 = CurrentAccount("0152330116", 1234)
# print(account_2.checkbalance())
# account_2.deposite(100000)
# print(account_2.checkbalance())
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# account_2.withdraw(10000)
# print(account_2.checkbalance())
# print(account_2.profit())
# print(account_2.checkbalance())