# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    font-family: 'Roboto', sans-serif;\n"
"    background-color: #2C2C2C;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    padding: 8px 16px;\n"
"    border-radius: 4px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton.primary {\n"
"    background-color: #007BFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"\n"
"QLineEdit, QTextEdit, QDoubleSpinBox,QSpinBox {\n"
"    border: 1px solid #555555;\n"
"    padding: 8px;\n"
"    border-radius: 4px;\n"
"    background-color: #3C3C3C;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QDoubleSpinBox:focus,QSpinBox:focus {\n"
"    border-color: #007BFF;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,QSpinBox::up-button,QSpinBox::down-button {\n"
"    background-color: #2C2C2C;\n"
"    border: 1px solid #555555;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow,QSpinBox::up-arr"
                        "ow, QSpinBox:down-arrow {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #3C3C3C;\n"
"    border: 1px solid #555555;\n"
"    border-radius: 4px;\n"
"    gridline-color: #555555;\n"
"    color: #FFFFFF;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #4C4C4C;\n"
"    color: #FFFFFF;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #555555;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"    border-bottom: 1px solid #555555;\n"
"}\n"
"\n"
"QTableWidget::item:nth-child(even) {\n"
"    background-color: #2C2C2C;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.abel = QLabel(self.centralwidget)
        self.abel.setObjectName(u"abel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.abel)

        self.mwname = QLineEdit(self.centralwidget)
        self.mwname.setObjectName(u"mwname")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mwname)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.mwphone = QLineEdit(self.centralwidget)
        self.mwphone.setObjectName(u"mwphone")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.mwphone)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.mwemail = QLineEdit(self.centralwidget)
        self.mwemail.setObjectName(u"mwemail")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.mwemail)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.mwaddrest = QTextEdit(self.centralwidget)
        self.mwaddrest.setObjectName(u"mwaddrest")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.mwaddrest)

        self.newcustomerbtn = QPushButton(self.centralwidget)
        self.newcustomerbtn.setObjectName(u"newcustomerbtn")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.newcustomerbtn)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.mwshowid = QLabel(self.centralwidget)
        self.mwshowid.setObjectName(u"mwshowid")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.mwshowid)


        self.verticalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.mwproductname = QLineEdit(self.centralwidget)
        self.mwproductname.setObjectName(u"mwproductname")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.mwproductname)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.mwproductprice = QDoubleSpinBox(self.centralwidget)
        self.mwproductprice.setObjectName(u"mwproductprice")
        self.mwproductprice.setMaximum(9000000000000000.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.mwproductprice)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.mvproductproductquantity = QSpinBox(self.centralwidget)
        self.mvproductproductquantity.setObjectName(u"mvproductproductquantity")
        self.mvproductproductquantity.setMinimum(1)
        self.mvproductproductquantity.setMaximum(100000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.mvproductproductquantity)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.mwproductdiscount = QDoubleSpinBox(self.centralwidget)
        self.mwproductdiscount.setObjectName(u"mwproductdiscount")
        self.mwproductdiscount.setMaximum(100.000000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.mwproductdiscount)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.mvproducttotal = QLineEdit(self.centralwidget)
        self.mvproducttotal.setObjectName(u"mvproducttotal")
        self.mvproducttotal.setInputMethodHints(Qt.ImhDigitsOnly)
        self.mvproducttotal.setReadOnly(True)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.mvproducttotal)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.mwaddtobill = QPushButton(self.centralwidget)
        self.mwaddtobill.setObjectName(u"mwaddtobill")

        self.horizontalLayout.addWidget(self.mwaddtobill)


        self.formLayout_2.setLayout(7, QFormLayout.FieldRole, self.horizontalLayout)

        self.newproduactbtn = QPushButton(self.centralwidget)
        self.newproduactbtn.setObjectName(u"newproduactbtn")

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.newproduactbtn)


        self.verticalLayout.addLayout(self.formLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newrepaymentbtn = QPushButton(self.centralwidget)
        self.newrepaymentbtn.setObjectName(u"newrepaymentbtn")

        self.horizontalLayout_2.addWidget(self.newrepaymentbtn)

        self.mwsavevbill = QPushButton(self.centralwidget)
        self.mwsavevbill.setObjectName(u"mwsavevbill")

        self.horizontalLayout_2.addWidget(self.mwsavevbill)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.total_sum = QLabel(self.centralwidget)
        self.total_sum.setObjectName(u"total_sum")

        self.horizontalLayout_2.addWidget(self.total_sum)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.mwname, self.mwphone)
        QWidget.setTabOrder(self.mwphone, self.mwproductname)
        QWidget.setTabOrder(self.mwproductname, self.mwproductprice)
        QWidget.setTabOrder(self.mwproductprice, self.mvproductproductquantity)
        QWidget.setTabOrder(self.mvproductproductquantity, self.mwproductdiscount)
        QWidget.setTabOrder(self.mwproductdiscount, self.mwaddtobill)
        QWidget.setTabOrder(self.mwaddtobill, self.newrepaymentbtn)
        QWidget.setTabOrder(self.newrepaymentbtn, self.mwsavevbill)
        QWidget.setTabOrder(self.mwsavevbill, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.newproduactbtn)
        QWidget.setTabOrder(self.newproduactbtn, self.mwaddrest)
        QWidget.setTabOrder(self.mwaddrest, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.newcustomerbtn)
        QWidget.setTabOrder(self.newcustomerbtn, self.mvproducttotal)
        QWidget.setTabOrder(self.mvproducttotal, self.mwemail)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.abel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"addreset", None))
        self.newcustomerbtn.setText(QCoreApplication.translate("MainWindow", u"New Customer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.mwshowid.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.mwaddtobill.setText(QCoreApplication.translate("MainWindow", u"Add To Bill", None))
        self.newproduactbtn.setText(QCoreApplication.translate("MainWindow", u"Add New Produact", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Discount", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total", None));
#if QT_CONFIG(tooltip)
        self.tableWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.newrepaymentbtn.setText(QCoreApplication.translate("MainWindow", u"Print Bill", None))
        self.mwsavevbill.setText(QCoreApplication.translate("MainWindow", u"Save Bill", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.total_sum.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

