class Database:
    def __init__(self, host='localhost', user='root', password='', database='responsi_5230411130'):
        import mysql.connector
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produk (
                id_produk INT AUTO_INCREMENT PRIMARY KEY,
                nama_produk VARCHAR(255) NOT NULL,
                harga DECIMAL(10, 2) NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transaksi (
                id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
                id_produk INT NOT NULL,
                jumlah INT NOT NULL,
                total_harga DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (id_produk) REFERENCES produk(id_produk)
            )
        ''')
        self.connection.commit()

    def add_product(self, nama_produk, harga):
        self.cursor.execute('INSERT INTO produk (nama_produk, harga) VALUES (%s, %s)', (nama_produk, harga))
        self.connection.commit()

    def edit_product(self, id_produk, nama_produk, harga):
        self.cursor.execute('UPDATE produk SET nama_produk = %s, harga = %s WHERE id_produk = %s', (nama_produk, harga, id_produk))
        self.connection.commit()

    def delete_product(self, id_produk):
        self.cursor.execute('DELETE FROM produk WHERE id_produk = %s', (id_produk,))
        self.connection.commit()

    def get_products(self):
        self.cursor.execute('SELECT * FROM produk')
        return self.cursor.fetchall()

    def add_transaction(self, id_produk, quantity, total_harga):
        self.cursor.execute('INSERT INTO transaksi (id_produk, jumlah, total_harga) VALUES (%s, %s, %s)', (id_produk, quantity, total_harga))
        self.connection.commit()

    def get_transactions(self):
        self.cursor.execute('SELECT * FROM transaksi')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
