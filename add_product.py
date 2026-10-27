import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from sqlalchemy.orm import Session
from PySide6.QtGui import QIcon, QPixmap
from models import *

class AddProduct(QWidget):
    def __init__(self, main_window,tovar=None,parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui = loader.load("add_product.ui", self)
        self.main_window = main_window
        self.setWindowTitle('Добавить товар')
        self.setWindowIcon(QIcon('icon.ico'))
        self.tovar=tovar
        self.load_combo_box()
        self.load_tovar()
        self.ui.pushButton.clicked.connect(self.back_to_main)
        self.ui.pushButton_3.clicked.connect(self.cancel)
        self.ui.pushButton_2.clicked.connect(self.save)
        self.ui.pushButton_4.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", '.' , "Изображение (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            file_name = os.path.basename(file_path)
            self.ui.lineEdit_4.setText(file_name)
            self.load_image()

    def load_image(self):
        file_path = self.ui.lineEdit_4.text().strip()
        if not file_path:
            self.ui.label_13.setText("Поле ввода пустое!")
            return
        file_path = '' + file_path
        if not os.path.exists(file_path):
            self.ui.label_13.setText("Файл не найден! Проверьте путь.")
            return
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            self.ui.label_13.setText("Не удалось загрузить изображение. \nНеверный формат или битый файл.")
        else:
            self.ui.label_13.setPixmap(pixmap)

    def load_tovar(self):
        if self.tovar != None:
            self.ui.lineEdit_2.setText(self.tovar.name)
            self.ui.comboBox.setCurrentIndex(self.ui.comboBox.findData(self.tovar.category.id))
            self.ui.textEdit.setText(self.tovar.description)
            self.ui.comboBox_2.setCurrentIndex(self.ui.comboBox_2.findData(self.tovar.manufacture.id))
            self.ui.comboBox_3.setCurrentIndex(self.ui.comboBox_3.findData(self.tovar.supplier.id))
            self.ui.doubleSpinBox.setValue(self.tovar.price)
            self.ui.lineEdit_3.setText(self.tovar.ed_izm)
            self.ui.spinBox.setValue(self.tovar.count)
            self.ui.doubleSpinBox_2.setValue(self.tovar.sale)
            self.ui.lineEdit_4.setText(self.tovar.photo)
            self.load_image()

    def save(self):
        if self.check() == False: return
        with Session(engine) as db:
            if self.tovar is None:
                new_tovar= Tovar(
                articul=self.ui.lineEdit.text(),
                name= self.ui.lineEdit_2.text(),
                category_id= int(self.ui.comboBox.currentData()),
                description= self.ui.textEdit.toPlainText(),
                manufactures_id= int(self.ui.comboBox_2.currentData()),
                supplier_id= int(self.ui.comboBox_3.currentData()),
                price= self.ui.doubleSpinBox.value(),
                ed_izm= self.ui.lineEdit_3.text(),
                count= self.ui.spinBox.value(),
                sale= self.ui.doubleSpinBox_2.value(),
                photo= self.ui.lineEdit_4.text()

                )
                db.add(new_tovar)
            else:
                t=db.merge(db.get(Tovar,self.tovar.id))
                t.articul=self.ui.lineEdit.text(),
                t.name= self.ui.lineEdit_2.text(),
                t.category_id= int(self.ui.comboBox.currentData()),
                t.description= self.ui.textEdit.toPlainText(),
                t.manufactures_id= int(self.ui.comboBox_2.currentData()),
                t.supplier_id= int(self.ui.comboBox_3.currentData()),
                t.price= float(self.ui.doubleSpinBox.value()),
                t.ed_izm= self.ui.lineEdit_3.text(),
                t.count= self.ui.spinBox.value(),
                t.sale= float(self.ui.doubleSpinBox_2.value()),
                t.photo= self.ui.lineEdit_4.text()
            db.commit()
        self.main_window.load_tovar()

    def load_combo_box(self):
        with Session(engine) as db:
            categories = db.query(Category).all()
            for cat in categories:
                self.ui.comboBox.addItem(cat.title, cat.id)

            manufactures = db.query(Manufactures).all()
            for man in manufactures:
                self.ui.comboBox_2.addItem(man.title, man.id)

            suppliers = db.query(Suppliers).all()
            for sup in suppliers:
                self.ui.comboBox_3.addItem(sup.title, sup.id)

    def check(self):
        msg=QMessageBox(self)
        if self.ui.lineEdit.text().strip() == '':
            msg.setText('Введите артикул')
            msg.exec()
            self.ui.lineEdit.setFocus()
            return False
        elif self.ui.lineEdit_2.text().strip() == '':
            msg.setText('Введите название')
            msg.exec()
            self.ui.lineEdit_2.setFocus()
            return False
        elif self.ui.lineEdit_3.text().strip() == '':
            msg.setText('Введите единицу измерения')
            msg.exec()
            self.ui.lineEdit_3.setFocus()
            return False
        elif self.ui.textEdit.toPlainText().strip() == '':
            msg.setText('Введите описание')
            msg.exec()
            self.ui.textEdit.setFocus()
            return False
        elif self.ui.doubleSpinBox.text().strip() == '':
            msg.setText('Введите цену')
            msg.exec()
            self.ui.doubleSpinBox.setFocus()
            return False
        elif self.ui.doubleSpinBox_2.text().strip() == '':
            msg.setText('Введите скидку')
            msg.exec()
            self.ui.doubleSpinBox_2.setFocus()
            return False
        elif self.ui.spinBox.text().strip() == '':
            msg.setText('Введите количество')
            msg.exec()
            self.ui.spinBox.setFocus()
            return False


    def back_to_main(self):
        self.close()
        self.main_window.show()

    def cancel(self):
        reply =QMessageBox.question(self, "Подтверждение", "Вы уверены, что хотите закрыть окно?",QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.back_to_main()

