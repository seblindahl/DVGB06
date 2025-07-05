import tkinter as tk
from tkinter import messagebox # importeras inte ens med asterix
from tkinter import ttk

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
    def __init__(self):
        super().__init__()

        font1 = "Arial"
        font1_size = 13
        frame_n = 4
        window_height = 800
        window_width = 1200
        window_size = f"{window_width}x{window_height}"
        frame_height = window_height // frame_n
        tf_width = 20  # textfältsbredd symetri

        def row_n_column_expander(frame_container, rows, columns):#anpassar rader och columner efter storlek källa: https://stackoverflow.com/questions/75250679/tkinter-making-a-large-number-of-cells-with-grid-while-using-geometry-property
            for row in range(rows):
                frame_container.rowconfigure(row,weight=1)
            for column in range(columns):
                frame_container.columnconfigure(column, weight=1)


        self.bank_objekt = BankCentral()
        self.title("BankOfPython - Main window")
        #self.iconbitmap("adress") gör en icon
        self.geometry(window_size)

        #Frame till huvudfönster
        self.frame1 = tk.Frame(self, bg="blue")
        self.frame2 = tk.Frame(self, bg="red")
        self.frame3 = tk.Frame(self, bg="white")
        self.frame4 = tk.Frame(self, bg="grey")

        self.frame1.grid(row=0, column=0, sticky="nsew") #sticky fäster north,south, east, west för att flylla ut liknar borderlayout
        self.frame2.grid(row=1, column=0, sticky="nsew")
        self.frame3.grid(row=2, column=0, sticky="nsew")
        row_n_column_expander(self, rows=4, columns=1)#ramar expanderas efter huvudfönstrets(root) storlek

        #Frame1(row0)byggsatser
        #3st inre ramar till frame1 för layout
        colframe1_frame1 = tk.Frame(self.frame1, bg="blue")
        colframe2_frame1 = tk.Frame(self.frame1, bg="black")
        colframe3_frame1 = tk.Frame(self.frame1, bg="white")
        #Frame1 inre ramar positionering kolumnvis 3st
        colframe1_frame1.grid(row=0, column=0)
        colframe2_frame1.grid(row=0, column=1)
        colframe3_frame1.grid(row=0, column=2)
        #Frame1 expanderbara inre ramar
        row_n_column_expander(self.frame1, rows=1, columns=3)
        #Frame1 sökpanel i mittersta ramen, lägg till pady för layout
        p_num_label = tk.Label(colframe2_frame1, text="Personnummer:", font=(font1, font1_size))
        name_label = tk.Label(colframe2_frame1, text="Namn:", font=(font1,font1_size))
        surname_label = tk.Label(colframe2_frame1, text="Efternamn:", font=(font1,font1_size))
        p_num_tf = tk.Entry(colframe2_frame1, width=tf_width)
        name_tf = tk.Entry(colframe2_frame1, width=tf_width)
        surname_tf = tk.Entry(colframe2_frame1, width=tf_width)
        create_customer_button = tk.Button(colframe2_frame1, text="Sök", command= self.create_customer)
        close_window_button = tk.Button(colframe2_frame1, text= "Stäng", command= self.destroy)
        center_col = 0 # för framtida justeringar
        p_num_label.grid(column=center_col, row=0)
        name_label.grid(column=center_col, row=1)
        surname_label.grid(column=center_col, row=2)
        p_num_tf.grid(column=center_col+1, row=0)
        name_tf.grid(column=center_col+1, row=1)
        surname_tf.grid(column=center_col+1, row=2)
        create_customer_button.grid(column=center_col, row=3)
        close_window_button.grid(column=center_col+1, row=3)

        #Frame2(row1) table med kunddata Källor: https://www.youtube.com/watch?v=YTqDYmfccQU, https://www.youtube.com/watch?v=-rVA37OVDs8
        #row_n_column_expander(self.frame2, rows=3, columns=1)  # ramar expanderas efter huvudfönstrets(root) storlek
        customer_info_tree_frame_frame2 = tk.Frame(self.frame2, bg="yellow")
        account_info_tree_frame_frame3 = tk.Frame(self.frame3,bg="purple")
        customer_info_tree_frame_frame2.grid(row=0, column=0, sticky="nsew")
        account_info_tree_frame_frame3.grid(row=1, column=0, sticky="nsew")

       # row_n_column_expander(customer_info_tree_frame_frame2, rows=1, columns=2)
        #row_n_column_expander(account_info_tree_frame_frame3, rows=1, columns=2)

        col_n = 3#antal columner i customer_info_tree
        column_width=window_width//col_n
        customer_info_tree = ttk.Treeview(self.frame2)
        customer_info_tree["columns"] = ("Personnummer","Namn", "Efternamn")
        customer_info_tree.column("#0", width=0, stretch=tk.NO)#Kallas spökkolumn, måste den finnas
        customer_info_tree.column("Personnummer", width=column_width, anchor="w")
        customer_info_tree.column("Namn", width=column_width, anchor="center")
        customer_info_tree.column("Efternamn", width=column_width, anchor="w")
        customer_info_tree.heading("Personnummer", text= "Personnummer", anchor="w")
        customer_info_tree.heading("Namn", text="Namn", anchor="center")
        customer_info_tree.heading("Efternamn", text="Efternamn", anchor="w")
        customer_info_tree.grid(row=0, column=0, sticky="nswe")
        customer_info_tree_scroll = tk.Scrollbar(self.frame2, orient="vertical", command=customer_info_tree.yview)#scroll horisontel
        customer_info_tree.configure(yscrollcommand=customer_info_tree_scroll.set)
        customer_info_tree_scroll.grid(row=0, column=1, sticky="e")#scrollbar höger sida
        customer_info_tree.rowconfigure(0, weight=1)
        customer_info_tree.columnconfigure(0, weight=1)

        col_n = 3  # antal columner i customer_info_tree
        account_info_tree_heading1 = "Kontonummer"
        account_info_tree_heading2 = "Kontotyp"
        account_info_tree_heading3 = "Saldo"
        column_width = window_width // col_n


        account_info_tree = ttk.Treeview(account_info_tree_frame_frame3)
        account_info_tree["columns"] = (account_info_tree_heading1,account_info_tree_heading2, account_info_tree_heading3)
        account_info_tree.column("#0", width=0, stretch=tk.NO)  # Kallas spökkolumn, måste den finnas
        account_info_tree.column(account_info_tree_heading1, width=column_width, anchor="w")
        account_info_tree.column(account_info_tree_heading2, width=column_width, anchor="center")
        account_info_tree.column(account_info_tree_heading3, width=column_width, anchor="w")
        account_info_tree.heading(account_info_tree_heading1, text=account_info_tree_heading1, anchor="w")
        account_info_tree.heading(account_info_tree_heading2, text=account_info_tree_heading2, anchor="center")
        account_info_tree.heading(account_info_tree_heading3, text=account_info_tree_heading3, anchor="w")
        account_info_tree.grid(row=0, column=0, sticky="nswe")
        account_info_tree_scroll = tk.Scrollbar(account_info_tree_frame_frame3)
        account_info_tree_scroll.grid(row=0, column=1, sticky="ns")  # scrollbar höger sida


        # 3st inre ramar till frame1 för layout

        # Frame1(row0)byggsatser
        # 3st inre ramar till frame1 för layout
        colframe1_frame3 = tk.Frame(self.frame3, bg="blue")
        colframe2_frame3 = tk.Frame(self.frame3, bg="red")
        colframe3_frame3 = tk.Frame(self.frame3, bg="purple")
        # Frame1 inre ramar positionering kolumnvis 3st
        colframe1_frame3.grid(row=0, column=0)
        colframe2_frame3.grid(row=0, column=1)
        colframe3_frame3.grid(row=0, column=2)
        # Frame1 expanderbara inre ramar
        row_n_column_expander(self.frame1, rows=0, columns=3)
        # Frame1 sökpanel i mittersta ramen, lägg till pady för layout
        account_num_label= tk.Label(colframe1_frame3, text="Kontonummer", font=(font1, font1_size))
        amount_label = tk.Label(colframe1_frame3, text="Summa", font=(font1, font1_size))
        account_num_tf = tk.Entry(colframe1_frame3, width=tf_width)
        amount_tf = tk.Entry(colframe1_frame3, width=tf_width)
        account_input_type = tk.StringVar(value="")
        account_withdrawal_rbutton = tk.Radiobutton(colframe1_frame3, text="Insättning", variable=account_input_type, value="")
        account_deposit_rbutton  = tk.Radiobutton(colframe1_frame3, text="Uttag",variable=account_input_type, value="")
        center_col = 1  # för framtida justeringar
        account_num_label.grid(column=center_col, row=0)
        amount_label.grid(column=center_col, row=1)
        account_num_tf.grid(column=center_col + 1, row=0)
        amount_tf.grid(column=center_col + 1, row=1)
        account_withdrawal_rbutton.grid(column=center_col, row=3)
        account_deposit_rbutton.grid(column=center_col + 1, row=3)








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

