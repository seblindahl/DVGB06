import datetime as datetime

class Account:
    _account_num_initiator = 1000 #Går inte att göra åtkomstkontroll som java ex. private static int
    _standard_account_type = "Sparkonto"
    _start_balance = 0
    _standard_intrest_rate = 0.02 + 1



    def __init__(self, account_type=_standard_account_type, balance=_start_balance, intrest_rate=_standard_intrest_rate):
        Account._account_num_initiator += 1
        self.account_num = Account._account_num_initiator
        self.account_type = account_type
        self.balance = balance
        self.intrest_rate = intrest_rate
        self.transaction_list = [] #lista tuple med transaktionsdata

    def get_balance(self):
        return self.balance

    def get_intrest_rate(self):
        return self.intrest_rate

    def get_intrest(self):
        return self.balance * (self.intrest_rate / 100)

    def get_account_num(self):
        return self.account_num

    def get_account_type(self):
        return self.account_type

    def deposit(self, amount: int):
        if int(amount) > 0:
            self.balance += amount
            tid = datetime.datetime.now()
            transaction_tuple = (tid, "Insättning", amount, self.balance)
            self.transaction_list.append(transaction_tuple)
            return [transaction_tuple]#returnerar lista och inte None
        return None

    def withdrawal(self, amount: int):
        if int(amount) <= self.balance:
            self.balance -= amount
            tid = datetime.datetime.now()
            transaction_tuple = (tid, "Uttag", amount, self.balance)
            self.transaction_list.append(transaction_tuple)
            return [transaction_tuple]#returnerar lista och inte None
        return None
