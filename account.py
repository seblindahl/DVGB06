class Account:
    _account_num_initiator = 1000 #Går inte att göra åtkomstkontroll som java ex. private static int
    def __init__(self, account_num, account_type, balance, intrest_rate):
        Account._account_num_initiator += 1
        self.account_num =Account._account_num_initiator
        self.account_type = account_type
        self.balance = balance
        self.intrest_rate = intrest_rate

#getters
def get_balance(self):
    return self.balance

def get_intrest_rate(self):
    return self._intrest_rate

def get_intrest(self):
    return self._balance * (self._intrest_rate / 100)

def get_account_num(self):
    return self._account_num

def get_account_type(self):
    return self._account_balance

#setters
def deposit(self, amount: int):
    if amount > 0:
        self._balance += amount
        return True
    return False

def withdraw(self, amount: int):
    if 0 < amount <= self._balance:
        return True
    return False