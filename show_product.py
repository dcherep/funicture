from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from models import create,engine, User, Tovar, Manufactures,Suppliers
from add_product import AddProduct
from edit_product import EditProduct


class ShowProduct(QWidget):
    def __init__(self, tovar, main_window,parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui = loader.load("ShowProduct.ui", self)
        self.main_window = main_window
        self.tovar = tovar
        self.edit_window=None

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
        if tovar.sale>0 :
            price_sum=tovar.price-tovar.price*tovar.sale/100.
            self.ui.l_13.setText(f'<span style="color:red;text-decoration: line-through;">{tovar.price:.2f}</span> <span>{price_sum:.2f}<span/>')
        self.ui.l_14.setText(tovar.ed_izm)
        self.ui.l_15.setText(str(tovar.count))
        self.ui.l_16.setText(str(tovar.sale))

        if tovar.photo !='':
             self.ui.l_1.setPixmap(QPixmap('' + tovar.photo))
        else:
            self.ui.l_1.setPixmap(QPixmap('picture.png'))

        self.ui.pushButton_2.clicked.connect(self.show_edit)
        self.ui.pushButton.clicked.connect(self.delete)

    def show_edit(self):
        if self.edit_window is None:
            self.edit_window=EditProduct(self.main_window,self.tovar)
        self.edit_window.show()

    def delete(self):
        reply = QMessageBox.question(
            self, 
            "Подтверждение", 
            f"Вы уверены, что хотите удалить товар:\n«{self.tovar.name}»?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            from sqlalchemy.orm import Session
            from models import engine, Tovar

            with Session(engine) as db:
                t = db.get(Tovar, self.tovar.id)
                if t:
                    db.delete(t)
                    db.commit()
            
            self.main_window.load_tovar()
            self.close()





