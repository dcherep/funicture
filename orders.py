from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from sqlalchemy.orm import Session
from models import *
from show_order import ShowOrder

class Orders(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui = loader.load("orders.ui", self)
        self.main_window=main_window
        self.setWindowTitle('Заказы')
        self.setWindowIcon(QIcon('icon.ico'))

        self.ui.pushButton.clicked.connect(self.back_to_main)
        #self.ui.pushButton_2.clicked.connect(self.show_add_order)

        if self.main_window.user.role.id != 1: 
            self.ui.pushButton_2.hide()

        self.load_products()

    def back_to_main(self):
        self.main_window.show()  
        self.close()   
         

    def load_products(self):
        layout=self.ui.scrollAreaWidgetContents.layout()
        while layout.count():
            layout.takeAt(0).widget().deleteLater()

        with Session(engine) as db:
            orders = db.query(Zakaz).all()
            for o in orders:
                order =ShowOrder(o,self)
                layout.addWidget(order)
