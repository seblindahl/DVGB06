from typing import List  # möjliggör objektlistor
import locale # svensk bank svenska kronor

from customer import Customer

class BankCentral:

    def __init__(self):
        self.customers: List[Customer] = []

    #metoder för customer objekt
    def create_customer(self, p_num: str, name: str, surname: str):
        if self._get_customer(p_num):#kontrollerar om kund redan finns
            return False
        self.customers.append(Customer(p_num, name, surname))  # Korrigerat 2506027 ordningsföljd
        return True

    def delete_customer(self, p_num: str):
        customer = self._find_customer(p_num)
        if not customer:
            return None
        info = [self._customer_info_str(customer)]
        for account in customer.get_accounts():
            info.append(
                f"{self._get_account_num_str(account)} {self._amount_to_sek_str(account.balance)} {account.account_type} {self._get_amount_in_sek_str(account.calculate_intrest())}")
        self.customers.remove(customer)
        return info

    # metoder för account objekt
    def close_account(self, p_num: str, account_id: int):
        customer = self._find_customer(p_num)
        account = customer.find_account(account_id) if customer else None
        if not account:
            return None
        account_info = f"{self._get_account_num_str(account)} {self._get_amount_in_sek_str(account.balance)} {account.account_type} {self._intrest_rate_str(account.intrest_rate)}" #korrigerat 250626 felaktiga anrop
        customer.delete_account(account_id)
        return account_info

    #getters för kundobjekt
    def _get_customer(self, p_num: str):#hittar kund och kontroll av dubletter
        for customer in self.customers:
            if customer.p_num == p_num:
                return customer
        return None #250627 korrigerat fel, stod innanför loop

    def get_all_customers(self):
        return [self._customer_info_str(c) for c in self.customers]

    #setters för accountobjekt
    def deposit(self, p_num:str, account_id: int, amount: int):
        customer = self._find_customer(p_num)
        account = customer.find_account(account_id) if customer else None
        return account.deposit(amount) if account else False

    def withdraw(self, p_num:str, account_id: int, amount: int):
        customer = self._find_customer(p_num)
        account = customer.find_account(account_id) if customer else None
        if not account:
            return None
        account_info = f"{self._get_account_num_str(account)} {self._get_amount_in_sek_str(account.balance)} {account.account_type} {self._intrest_rate_str(account.intrest_rate)}"#korrigerat 250626 felaktiga anrop
        customer.delete_account(account_id)
        return  account_info

    #hjälpmetoder f-strängs utskrifter för bokföring - fanns i java versionen, nödvändigt? får se längre fram ev. messagebox och transaktioner

    def _customer_info_str(self, customer: "Customer"):
        return f"{customer.p_num} {customer.name} {customer.surname}" #return formatera till f sträng

    def _get_account_num_str(self, account: "Account"):
        return str(account.account_num)

    def _get_amount_in_sek_str(self, amount: float):
        return locale.currency(amount)

    def _intrest_rate_str(self, rate: float):
        return f"{self.rate}%"

    def _get_customer_info_str(self, p_num:str):
        customer = self._find_customer(p_num)
        if not customer:
            return None
        info = [self._customer_info_str(customer)]
        for account in customer.get_accounts():
            info.append(f"{self._get_account_num_str(account)} {self._get_amount_in_sek_str(account.balance)}")
        return info




