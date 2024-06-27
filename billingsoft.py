import sys
import time
from PySide6.QtGui import Qt
from PySide6.QtWidgets import *
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer
from mainwindow import Ui_MainWindow
from addnewcustomer import DialogAddCustmer
from addnewproduact import DialogAddProduact
from addnewpyment import DialogAddPyment
from addnewrepayment import DialogAddRePyment
from utlity.converter import tuple_list
import mysql.connector


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.w = None
        self.w1 = None
        self.setupUi(self)
        self.show_splash_screen()
        self.connectToDatabase()
        self.loadPhoneNo()
        self.loadCustomerNames()
        self.loadProductsNames()
        self.newcustomerbtn.clicked.connect(self.open_newcustomer)
        self.newproduactbtn.clicked.connect(self.open_newproduact)
        self.newrepaymentbtn.clicked.connect(self.open_newrepayment)
        self.mwaddtobill.clicked.connect(self.loadToBillingWindow)
        self.mwsavevbill.clicked.connect(self.open_newpyment)
        self.mwproductname.returnPressed.connect(self.correctProduct)
        self.mwname.textChanged.connect(self.nameChange)
        self.mwphone.textChanged.connect(self.phoneChange)
        self.mwproductdiscount.valueChanged.connect(self.discount_change)
        self.mvproductproductquantity.valueChanged.connect(self.quantity_change)
        self.mwproductprice.valueChanged.connect(self.price_change)

    def show_splash_screen(self):
        app_icon = QPixmap("UI/img/icon.png")
        splash = QSplashScreen(app_icon, Qt.WindowStaysOnTopHint)
        splash.showMessage("Loading...", Qt.AlignCenter | Qt.AlignBottom, Qt.white)
        splash.show()

        time.sleep(3)

    def open_newcustomer(self, checked):
        dialog = DialogAddCustmer()
        dialog.exec()
    def open_newproduact(self, checked):
        dialog = DialogAddProduact()
        dialog.exec()

    def open_newrepayment(self, checked):
        dialog = DialogAddRePyment()
        dialog.exec()

    @Slot()
    def open_newpyment(self):
        custid = int(self.mwshowid.text())
        totalsum = float(self.total_sum.text())
        senddata = [custid,totalsum]
        dialog = DialogAddPyment(senddata)
        dialog.exec()

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

    def loadCustomerNames(self):
        query = "SELECT Name FROM Customers"
        self.cursor.execute(query)
        customer_names = [row[0] for row in self.cursor.fetchall()]
        completer = QCompleter(customer_names)
        self.mwname.setCompleter(completer)

    def nameChange(self):
        if " " in self.mwname.text():
            customer_name = self.mwname.text()
            self.mwemail.clear()
            self.mwaddrest.clear()
            query = ("SELECT name,Email,Phone,Address,CustomerID FROM Customers where Name = '"+customer_name+"'" )
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            data = tuple_list(data)
            self.mwname.setText(str(data[0]))
            self.mwphone.setText(str(data[2]))
            self.mwemail.setText(str(data[1]))
            self.mwaddrest.setText(str(data[3]))
            self.mwshowid.setText(str(data[4]))

    def loadPhoneNo(self):
        query = "SELECT Phone FROM Customers"
        self.cursor.execute(query)
        customer_phone_no = [row[0] for row in self.cursor.fetchall()]
        completer = QCompleter(customer_phone_no)
        self.mwphone.setCompleter(completer)

    def phoneChange(self):
        if len(self.mwphone.text()) == 10:
            customer_phone_no = self.mwphone.text()
            self.mwname.clear()
            self.mwemail.clear()
            self.mwaddrest.clear()
            query = ("SELECT name,Email,Phone,Address,CustomerID FROM Customers where Phone = " + customer_phone_no)
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            data = tuple_list(data)
            self.mwname.setText(str(data[0]))
            self.mwphone.setText(str(data[2]))
            self.mwemail.setText(str(data[1]))
            self.mwaddrest.setText(str(data[3]))
            self.mwshowid.setText(str(data[4]))
    def loadToBillingWindow(self):
        myheader = ['Item', 'Discount', 'Quantity', 'Total']
        self.tableWidget.setHorizontalHeaderLabels(myheader)
        item_name = self.mwproductname.text()
        item_price = self.mvproducttotal.text()
        item_quantity = self.mvproductproductquantity.text()
        total_price = float(self.mwproductprice.text()) * int(self.mvproductproductquantity.text())
        discount = (float(self.mwproductdiscount.text()) * total_price) / 100
        if len(self.mwproductname.text()) > 0 and float(self.mwproductprice.text()) > 0:
            items = [item_name, str(discount),item_quantity, item_price ]
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for col, value in enumerate(items):
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(value))
        else:
            # todo: add message box
            print('invalid value')
        self.calculate_total()

    # todo: change formula according
    def discount_change(self):
        print("cal_discount")
        total_price = float(self.mwproductprice.text())*int(self.mvproductproductquantity.text())
        discount = (float(self.mwproductdiscount.text())*total_price)/100
        total = total_price-discount
        self.mvproducttotal.setText(str(total))

    def price_change(self):
        print("price change")
        total_price = float(self.mwproductprice.text())*int(self.mvproductproductquantity.text())
        self.mvproducttotal.setText(str(total_price))

    def quantity_change(self):
        print('quantity_change')
        total_price = float(self.mwproductprice.text()) * int(self.mvproductproductquantity.text())
        self.mvproducttotal.setText(str(total_price))


    def loadProductsNames(self):
        query = "SELECT Name FROM products"
        self.cursor.execute(query)
        customer_names = [row[0] for row in self.cursor.fetchall()]
        completer = QCompleter(customer_names)
        self.mwproductname.setCompleter(completer)

    def correctProduct(self):
        produact_name = self.mwproductname.text()
        self.mwproductprice.setValue(0)
        self.mvproductproductquantity.setValue(1)
        self.mwproductdiscount.setValue(0)
        self.mvproducttotal.clear()
        query = ("select Price From products where name =  '"+produact_name+"'")
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data = tuple_list(data)
        self.mwproductprice.setValue(data[0])

    def calculate_total(self):
        total = 0.0
        column_index = 3  # Index of the column to sum (Price column)

        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, column_index)
            if item is not None:
                try:
                    value = float(item.text())
                    total += value
                except ValueError:
                    pass  # Ignore cells that don't contain a valid number

        self.total_sum.setText(f"{total:.2f}")


    def create_bill(self):
        self.mwshowid.text()
        self.total_sum.text()

        customer_id, ok = QInputDialog.getInt(self, "Customer ID", "Enter Customer ID:")
        if ok:
            total_amount, ok = QInputDialog.getDouble(self, "Total Amount", "Enter Total Amount:")
            if ok:
                payment_status, ok = QInputDialog.getItem(self, "Payment Status", "Select Payment Status:",
                                                          ["Paid", "On Loan"], 0, False)
                if ok:
                    query = "INSERT INTO Bills (CustomerID, TotalAmount, PaymentStatus) VALUES (%s, %s, %s)"
                    values = (customer_id, total_amount, payment_status)

                    try:
                        self.cursor.execute(query, values)
                        self.db.commit()
                        QMessageBox.information(self, "Success", "Bill created successfully.")
                    except mysql.connector.Error as err:
                        QMessageBox.critical(self, "Database Error", str(err))
                        self.db.rollback()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
