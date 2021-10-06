from PyQt5.QtWidgets import QDialog
from customerListForm import Ui_customers


class ListCustomersClass(QDialog, Ui_customers):
    def __init__(self, data_base_connection):
        super().__init__()
        self.setupUi(self)
        self.connect_db = data_base_connection

