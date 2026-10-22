from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from models import create,engine, User, Tovar, Manufactures,Suppliers


class ShowProduct(QWidget):
    def __init__(self, tovar,parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui = loader.load("ShowProduct.ui", self)
        layout=QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.ui)


        if tovar.sale >15:
            self.ui.setStyleSheet('background-color:#008080;')

        if tovar.count == 0:
            self.ui.setStyleSheet('color:grey;')


        self.ui.l_2.setText(tovar.category.title)
        self.ui.l_9.setText(tovar.name)
        self.ui.l_10.setText(tovar.description)
        self.ui.l_11.setText(tovar.manufacture.title)
        self.ui.l_12.setText(tovar.supplier.title)
        if tovar.sale>0 : #& tovar.count>0:
            price_sum=tovar.price-tovar.price*tovar.sale/100.
            self.ui.l_13.setText(f'<span style="color:red;text-decoration: line-through;">{tovar.price:.2f}</span> <span>{price_sum:.2f}<span/>')
        self.ui.l_14.setText(tovar.ed_izm)
        self.ui.l_15.setText(str(tovar.count))
        self.ui.l_16.setText(str(tovar.sale))

        if tovar.photo !='':
             self.ui.l_1.setPixmap(QPixmap('' + tovar.photo))
        else:
            self.ui.l_1.setPixmap(QPixmap('picture.png'))


