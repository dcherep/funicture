import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from ui_form import Ui_Widget
from sqlalchemy.orm import Session
from models import create,engine, User, Tovar, Manufactures,Suppliers
from login import Login
from show_product import ShowProduct
from add_product import AddProduct
from edit_product import EditProduct
from orders import Orders


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.user =None
        self.window_add=None
        self.window_orders=None

        create()
        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle('Главная')

        self.ui.pushButton.clicked.connect(self.logout)
        self.ui.comboBox.currentIndexChanged.connect(self.load_tovar)
        self.ui.radioButton.toggled.connect(self.load_tovar)
        self.ui.radioButton_2.toggled.connect(self.load_tovar)
        self.ui.radioButton_3.toggled.connect(self.load_tovar)
        self.ui.radioButton_4.toggled.connect(self.load_tovar)
        self.ui.radioButton_5.toggled.connect(self.load_tovar)
        self.ui.lineEdit.textChanged.connect(self.load_tovar)
        self.ui.pushButton_2.clicked.connect(self.show_add)
        self.ui.pushButton_3.clicked.connect(self.show_orders)

    def show_orders(self):
        if self.window_orders is None:
            self.window_orders = Orders(self)
        self.window_orders.show()


    def show_add(self):
        if self.window_add is None:
            self.window_add=AddProduct(self)
        self.window_add.show()


    def load(self):
        self.ui.label.setText(f'{self.user.surname} {self.user.name} {self.user.patr}')
        if self.user.role.id == 1:
            self.ui.groupBox_3.show()
            self.ui.pushButton_2.show()   
            self.ui.pushButton_3.show()
            #self.ui.gridLayout.setColumnStretch(0,0)
        elif self.user.role.id == 2:
            self.ui.groupBox_3.show()
            self.ui.pushButton_2.show()   
            self.ui.pushButton_3.show()
            #$self.ui.gridLayout.setColumnStretch(0,1)
        elif self.user.role.id == 3:
            self.ui.groupBox_2.hide()
            self.ui.gridLayout.setColumnStretch(0,0)
            self.ui.gridLayout.setColumnStretch(1,5)

        self.load_tovar()


    def load_tovar(self):
        layout = self.ui.scrollAreaWidgetContents.layout()
        while layout.count():
            layout.takeAt(0).widget().deleteLater()

        with Session(engine) as db:
            tovars= db.query(Tovar).all()

            if self.ui.comboBox.currentIndex()==1:
                tovars = [t for t in tovars if t.sale < 11]
            elif self.ui.comboBox.currentIndex()==2:
                tovars = [t for t in tovars if t.sale >= 11 and t.sale <15]
            elif self.ui.comboBox.currentIndex()==3:
                tovars = [t for t in tovars if t.sale >= 15]


            if self.ui.radioButton_2.isChecked()==True:
                tovars = sorted(tovars, key=lambda t:t.price)
            elif self.ui.radioButton_3.isChecked()==True:
                tovars = sorted(tovars, key=lambda t:t.price, reverse=True)
            elif self.ui.radioButton_4.isChecked()==True:
                tovars = sorted(tovars, key=lambda t:t.count)
            elif self.ui.radioButton_5.isChecked()==True:
                tovars = sorted(tovars, key=lambda t:t.count, reverse=True)

            search = self.ui.lineEdit.text().strip().lower()
            if len(search)>0:
                tovars = [t for t in tovars if t.articul.lower().find(search) != -1 or t.name.lower().find(search) != -1 or t.description.lower().find(search) != -1]

            for t in tovars:
                tovar= ShowProduct(t,self)
                layout.addWidget(tovar)

            self.ui.label_2.setText(f'Всего: {len(tovars)}')



    def logout(self):
        self.user=None
        login_window.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    login_window =Login(widget)
    login_window.show()
    sys.exit(app.exec())
