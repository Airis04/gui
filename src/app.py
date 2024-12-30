from tkinter import Tk
from database import Database
from gui.main_window import MainWindow
import mysql.connector
from mysql.connector import Error

class CashierApp:
    def __init__(self):
        try:
            self.database = Database('localhost')
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            exit(1)
        self.root = Tk()
        self.root.title("Cashier System")
        self.main_window = MainWindow(self.root, self.database)  # Pass both root and database arguments

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CashierApp()
    app.run()