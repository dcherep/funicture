# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(973, 672)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")

        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")

        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"GroupBox", None))
    # retranslateUi

