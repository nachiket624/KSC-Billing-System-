import sys
from PySide6.QtWidgets import *
from PySide6 import QtWidgets
from NewRePayment import Ui_Dialog
import mysql.connector
from utlity.converter import tuple_list

class DialogAddRePyment(QtWidgets.QDialog,Ui_Dialog):
    def __init__(self):
        super(DialogAddRePyment, self).__init__()
        self.setupUi(self)
        self.connectToDatabase()
        self.loadPhoneNo()
        self.loadCustomerNames()
        self.nrpname.textChanged.connect(self.nameChange)
        self.nrpphone.textChanged.connect(self.phoneChange)
        self.nrpamount.valueChanged.connect(self.nrpamountChage)
        self.nrpsubmit.clicked.connect(self.insertRepayment)


    def loadCustomerNames(self):
        query = "SELECT Name FROM Customers"
        self.cursor.execute(query)
        customer_names = [row[0] for row in self.cursor.fetchall()]
        completer = QCompleter(customer_names)
        self.nrpname.setCompleter(completer)

    def nameChange(self):
        if " " in self.nrpname.text():
            customer_name = self.nrpname.text()
            query = ("SELECT name,Phone,CustomerID FROM Customers where Name = '" + customer_name + "'")
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            data = tuple_list(data)
            print(data)
            self.nrpname.setText(str(data[0]))
            self.nrpphone.setText(str(data[1]))
            self.nrpshowid.setText(str(data[2]))
            self.updateRepayment()

    def loadPhoneNo(self):
        query = "SELECT Phone FROM Customers"
        self.cursor.execute(query)
        customer_phone_no = [row[0] for row in self.cursor.fetchall()]
        completer = QCompleter(customer_phone_no)
        self.nrpphone.setCompleter(completer)

    def phoneChange(self):
        if len(self.nrpphone.text()) == 10:
            customer_phone_no = self.nrpphone.text()
            query = ("SELECT name,Phone,CustomerID FROM Customers where Phone = " + customer_phone_no)
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            data = tuple_list(data)
            self.nrpname.setText(str(data[0]))
            self.nrpphone.setText(str(data[1]))
            self.nrpshowid.setText(str(data[2]))
            self.updateRepayment()

    def getLoanByID(self,cust_id) -> []:
        query = ("SELECT LoanID,LoanAmount FROM loans where CustomerID = '" + cust_id + "'")
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data = tuple_list(data)
        print("getLoanByID",data)
        return data

    def updateRepayment(self):
        custid = self.nrpshowid.text()
        data = self.getLoanByID(custid)
        self.nrploanid.setText(str(data[0]))
        self.nrpremaninamount.setText(str(data[1]))


    def nrpamountChage(self):
        custid = self.nrpshowid.text()
        data = self.getLoanByID(custid)
        amount = float(self.nrpamount.text())
        remaning = float(data[1])-amount
        if remaning < 0:
            self.nrpsubmit.setEnabled(False)
        else:
            self.nrpsubmit.setEnabled(True)
            self.nrpremaninamount.setText(str(remaning))
        self.nrpremaninamount.setText(str(remaning))

    def insertRepayment(self):
        loanid = self.nrploanid.text()
        amount = float(self.nrpamount.text())
        query = "INSERT INTO repayments(LoanID, RepaymentAmount) VALUES (%s, %s)"
        values = (loanid,amount)
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            QMessageBox.information(self, "Success", "RePayment successfull.")
            DialogAddRePyment.close(self)

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