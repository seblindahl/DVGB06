from bank_central import BankCentral
import tkinter
from tkinter import messagebox #ingår inte automatiskt i thinker https://docs.python.org/3/library

#instansvariabel från BankCentral

def __init__(self):
    self.bank_objekt = BankCentral()

#valid input metoder

def clearNum(p_num):#return str num
        onlyNum = "".join(filter(str.isdigit, p_num))#https://docs.python.org/3/library
        return onlyNum

def clearName(name): #return str name
    onlyLetters = "".join(filter(str.isalpha()))
    return onlyLetters

def validPNum(p_num):#return bool
        onlyNum = "".join(filter(str.isdigit, p_num))
        return len(onlyNum) == 12

def validName(name):#return bool
    onlyNum = "".join(filter(str.isalpha()))
    return len(onlyNum) > 0

def _create_customer(self):
    input_p_num = p_num_tf.get()
    input_name = name_tf.get()
    input_surname = surname_tf.get()
    if not validPNum(input_p_num):
        messagebox.showerror("Fel", "Personnummer måste innehålla 12 siffror")
        return
    if not validName(input_name) and validName(input_surname):
        messagebox.showerror("Fel", "Namn och/eller efternamn saknas")
        return
    new_cust_confirm = self.bank_objekt.create_customer(input_p_num, input_name, input_surname)
    if not new_cust_confirm:
        messagebox.showerror("Fel", "Personnummer finns redan")
    else:
        messagebox.showinfo("Confirm", "Kund tillagd")#ska använda fstängs - utskriftsmetoderna istället

# skapa huvudfönster windowX
c_window = tkinter.Tk()
window1 = c_window
window1 .title("Kunddata")

#lables
p_num_label = tkinter.Label(window1 ,text = "Personnummer:") #lokalisering, text
name_label = tkinter.Label(window1 , text = "Namn:")
surname_label = tkinter.Label(window1 , text = "Efternamn:")

#textfields
tf_width = 20 #textfältsbredd symetri
p_num_tf = tkinter.Entry(window1 ,width= tf_width)
name_tf = tkinter.Entry(window1 , width= tf_width)
surname_tf = tkinter.Entry(window1 , width= tf_width)

#buttons
#customer_create_button(window1, text = "skapa kund", command = _create_customer())
#p_num_search_button(window1, text = "sök personnummer", command = )
##window_exit_button(window1, text = "sök personnummer", command = )

#positioneringar av gui objekt i c_window
p_num_label.grid(column= 0, row= 0)
name_label.grid(column= 0, row= 1)
surname_label.grid(column= 0, row= 2)
p_num_tf.grid(column= 1, row= 0)
name_tf.grid(column= 1, row= 1)
surname_tf.grid(column= 1, row= 2)


window1.mainloop()#låter fönstret vara kvar och lyssnar kontinuerligt