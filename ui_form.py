# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(973, 526)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(670, 10, 181, 16))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(870, 10, 75, 24))

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.groupBox_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 648, 414))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 10, 141, 58))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 70, 261, 160))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButton = QRadioButton(self.groupBox_5)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_5)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_5)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_5)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_4.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox_5)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_4.addWidget(self.radioButton_5)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 420, 101, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 240, 251, 61))
        self.lineEdit = QLineEdit(self.groupBox_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 231, 24))
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 320, 251, 24))
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 350, 251, 26))

        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 2)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Widget", u"\u0424\u0418\u041e", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"\u0412\u0441\u0435 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u044b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"0-10.99%", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"11-14.99%", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"15% \u0438 \u0431\u043e\u043b\u0435\u0435", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("Widget", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"\u0411\u0435\u0437 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c(\u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e)", None))
        self.radioButton_3.setText(QCoreApplication.translate("Widget", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c(\u043f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e)", None))
        self.radioButton_4.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e(\u043f\u043e \u0432\u043e\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044e)", None))
        self.radioButton_5.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e(\u043f\u043e \u0443\u0431\u044b\u0432\u0430\u043d\u0438\u044e)", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0412\u0441\u0435\u0433\u043e:", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Widget", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043a\u0430\u0437\u044b", None))
    # retranslateUi

