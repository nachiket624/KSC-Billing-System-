# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewRePayment.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(478, 210)
        Dialog.setStyleSheet(u"QLabel{\n"
"	font: 12pt \"Arial\";\n"
"}\n"
"QLineEdit{\n"
"	font: 12pt \"Verdana\";\n"
"	\n"
"}\n"
"QPushButton{\n"
"border-radius: 10px;\n"
"	background-color: rgb(0, 255, 30);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 10px;\n"
"	background-color: rgb(255, 0, 0)\n"
"}")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.nrpname = QLineEdit(Dialog)
        self.nrpname.setObjectName(u"nrpname")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nrpname)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.nrpphone = QLineEdit(Dialog)
        self.nrpphone.setObjectName(u"nrpphone")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nrpphone)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label)

        self.nrpamount = QDoubleSpinBox(Dialog)
        self.nrpamount.setObjectName(u"nrpamount")
        self.nrpamount.setMaximum(999999999999.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.nrpamount)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.nrpremaninamount = QLabel(Dialog)
        self.nrpremaninamount.setObjectName(u"nrpremaninamount")
        self.nrpremaninamount.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.nrpremaninamount)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.nrpshowid = QLabel(Dialog)
        self.nrpshowid.setObjectName(u"nrpshowid")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nrpshowid)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.nrploanid = QLabel(Dialog)
        self.nrploanid.setObjectName(u"nrploanid")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nrploanid)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.nrpsubmit = QPushButton(Dialog)
        self.nrpsubmit.setObjectName(u"nrpsubmit")
        self.nrpsubmit.setMinimumSize(QSize(70, 30))

        self.horizontalLayout.addWidget(self.nrpsubmit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Phone No:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Remaning Amount", None))
        self.nrpremaninamount.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.nrpshowid.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Loan ID", None))
        self.nrploanid.setText("")
        self.nrpsubmit.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

