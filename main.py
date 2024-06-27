import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,
                               QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QInputDialog)
import mysql.connector


class BillingSoftware(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Billing Software")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()
        self.connectToDatabase()

    def initUI(self):
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()

        self.name_label = QLabel("Customer Name:")
        self.name_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()

        self.address_label = QLabel("Address:")
        self.address_input = QLineEdit()

        self.add_button = QPushButton("Add Customer")
        self.add_button.clicked.connect(self.add_customer)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.phone_label)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.address_label)
        self.layout.addWidget(self.address_input)
        self.layout.addWidget(self.add_button)

        self.bill_button = QPushButton("Create Bill")
        self.bill_button.clicked.connect(self.create_bill)
        self.layout.addWidget(self.bill_button)

        self.view_history_button = QPushButton("View Purchase History")
        self.view_history_button.clicked.connect(self.view_purchase_history)
        self.layout.addWidget(self.view_history_button)

        self.payment_button = QPushButton("Add Payment")
        self.payment_button.clicked.connect(self.add_payment)
        self.layout.addWidget(self.payment_button)

        self.add_loan_button = QPushButton("Add Loan")
        self.add_loan_button.clicked.connect(self.add_loan)
        self.layout.addWidget(self.add_loan_button)

        self.view_loan_history_button = QPushButton("View Loan History")
        self.view_loan_history_button.clicked.connect(self.view_loan_history)
        self.layout.addWidget(self.view_loan_history_button)

        self.main_widget.setLayout(self.layout)

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

    def add_customer(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        address = self.address_input.text()

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
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", str(err))
            self.db.rollback()

    def create_bill(self):
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

    def view_purchase_history(self):
        customer_id, ok = QInputDialog.getInt(self, "Customer ID", "Enter Customer ID:")
        if ok:
            query = """
                SELECT Bills.BillID, Bills.Date, Bills.TotalAmount, Bills.PaymentStatus
                FROM Bills
                WHERE Bills.CustomerID = %s
            """
            self.cursor.execute(query, (customer_id,))
            bills = self.cursor.fetchall()

            if bills:
                history_window = QWidget()
                history_layout = QVBoxLayout()
                table = QTableWidget()
                table.setRowCount(len(bills))
                table.setColumnCount(4)
                table.setHorizontalHeaderLabels(["Bill ID", "Date", "Total Amount", "Payment Status"])

                for i, (bill_id, date, total_amount, payment_status) in enumerate(bills):
                    table.setItem(i, 0, QTableWidgetItem(str(bill_id)))
                    table.setItem(i, 1, QTableWidgetItem(str(date)))
                    table.setItem(i, 2, QTableWidgetItem(str(total_amount)))
                    table.setItem(i, 3, QTableWidgetItem(str(payment_status)))

                history_layout.addWidget(table)
                history_window.setLayout(history_layout)
                history_window.setWindowTitle("Purchase History")
                history_window.setGeometry(200, 200, 600, 400)
                history_window.show()
            else:
                QMessageBox.information(self, "No History", "No purchase history found for this customer.")

    def add_payment(self):
        customer_id, ok = QInputDialog.getInt(self, "Customer ID", "Enter Customer ID:")
        if ok:
            bill_id, ok = QInputDialog.getInt(self, "Bill ID", "Enter Bill ID:")
            if ok:
                amount, ok = QInputDialog.getDouble(self, "Payment Amount", "Enter Payment Amount:")
                if ok:
                    payment_method, ok = QInputDialog.getText(self, "Payment Method", "Enter Payment Method:")
                    if ok:
                        query = "INSERT INTO Payments (CustomerID, BillID, Amount, PaymentMethod) VALUES (%s, %s, %s, %s)"
                        values = (customer_id, bill_id, amount, payment_method)

                        try:
                            self.cursor.execute(query, values)
                            self.db.commit()
                            # Update bill payment status if full amount paid
                            self.cursor.execute("SELECT SUM(Amount) FROM Payments WHERE BillID = %s", (bill_id,))
                            total_paid = self.cursor.fetchone()[0]
                            self.cursor.execute("SELECT TotalAmount FROM Bills WHERE BillID = %s", (bill_id,))
                            total_amount = self.cursor.fetchone()[0]
                            if total_paid >= total_amount:
                                self.cursor.execute("UPDATE Bills SET PaymentStatus = 'Paid' WHERE BillID = %s",
                                                    (bill_id,))
                                self.db.commit()
                            QMessageBox.information(self, "Success", "Payment added successfully.")
                        except mysql.connector.Error as err:
                            QMessageBox.critical(self, "Database Error", str(err))
                            self.db.rollback()

    def add_loan(self):
        customer_id, ok = QInputDialog.getInt(self, "Customer ID", "Enter Customer ID:")
        if ok:
            bill_id, ok = QInputDialog.getInt(self, "Bill ID", "Enter Bill ID:")
            if ok:
                loan_amount, ok = QInputDialog.getDouble(self, "Loan Amount", "Enter Loan Amount:")
                if ok:
                    due_date, ok = QInputDialog.getText(self, "Due Date", "Enter Due Date (YYYY-MM-DD):")
                    if ok:
                        query = "INSERT INTO Loans (CustomerID, BillID, LoanAmount, DueDate) VALUES (%s, %s, %s, %s)"
                        values = (customer_id, bill_id, loan_amount, due_date)

                        try:
                            self.cursor.execute(query, values)
                            self.db.commit()
                            QMessageBox.information(self, "Success", "Loan added successfully.")
                        except mysql.connector.Error as err:
                            QMessageBox.critical(self, "Database Error", str(err))
                            self.db.rollback()

    def view_loan_history(self):
        customer_id, ok = QInputDialog.getInt(self, "Customer ID", "Enter Customer ID:")
        if ok:
            query = """
                SELECT Loans.LoanID, Loans.BillID, Loans.LoanAmount, Loans.LoanDate, Loans.DueDate
                FROM Loans
                WHERE Loans.CustomerID = %s
            """
            self.cursor.execute(query, (customer_id,))
            loans = self.cursor.fetchall()

            if loans:
                loan_history_window = QWidget()
                loan_history_layout = QVBoxLayout()
                table = QTableWidget()
                table.setRowCount(len(loans))
                table.setColumnCount(5)
                table.setHorizontalHeaderLabels(["Loan ID", "Bill ID", "Loan Amount", "Loan Date", "Due Date"])

                for i, (loan_id, bill_id, loan_amount, loan_date, due_date) in enumerate(loans):
                    table.setItem(i, 0, QTableWidgetItem(str(loan_id)))
                    table.setItem(i, 1, QTableWidgetItem(str(bill_id)))
                    table.setItem(i, 2, QTableWidgetItem(str(loan_amount)))
                    table.setItem(i, 3, QTableWidgetItem(str(loan_date)))
                    table.setItem(i, 4, QTableWidgetItem(str(due_date)))

                loan_history_layout.addWidget(table)
                loan_history_window.setLayout(loan_history_layout)
                loan_history_window.setWindowTitle("Loan History")
                loan_history_window.setGeometry(200, 200, 600, 400)
                loan_history_window.show()
            else:
                QMessageBox.information(self, "No History", "No loan history found for this customer.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BillingSoftware()
    window.show()
    sys.exit(app.exec())
