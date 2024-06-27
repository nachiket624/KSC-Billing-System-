# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewPyment.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 49, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 131, 16))
        self.nprepayamount = QLabel(Dialog)
        self.nprepayamount.setObjectName(u"nprepayamount")
        self.nprepayamount.setGeometry(QRect(170, 110, 49, 16))
        self.npsubmit = QPushButton(Dialog)
        self.npsubmit.setObjectName(u"npsubmit")
        self.npsubmit.setGeometry(QRect(120, 220, 75, 24))
        self.npuprepayamount = QLabel(Dialog)
        self.npuprepayamount.setObjectName(u"npuprepayamount")
        self.npuprepayamount.setGeometry(QRect(180, 150, 49, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 150, 131, 16))
        self.nppayamount = QDoubleSpinBox(Dialog)
        self.nppayamount.setObjectName(u"nppayamount")
        self.nppayamount.setGeometry(QRect(110, 30, 121, 22))
        self.nppayamount.setMaximum(9999999999.000000000000000)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Repay Amount", None))
        self.nprepayamount.setText(QCoreApplication.translate("Dialog", u"0000", None))
        self.npsubmit.setText(QCoreApplication.translate("Dialog", u"Submit", None))
        self.npuprepayamount.setText(QCoreApplication.translate("Dialog", u"0000", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Updated Repay Amount", None))
    # retranslateUi

