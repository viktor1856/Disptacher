from FixedDriverForm import Ui_FixedDriverList
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox


class FixedDriverClass(QDialog, Ui_FixedDriverList):
    def __init__(self, data_base_connection):
        super().__init__()
        self.db_connection = data_base_connection
        self.setupUi(self)