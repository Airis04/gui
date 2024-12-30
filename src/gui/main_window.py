from tkinter import Tk, Frame, Label, Button, Menu, messagebox
from gui.product_management import ProductManagement
from gui.transaction_processing import TransactionProcessing

class MainWindow:
    def __init__(self, master,database):
        self.master = master
        self.database = database
        # self.transaction_processing = TransactionProcessing(self.master, self.database)
        self.master.title("Cashier System")
        self.master.geometry("800x600")

        self.create_menu()
        self.create_widgets()

        self.product_management = ProductManagement(self.master)
        self.transaction_processing = TransactionProcessing(self.master,self.database)

    def create_menu(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.master.quit)

    def create_widgets(self):
        frame = Frame(self.master)
        frame.pack(pady=20)

        label = Label(frame, text="Welcome to the Cashier System", font=("Helvetica", 16))
        label.pack()

        btn_product_management = Button(frame, text="Manage Products", command=self.open_product_management)
        btn_product_management.pack(pady=10)

        btn_transaction_processing = Button(frame, text="Process Transactions", command=self.open_transaction_processing)
        btn_transaction_processing.pack(pady=10)

    def open_product_management(self):
        self.product_management.show()

    def open_transaction_processing(self):
        self.transaction_processing.show()


def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()