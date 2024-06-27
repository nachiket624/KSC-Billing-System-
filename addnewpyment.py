import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from NewPyment import Ui_Dialog
import mysql.connector
from PySide6.QtCore import Signal
from utlity.converter import tuple_list

class DialogAddPyment(QtWidgets.QDialog,Ui_Dialog):
    data_sent = Signal(list)
    def __init__(self,senddata):
        self.senddata = senddata
        print("sended data",senddata)
        super(DialogAddPyment, self).__init__()
        self.setupUi(self)
        self.connectToDatabase()
        self.PaymentStatus = "cash"
        self.custloneamount = self.checkLone(str(senddata[0]))
        self.nprepayamount.setText(str(self.custloneamount))
        self.nppayamount.setValue(float(self.senddata[1]))
        self.nppayamount.valueChanged.connect(self.npamountChange)
        self.npsubmit.clicked.connect(self.insertBill)
    def checkLone(self,id):
        query = ("SELECT SUM(LoanAmount) FROM LOANS WHERE CustomerID = " + str(id))
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data = tuple_list(data)
        print("checkLone",data[0])
        return data[0]
    def npamountChange(self):
        amount = float(self.nppayamount.text())

        self.npuprepayamount.setText(str(self.custloneamount))
        self.npUpdateRepay(self.custloneamount,amount)
    def npUpdateRepay(self,loneamount,amount):
        print("amount: ",amount)
        updated_amount = float(self.senddata[1]) + float(loneamount)
        zero_lone = float(amount)-float(loneamount)
        print("updated_amount",updated_amount)
        print("loanamount",loneamount)
        new_repay = amount - self.senddata[1]
        print("new_repay",new_repay)
        if amount > updated_amount:
            print("amount is to high")
            self.npsubmit.setEnabled(False)
        if zero_lone == float(self.senddata[1]):
            self.npsubmit.setEnabled(False)
            print("set lone amount to zero")
            self.PaymentStatus = 'cash'
        if amount > self.senddata[1]:
            self.npsubmit.setEnabled(False)
            print("amount Incress ")
            self.npuprepayamount.setText(str(float(loneamount)-new_repay))
            self.PaymentStatus = 'loan'
        if new_repay < 0:
            self.npsubmit.setEnabled(True)
            print("incress lone")
            self.npuprepayamount.setText(str(float(loneamount) - new_repay))
            self.PaymentStatus = 'loan'

    def insertBill(self):
        PaymentStatus = self.PaymentStatus
        customer_id = str(self.senddata[0])
        TotalAmount = self.senddata[1]
        PaidBill = float(self.nppayamount.text())
        query = "INSERT INTO Bills (CustomerID, TotalAmount,PaidBill, PaymentStatus) VALUES (%s, %s, %s,%s)"
        values = (customer_id, TotalAmount, PaidBill,PaymentStatus)
        try:
            self.cursor.execute(query, values)
            self.db.commit()
            QMessageBox.information(self, "Success", "Bill created successfully.")
            DialogAddPyment.close(self)

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
