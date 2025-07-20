import tkinter as tk
from tkinter import messagebox, StringVar  # importeras inte ens med asterix
from tkinter import ttk

import bank_central
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






class BankGui(tk.Tk):
    def __init__(self, bank: BankCentral):
        super().__init__()
        self.bank_object = bank

        font1 = "Arial"
        font1_size = 13
        frame_n = 4
        window_height = 800
        window_width = 1200
        window_size = f"{window_width}x{window_height}"
        frame_height = window_height // frame_n
        tf_width = 20  # textfältsbredd symetri
        self.displayed_p_num = None#temporärt personummer

        self.title("BankOfPython - Main window")
        # self.iconbitmap("adress") gör en icon
        self.geometry(window_size)

        #meny längst upp
        self.menu = tk.Menu(self)#skapar menyrad
        self.config(menu=self.menu)#att meny skall vara meny i huvudfönster
        self.arkiv_menu = tk.Menu(self.menu)
        self.arkiv_menu.add_command(label="Ny kund", command= lambda: self.new_customer())
        self.arkiv_menu.add_command(label="Nytt konto", command= lambda: self.new_account())
        self.menu.add_cascade(label="Arkiv", menu=self.arkiv_menu)

        self.frame1 = tk.Frame(self, bg="blue")
        self.frame2 = tk.Frame(self, bg="red")
        self.frame3 = tk.Frame(self, bg="white")
        self.frame4 = tk.Frame(self, bg="grey")
        self.frame5 = tk.Frame(self, bg="grey")

        self.frame1.pack(side="top",fill="both", expand=True)
        self.frame2.pack(side="top",fill="both", expand=True)
        self.frame3.pack(side="top",fill="both", expand=True)
        self.frame4.pack(side="top",fill="both", expand=True)
        self.frame5.pack(side="top", fill="both", expand=True)

        #frame1 kund kontroll
        self.control_frame = ControlFrame(self.frame1, self, panel_class = CustomerControl)
        self.control_frame.pack(fill="both", expand=True)

        #Frame2 Kund table
        headings = ["Personnummer", "namn", "efternamn"]
        self.customer_tree = TreeScrollFrame(self.frame2, headings)
        self.customer_tree.pack(fill="both", expand=True)


        #frame3 Kontrollpanel för konton
        self.control_frame = ControlFrame(self.frame3, self, panel_class=AccountControl)
        self.control_frame.pack(fill="both", expand=True)

        #Frame4 Konto table
        headings = ["kontonummer", "Typ", "saldo"]
        self.account_tree = TreeScrollFrame(self.frame4, headings)
        self.account_tree.pack(fill="both", expand=True)

        #frame 5 transaktionsdata table
        headings = ["Datum", "Typ", "belopp", "saldo"]
        self.transaction_tree = TreeScrollFrame(self.frame5, headings)
        self.transaction_tree.pack(fill="both", expand=True)

    def new_customer(self):
        new_customer_window = tk.Toplevel(self)
        new_customer_window.geometry("300x300")
        new_customer_window.title("Ny kund")
        form = CustomerControl(new_customer_window, self, external_new_customer=True)
        form.pack(fill="both", expand=True)

    def new_account(self):
        new_account_window = tk.Toplevel(self)
        new_account_window.geometry("300x300")
        new_account_window.title("Nytt konto")
        form = AccountSettings(new_account_window, self)
        form.pack(fill="both", expand=True)

    def create_customer(self, input_p_num, input_name, input_surname):
        if not validPNum(input_p_num):
            messagebox.showerror("Fel", "Personnummer måste innehålla 12 siffror")
            return
        if not validName(input_name) or not validName(input_surname):
            messagebox.showerror("Fel", "Namn och/eller efternamn saknas")
            return
        new_cust_confirm = self.bank_object.create_customer(input_p_num, input_name, input_surname)
        if not new_cust_confirm:
            messagebox.showerror("Fel", "Personnummer finns redan")
        else:
            messagebox.showinfo("Confirm", "Kund tillagd")  # ska använda fstängs - utskriftsmetoderna istället

    def find_customer(self, input_p_num):
        customer = self.bank_object.get_customer_tuple(input_p_num)
        if not customer:
            messagebox.showerror("Fel", "Kunden hittades ej")
            return
        self.customer_tree.insert_data(customer)
        customer_accounts = self.bank_object.get_customer_account_info_tuple_list(input_p_num)
        if customer_accounts is not None:
            for account_tuple in customer_accounts:
                self.account_tree.insert_data(account_tuple)
        self.displayed_p_num = input_p_num

    def create_new_account(self, input_p_num):
        account_num = self.bank_object.create_new_savings_account(input_p_num)
        if not account_num:
            messagebox.showerror("Fel", "Fel konto skapades ej")
            return
        messagebox.showinfo("Nytt kontonummer", account_num)
        return

    def gui_deposit(self, account_num, amount):
        print(self.displayed_p_num)
        print("kontonummer:", account_num)
        print("belopp:", amount)
        int_amount = int(amount)#konvertera lägg till extra konvertering
        transacation_tuple_list = self.bank_object.deposit(self.displayed_p_num, account_num,int_amount)
        print("result:", transacation_tuple_list)
        if transacation_tuple_list:
            for transaction in transacation_tuple_list:
                self.transaction_tree.insert_data(transaction)
        else:
            messagebox.showerror("Fel", "Insättning genomfördes ej")

