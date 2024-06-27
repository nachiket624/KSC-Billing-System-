import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QMessageBox
from NewCustomer import Ui_Dialog
import mysql.connector
class DialogAddCustmer(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogAddCustmer, self).__init__()
        self.setupUi(self)
        self.connectToDatabase()
        self.dbaddcust.clicked.connect(self.add_customer)

    def connectToDatabase(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1900340220",
                database="BillingSoftware"
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            print("An error occur ")
            QMessageBox.critical(self, "Database Connection Error", str(err))
            sys.exit(1)


    def add_customer(self):
        name = str(self.name_input.text()).lower()
        last_name = str(self.lname_input.text()).lower()
        name = name + " " + last_name
        email = str(self.email_input.text()).lower()
        phone = self.phone_input.text()
        address = str(self.address_input.text()).lower()

        if not name:
            QMessageBox.warning(self, "Input Error", "Customer name is required.")
            return

        query = "INSERT INTO Customers (Name, Email, Phone, Address) VALUES (%s, %s, %s, %s)"
        values = (name, email, phone, address)

        try:
            self.cursor.execute(query, values)
            self.db.commit()
            QMessageBox.information(self, "Success", "Customer added successfully.")
            self.name_input.clear()
            self.email_input.clear()
            self.phone_input.clear()
            self.address_input.clear()
            self.lname_input.clear()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))
            self.db.rollback()

