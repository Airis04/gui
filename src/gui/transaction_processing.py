from tkinter import Label, Listbox, Entry, Button, END

class TransactionProcessing:
    def __init__(self, master, database):
        self.master = master
        self.database = database
        # self.transaction_processing = TransactionProcessing(self.master, self.database)
        self.selected_id_produk = None
        
        self.create_widgets()
        self.populate_product_list()

    def create_widgets(self):
        self.product_label = Label(self.master, text="Select Product:")
        self.product_label.pack()

        self.product_listbox = Listbox(self.master)
        self.product_listbox.pack()
        self.product_listbox.bind('<<ListboxSelect>>', self.on_product_select)

        self.jumlah_label = Label(self.master, text="jumlah:")
        self.jumlah_label.pack()

        self.jumlah_entry = Entry(self.master)
        self.jumlah_entry.pack()

        self.calculate_button = Button(self.master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.pack()

        self.total_label = Label(self.master, text="Total Price: $0.00")
        self.total_label.pack()

        self.save_button = Button(self.master, text="Save Transaction", command=self.save_transaction)
        self.save_button.pack()

        self.transaction_list_label = Label(self.master, text="Transaction List:")
        self.transaction_list_label.pack()

        self.transaction_listbox = Listbox(self.master)
        self.transaction_listbox.pack()

        self.export_button = Button(self.master, text="Export to Excel", command=self.export_to_excel)
        self.export_button.pack()

    def populate_product_list(self):
        products = self.database.get_products()
        for product in products:
            self.product_listbox.insert(END, f"{product[0]} - {product[1]} - ${product[2]:.2f}")

    def on_product_select(self, event):
        selection = self.product_listbox.curselection()
        if selection:
            self.selected_id_produk = selection[0] + 1  # Assuming product IDs start from 1

    def calculate_total(self):
        jumlah = self.jumlah_entry.get()
        if not jumlah.isdigit() or self.selected_id_produk is None:
            return
        jumlah = int(jumlah)
        product = self.database.get_product_by_id(self.selected_id_produk)
        total_harga = product[2] * jumlah  # Assuming product[2] is the price
        self.total_label.config(text=f"Total Price: ${total_harga:.2f}")

    def save_transaction(self):
        jumlah = self.jumlah_entry.get()
        if not jumlah.isdigit() or self.selected_id_produk is None:
            return
        jumlah = int(jumlah)
        product = self.database.get_product_by_id(self.selected_id_produk)
        total_harga = product[2] * jumlah
        self.database.add_transaction(self.selected_id_produk, jumlah, total_harga)
        self.transaction_listbox.insert(END, f"Product ID: {self.selected_id_produk}, jumlah: {jumlah}, Total: ${total_harga:.2f}")

    def export_to_excel(self):
        from utils.export_to_excel import export_transactions
        export_transactions(self.database.get_transactions())