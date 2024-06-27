# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewProduact.ui'
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
        Dialog.resize(319, 266)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.product_name = QLineEdit(Dialog)
        self.product_name.setObjectName(u"product_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.product_name)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.description = QLineEdit(Dialog)
        self.description.setObjectName(u"description")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.description)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.price = QLineEdit(Dialog)
        self.price.setObjectName(u"price")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.price)

        self.dbaddproduact = QPushButton(Dialog)
        self.dbaddproduact.setObjectName(u"dbaddproduact")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dbaddproduact)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Produact Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Description ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.dbaddproduact.setText(QCoreApplication.translate("Dialog", u"Add", None))
    # retranslateUi

