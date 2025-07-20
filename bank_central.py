from typing import List  # möjliggör objektlistor
import locale # svensk bank svenska kronor

from account import Account
from customer import Customer

class BankCentral:

    def __init__(self):
        self.customers: List[Customer] = []

    def get_customer(self, p_num):
        for customer in self.customers:
            if customer.p_num == p_num:
                return customer
        return None

    #metoder för customer objekt
    def create_customer(self, p_num: str, name: str, surname: str):
        if self.get_customer(p_num):#kontrollerar om kund redan finns
            return False
        self.customers.append(Customer(p_num, name, surname))
        return True



    def delete_customer(self, p_num: str):
        customer = self.get_customer(p_num)
        if not customer:
            return None
        info = [self._customer_info_str(customer)]
        for account in customer.get_accounts():
            info.append(
                f"{self._get_account_num_str(account)} {self._amount_to_sek_str(account.balance)} {account.account_type} {self._get_amount_in_sek_str(account.calculate_intrest())}")
        self.customers.remove(customer)
        return info

    # metoder för account objekt

    def create_new_savings_account(self, p_num, ):
        customer = self.get_customer(p_num)
        if customer is not None:
            return customer.new_customer_account()
        return None

    def close_account(self, p_num: str, account_id: int):
        customer = self.get_customer(p_num)
        account = customer.find_account(account_id) if customer else None
        if not account:
            return None
        account_info = f"{self._get_account_num_str(account)} {self._get_amount_in_sek_str(account.balance)} {account.account_type} {self._intrest_rate_str(account.intrest_rate)}" #korrigerat 250626 felaktiga anrop
        customer.delete_account(account_id)
        return account_info


    #getters för kundobjekt
    def get_customer_tuple(self, p_num: str):#hittar kund och kontroll av dubletter
        for customer in self.customers:
            if customer.p_num == p_num:
                return (customer.p_num, customer.name, customer.surname) #returnerar tuple
        return None #250627 korrigerat fel, stod innanför loop

    def get_customer_account_info_tuple_list(self, p_num: str):
        customer = self.get_customer(p_num)
        account_info_list = []
        if not customer:
            return None
        for account in customer.customer_accounts:
            account_info_list.append((account.account_num, account.account_type, account.balance))
        return account_info_list


    def _get_all_customers(self):
        return [self._customer_info_str(c) for c in self.customers]

    #setters för accountobjekt
    def deposit(self, p_num:str, account_id: int, amount: int):
        customer = self.get_customer(p_num)
        if not customer:
            print("BankCentral: Ingen kund")
            return None
        print("kontonummer1:", account_id)
        account = customer.get_customer_account(account_id)#hittar inget konto
        print("kontonummer2:", account.account_num)
        if not account:
            print("BankCentral: Inget Konto")
            return None
        temp = account.deposit(amount)
        print("BankCentral_tuple:", temp)
        return temp

    def withdraw(self, p_num:str, account_id: int, amount: int):
        customer = self.get_customer(p_num)
        account = customer.find_account(account_id) if customer else None
        if not account:
            return None
        account_info = f"{self._get_account_num_str(account)} {self._get_amount_in_sek_str(account.balance)} {account.account_type} {self._intrest_rate_str(account.intrest_rate)}"#korrigerat 250626 felaktiga anrop
        customer.delete_account(account_id)
        return  account_info

    #hjälpmetoder f-strängs utskrifter för bokföring - fanns i java versionen, nödvändigt? får se längre fram ev. messagebox och transaktioner



    def get_account_num_str(self, account: "Account"):
        return str(account.account_num)

    def get_amount_in_sek_str(self, amount: float):
        return locale.currency(amount)

    def intrest_rate_str(self, rate: float):
        return f"{self.rate}%"





