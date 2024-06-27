import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog
from NewProduact import Ui_Dialog
import mysql.connector


class DialogAddProduact(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogAddProduact, self).__init__()
        self.setupUi(self)
        self.connectToDatabase()
        self.dbaddproduact.clicked.connect(self.add_product)


    def add_product(self):
        product_name = self.product_name.text()
        description = self.description.text()
        price = self.price.text()

        query = "INSERT INTO Products (Name, Description, Price) VALUES (%s, %s, %s)"
        values = (product_name, description, price)

        try:
            self.cursor.execute(query, values)
            self.db.commit()
            QMessageBox.information(self, "Success", "Product added successfully.")
            self.product_name.clear()
            self.description.clear()
            self.price.clear()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))
            self.db.rollback()

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
            QMessageBox.critical(self, "Database Connection Error", str(err))
            sys.exit(1)