class ControlFrame(tk.Frame):
    def __init__(self, parent, bank_gui, panel_class=None):
        super().__init__(parent)
        self.bank_gui = bank_gui #referens från subklass CustomerControl till masterklass

        self.i_frame1 = tk.Frame(self, bg="blue")
        self.i_frame2 = tk.Frame(self, bg="red")
        self.i_frame3 = tk.Frame(self, bg="white")

        self.i_frame1.pack(side="left", fill="both", expand=True)
        self.i_frame2.pack(side="left", fill="y", expand=True)
        self.i_frame3.pack(side="left", fill="both", expand=True)

        #om någon skickar in widget med textfields och lables osv. så läggs detta in i mittersta frame
        if panel_class:
            self.panel_class = panel_class(self.i_frame2, self.bank_gui)
            self.panel_class.pack(fill="both", expand=True)

class CustomerControl(tk.Frame): #källa: https://www.youtube.com/watch?v=7A_csP9drJw&t=434s
    def __init__(self,parent, bank_gui, external_new_customer = False):
        super().__init__(parent)
        self.bank_gui = bank_gui #referens till överordnad subklass (ControlFrame)

        tf_width = 20

        #label
        self.label1 = tk.Label(self, text="Personummer", font=("Arial", 13))
        self.label2 = tk.Label(self, text="namn", font=("Arial", 13))
        self.label3 = tk.Label(self, text="efternamn", font=("Arial", 13))

        #textfields
        self.entry1 = tk.Entry(self, width=tf_width)
        self.entry2 = tk.Entry(self, width=tf_width)
        self.entry3 = tk.Entry(self, width=tf_width)

        #knappar
        if external_new_customer:
            self.button1_new_cust = tk.Button(self, text="Ny kund",command=lambda: self.bank_gui.create_customer(self.entry1.get(), self.entry2.get(),self.entry3.get()))
            self.button1_new_cust.grid(row=3, column=1, sticky="nsew")
        if not external_new_customer:
            self.button2 = tk.Button(self, text="Sök", command=lambda: self.bank_gui.find_customer(self.entry1.get()))
            self.button2.grid(row=3, column=1, sticky="nsew")
        self.button3 = tk.Button(self, text="Rensa")
        self.button3.grid(row=4, column=1, sticky="nsew")

        #måste överge pack när det är formulär tillförmån för .grid
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)

        #gör kolumnerna expanderbara
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

class TreeScrollFrame(tk.Frame): #källa: https://www.youtube.com/watch?v=YTqDYmfccQU&t=242s
    def __init__(self, parent, col, col_widths = None):
        super().__init__(parent)

        # treeview med scrollbar för kund-, konto-, transaktionsdata.
        self.tree = ttk.Treeview(self, columns=col, show="headings")#skapar träd

        for i, c in enumerate(col):#olika kolumner och kolumnheadings
            width = col_widths[i] if col_widths else 100
            self.tree.heading(c, text=c)
            self.tree.column(c, width=width)

        scrollbar = tk.Scrollbar(self, orient="vertical", command="tree.yview")
        self.tree.configure(yscrollcommand=scrollbar.set)#kollpar scrollbar till tree
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def insert_data (self, data):#lägger till data i ny rad
        print("Debug:", data, type(data))
        self.tree.insert("", "end", values=data)

