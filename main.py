from bank_central import BankCentral
from gui.bank_gui import BankGui

if __name__ == "__main__":
    bank = BankCentral()
    bank.create_customer("198303203999", "Sebastian", "Lindahl")
    gui = BankGui(bank)
    gui.mainloop()


