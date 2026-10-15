import sys

from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from sqlalchemy.orm import Session
from models import create,engine


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        create()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