class AccountControl(tk.Frame): #källa: https://www.youtube.com/watch?v=7A_csP9drJw&t=434s
    def __init__(self,parent, bank_gui):
        super().__init__(parent)
        self.bank_gui = bank_gui #referens till överordnad subklass (ControlFrame)

        tf_width = 20

        #label
        self.label1 = tk.Label(self, text="Kontonummer", font=("Arial", 13))
        self.label2 = tk.Label(self, text="Belopp", font=("Arial", 13))
        self.label3 = tk.Label(self, text="Transaktion", font=("Arial", 13))

        #textfields
        self.entry1 = tk.Entry(self, width=tf_width)
        self.entry2 = tk.Entry(self, width=tf_width)
        #self.entry3 = tk.Entry(self, width=tf_width)

        #radioknappar källa: https://www.youtube.com/watch?v=kZM3O1F-U08
        radio_value = StringVar()
        radio_value.set("deposit")  # standardvärde uttag
        self.radio1 = tk.Radiobutton(self, text="Uttag", variable=radio_value, value="withdrawal")
        self.radio2 = tk.Radiobutton(self, text="Insättning", variable=radio_value, value="deposit")

        #knappar
        self.button1 = tk.Button(self, text="Utför", command= lambda: self.bank_gui.gui_deposit(self.entry1.get(), self.entry2.get()))
        self.button2 = tk.Button(self, text="Rensa", command= None)


        #måste överge pack när det är formulär tillförmån för .grid
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.radio1.grid(row=2, column=1, sticky="w")
        self.radio2.grid(row=2, column=1, sticky="e")
        self.button1.grid(row=3, column=1, sticky="nsew")
        self.button2.grid(row=4, column=1, sticky="nsew")


        #gör kolumnerna expanderbara
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

class AccountSettings(tk.Frame): #källa: https://www.youtube.com/watch?v=7A_csP9drJw&t=434s
    def __init__(self,parent, bank_gui):
        super().__init__(parent)
        self.bank_gui = bank_gui #referens till överordnad mastercalss


        tf_width = 20
        tf1_label_text = "Personummer"
        tf2_label_text = "Namn"
        tf3_label_text  = "Efternamn"
        tf4_label_text = "Kontotyp"
        tf5_label_text  = "Sparränta (%)"
        tf6_label_text  = "Övertrasseringsränta"
        tf7_label_text = "Startbelopp"
        rb1_label_text = "Sparkonto"
        rb2_label_text = "Kreditkonto"

        #label
        self.label1 = tk.Label(self, text=tf1_label_text, font=("Arial", 13))
        self.label2 = tk.Label(self, text=tf2_label_text, font=("Arial", 13))
        self.label3 = tk.Label(self, text=tf3_label_text, font=("Arial", 13))
        self.label4 = tk.Label(self, text=tf4_label_text, font=("Arial", 13))
        self.label5 = tk.Label(self, text=tf5_label_text, font=("Arial", 13))
        self.label6 = tk.Label(self, text=tf6_label_text, font=("Arial", 13))
        self.label7 = tk.Label(self, text=tf7_label_text, font=("Arial", 13))

        #textfields
        self.entry1 = tk.Entry(self, width=tf_width)
        self.entry2 = tk.Entry(self, width=tf_width)
        self.entry3 = tk.Entry(self, width=tf_width)
        self.entry4 = tk.Entry(self, width=tf_width)
        self.entry5 = tk.Entry(self, width=tf_width)
        self.entry6 = tk.Entry(self, width=tf_width)
        self.entry7 = tk.Entry(self, width=tf_width)

        #radioknappar källa: https://www.youtube.com/watch?v=kZM3O1F-U08
        radio_value = StringVar()
        radio_value.set(rb2_label_text)  # standardvärde uttag
        self.radio1 = tk.Radiobutton(self, text=rb1_label_text, variable=radio_value, value="new_savings_account")
        self.radio2 = tk.Radiobutton(self, text=rb2_label_text, variable=radio_value, value="new_credit_account")

        #knappar
        self.button1 = tk.Button(self, text="Utför", command= lambda: self.bank_gui.create_new_account(self.entry1.get()))
        self.button2 = tk.Button(self, text="Avbryt", command= None)


        #måste överge pack när det är formulär tillförmån för .grid
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.label4.grid(row=3, column=0)
        self.label5.grid(row=4, column=0)
        self.label6.grid(row=5, column=0)
        self.label7.grid(row=6, column=0)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)
        self.entry4.grid(row=3, column=1)
        self.entry5.grid(row=4, column=1)
        self.entry6.grid(row=5, column=1)
        self.entry7.grid(row=6, column=1)
        self.radio1.grid(row=7, column=1, sticky="w")
        self.radio2.grid(row=7, column=1, sticky="e")
        self.button1.grid(row=8, column=1, sticky="nsew")
        self.button2.grid(row=9, column=1, sticky="nsew")


        #gör kolumnerna expanderbara
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)




