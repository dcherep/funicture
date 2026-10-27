# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_product.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(371, 501)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 13, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 11, 1, 1, 1)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 15, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 13, 1, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 14, 0, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 18, 1, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 7, 1, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 6, 1, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 11, 0, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 16, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 18, 3, 1, 1)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 10, 1, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 8, 1, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.doubleSpinBox = QDoubleSpinBox(Form)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout.addWidget(self.doubleSpinBox, 12, 1, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(Form)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout.addWidget(self.doubleSpinBox_2, 15, 1, 1, 1)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 14, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 16, 1, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 9, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0438\u0434\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0445\u0430\u0434", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0442\u043e \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0410\u0440\u0442\u0438\u043a\u0443\u043b", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
    # retranslateUi

