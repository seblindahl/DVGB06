"""

gammal kod:

from tkinter import *
from tkinter import messagebox # importeras inte ens med asterix

from bank_central import BankCentral

standardPNumLength: int = 12 # Det är bättre att detta finns i GUI då kan bank_central användas i andra länder

def clearNum(p_num):  # return str num
    onlyNum = "".join(filter(str.isdigit, p_num))  # https://docs.python.org/3/library
    return onlyNum


def clearName(name):  # return str name
    onlyLetters = "".join(filter(str.isalpha, name))
    return onlyLetters


def validPNum(p_num):  # return bool
    onlyNum = "".join(filter(str.isdigit, p_num))
    return len(onlyNum) == standardPNumLength


def validName(name):  # return bool
    onlyLetters = "".join(filter(str.isalpha, name))
    return len(onlyLetters) > 0


class BankGui(Tk):
    def __init__(self):
        super().__init__()

        font1 = "Arial"
        font1_size = 13

        self.bank_objekt = BankCentral()
        self.title("BankOfPython")
        #self.iconbitmap("adress") gör en icon
        self.geometry("400x450")

        #Label widgets
        self.p_num_label = Label(self, text="Personnummer:", font=(font1, font1_size))
        self.name_label = Label(self, text="Namn:", font=(font1,font1_size))
        self.surname_label = Label(self, text="Efternamn:", font=(font1,font1_size))

        #TF widgets
        tf_width = 20  # textfältsbredd symetri

        self.p_num_tf = Entry(self, width=tf_width)
        self.name_tf = Entry(self, width=tf_width)
        self.surname_tf = Entry(self, width=tf_width)

        #Knapp widgets
        self.create_customer_button = Button(self, text="Ny kund", command= self.create_customer)
        self.close_window_button = Button(self, text= "Stäng", command= self.destroy)

        #rutnäts positioner för widgets
        self.p_num_label.grid(column=0, row=0)
        self.name_label.grid(column=0, row=1)
        self.surname_label.grid(column=0, row=2)
        ""
        self.p_num_tf.grid(column=1, row=0)
        self.name_tf.grid(column=1, row=1)
        self.surname_tf.grid(column=1, row=2)
        ""
        self.create_customer_button.grid(column=0, row=3)
        self.close_window_button.grid(column=2, row=3)

    def create_customer(self):
        input_p_num = self.p_num_tf.get()
        input_name = self.name_tf.get()
        input_surname = self.surname_tf.get()

        if not validPNum(input_p_num):
            messagebox.showerror("Fel", "Personnummer måste innehålla 12 siffror")
            return
        if not validName(input_name) or not validName(input_surname):
            messagebox.showerror("Fel", "Namn och/eller efternamn saknas")
            return
        new_cust_confirm = self.bank_objekt.create_customer(input_p_num, input_name, input_surname)
        if not new_cust_confirm:
            messagebox.showerror("Fel", "Personnummer finns redan")
        else:
            messagebox.showinfo("Confirm", "Kund tillagd")  # ska använda fstängs - utskriftsmetoderna istället



"""