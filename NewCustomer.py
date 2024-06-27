# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewCustomer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(507, 291)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name_input = QLineEdit(Dialog)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setInputMethodHints(Qt.ImhPreferLowercase)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_input)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lname_input = QLineEdit(Dialog)
        self.lname_input.setObjectName(u"lname_input")
        self.lname_input.setInputMethodHints(Qt.ImhPreferLowercase)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lname_input)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.phone_input = QLineEdit(Dialog)
        self.phone_input.setObjectName(u"phone_input")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.phone_input)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.email_input = QLineEdit(Dialog)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setInputMethodHints(Qt.ImhPreferLowercase)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.email_input)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.address_input = QLineEdit(Dialog)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setMinimumSize(QSize(0, 100))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.address_input)

        self.dbaddcust = QPushButton(Dialog)
        self.dbaddcust.setObjectName(u"dbaddcust")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.dbaddcust)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Frist Name", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"email", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Addreset", None))
        self.dbaddcust.setText(QCoreApplication.translate("Dialog", u"ADD", None))
    # retranslateUi

