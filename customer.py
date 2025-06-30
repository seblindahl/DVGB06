from account import Account
from typing import List

class Customer:
    def __init__(self, p_num: int, name: str, surname: str):
        self.p_num = p_num
        self.name = name
        self.surname = surname
        self.customer_accounts: List[Account] = []

    def get_customer_account(self, account_id: int):
        for account in self.customer_accounts:
            if account.account_num == account_id:
             return account

    def get_customer_p_num(self):
        return self.name

    def get_customer_name(self):
        return self.name

    def get_customer_surname(self):
        return self.surnamename

    def set_p_num(self, new_p_num):
        self.p_num = new_p_num

    def set_name(self, new_name):
        self.name = new_name

    def set_surname(self, new_name):
        self.surname = new_name

    def new_customer_account(self):
        account = Account()
        self.customer_accounts.append(account)
        return account.account_num

    def delete_account(self, account_id: int):
        self.customer_accounts = [
            account for account in self.customer_accounts
            if account.account_num != account_id
        ]

