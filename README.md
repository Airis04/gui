# Cashier System

This project is a simple cashier system designed for small stores, implemented using Python's Tkinter for the GUI and connected to a MySQL database. The application allows users to manage products, process transactions, and export transaction data to Excel.

## Features

- **Product Management**: 
  - Add, edit, delete, and view products in the database.
  
- **Transaction Processing**: 
  - Select products, input quantities, calculate total prices, and save transactions.
  - Display a list of all transactions.

- **Export to Excel**: 
  - Export transaction data to an Excel file for reporting purposes.

## Requirements

To run this project, you need to have the following dependencies installed:

- Tkinter
- MySQL Connector
- openpyxl (for Excel export)

You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Ensure you have MySQL installed and create a database named `responsi_5230411130`.
3. Update the database connection settings in `src/database.py` if necessary.
4. Run the application by executing `src/app.py`.

## Usage Guidelines

- Launch the application and navigate through the GUI to manage products and process transactions.
- Ensure to validate inputs to avoid errors during transactions.
- Use the export feature to generate Excel reports of transactions for your records.

## License

This project is open-source and available for modification and distribution under the MIT License.