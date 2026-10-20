import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from sqlalchemy.orm import Session
from models import create,engine
from login import Login


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.user =None
        create()
        self.ui.pushButton.clicked.connect(self.logout)

    def load(self):
        self.ui.label.setText(f'{self.user}')
        if self.user.role.id == 1:
            pass
        elif self.user.role.id == 2:
            pass
        elif self.user.role.id == 3:
            self.ui.groupBox_2.hide()
            self.ui.gridLayout.setColumnStretch(0,0)
            self.ui.gridLayout.setColumnStretch(1,5)


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
