from openpyxl import Workbook
import mysql.connector

def export_transactions_to_excel(database_config, output_file):
    try:
        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM transactions')
        transactions = cursor.fetchall()

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = 'Transactions'

        # Adding headers
        headers = ['ID', 'Product ID', 'Quantity', 'Total Price']
        sheet.append(headers)

        # Adding transaction data
        for transaction in transactions:
            sheet.append(transaction)

        workbook.save(output_file)
        print(f'Transactions exported successfully to {output_file}')
    except mysql.connector.Error as err:
        print(f'Error: {err}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()