from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QVBoxLayout

class ShowOrder(QWidget):
    def __init__(self,zakaz,main_window,parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui =loader.load("show_order.ui",self)
        self.main_window = main_window

        layout=QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(self.ui)

        self.ui.label.setText(str(zakaz.id))
        self.ui.label_2.setText(zakaz.status.title)
        self.ui.label_3.setText(f"{zakaz.address.city},{zakaz.address.street}")
        self.ui.label_4.setText(str(zakaz.date_z))
        self.ui.label_5.setText(str(zakaz.data_d))
