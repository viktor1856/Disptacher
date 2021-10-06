from PyQt5.QtWidgets import QDialog
from customerListForm import Ui_customers
from dbClass import SqlLiteDb

class ListCustomersClass(QDialog, Ui_customers):
    def __init__(self, data_base_connection):
        super().__init__()
        self.setupUi(self)
        self.connect_db = data_base_connection
        customers_list = self.connect_db.select_all_customers()
        print(customers_list)
        self.listCustomers.addItems(customers_list)


