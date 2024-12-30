from tkinter import Tk, Frame, Label, Entry, Button, Listbox, END, messagebox
import mysql.connector

class ProductManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("Product Management")
        
        self.frame = Frame(self.master)
        self.frame.pack(pady=10)

        self.label_id = Label(self.frame, text="Product ID:")
        self.label_id.grid(row=0, column=0)
        self.entry_id = Entry(self.frame)
        self.entry_id.grid(row=0, column=1)

        self.label_nama_produk = Label(self.frame, text="Product nama_produk:")
        self.label_nama_produk.grid(row=1, column=0)
        self.entry_nama_produk = Entry(self.frame)
        self.entry_nama_produk.grid(row=1, column=1)

        self.label_price = Label(self.frame, text="Price:")
        self.label_price.grid(row=2, column=0)
        self.entry_price = Entry(self.frame)
        self.entry_price.grid(row=2, column=1)

        self.label_quantity = Label(self.frame, text="Quantity:")
        self.label_quantity.grid(row=3, column=0)
        self.entry_quantity = Entry(self.frame)
        self.entry_quantity.grid(row=3, column=1)

        self.button_add = Button(self.frame, text="Add Product", command=self.add_product)
        self.button_add.grid(row=4, column=0, pady=10)

        self.button_edit = Button(self.frame, text="Edit Product", command=self.edit_product)
        self.button_edit.grid(row=4, column=1, pady=10)

        self.button_delete = Button(self.frame, text="Delete Product", command=self.delete_product)
        self.button_delete.grid(row=4, column=2, pady=10)

        self.listbox_products = Listbox(self.master, width=50)
        self.listbox_products.pack(pady=10)
        self.listbox_products.bind('<<ListboxSelect>>', self.on_select)

        self.load_products()

    def load_products(self):
        self.listbox_products.delete(0, END)
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='responsi_5230411130')
        cursor = connection.cursor()
        cursor.execute("SELECT id_produk, nama_produk, harga FROM produk")
        for row in cursor.fetchall():
            self.listbox_products.insert(END, row)
        cursor.close()
        connection.close()

    def on_select(self, event):
        try:
            selected_product = self.listbox_products.get(self.listbox_products.curselection())
            self.entry_id.delete(0, END)
            self.entry_id.insert(END, selected_product[0])
            self.entry_nama_produk.delete(0, END)
            self.entry_nama_produk.insert(END, selected_product[1])
            self.entry_harga.delete(0, END)
            self.entry_harga.insert(END, selected_product[2])
        except IndexError:
            pass

    def add_product(self):
        nama_produk = self.entry_nama_produk.get()
        harga = self.entry_harga.get()
        
        if not nama_produk or not harga:
            messagebox.showerror("Input Error", "Please fill all fields")
            return
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='responsi_5230411130')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO produk (nama_produk, harga) VALUES (%s, %s,)", (nama_produk, harga,))
        connection.commit()
        cursor.close()
        connection.close()
        self.load_products()
        self.clear_entries()

    def edit_product(self):
        id_produk = self.entry_id_produk.get()
        nama_produk = self.entry_nama_produk.get()
        harga = self.entry_harga.get()
        
        if not id_produk or not nama_produk or not harga :
            messagebox.showerror("Input Error", "Please fill all fields")
            return
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='responsi_5230411130')
        cursor = connection.cursor()
        cursor.execute("UPDATE produk SET nama_produk = %s, price = %s WHERE id = %s", (nama_produk, harga, id_produk))
        connection.commit()
        cursor.close()
        connection.close()
        self.load_products()
        self.clear_entries()

    def delete_product(self):
        id_produk = self.entry_id.get()
        if not id_produk:
            messagebox.showerror("Input Error", "Please select a product to delete")
            return
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='responsi_5230411130')
        cursor = connection.cursor()
        cursor.execute("DELETE FROM produk WHERE id = %s", (id_produk,))
        connection.commit()
        cursor.close()
        connection.close()
        self.load_products()
        self.clear_entries()

    def clear_entries(self):
        self.entry_id.delete(0, END)
        self.entry_nama_produk.delete(0, END)
        self.entry_price.delete(0, END)
        self.entry_quantity.delete(0, END)