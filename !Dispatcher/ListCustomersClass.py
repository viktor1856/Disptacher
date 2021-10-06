from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from customerListForm import Ui_customers


class ListCustomersClass(QDialog, Ui_customers):
    def __init__(self, data_base_connection):
        super().__init__()
        self.setupUi(self)
        self.connect_db = data_base_connection
        self.refresh_table()
        self.insertCustomer.clicked.connect(self.insert_new_customer)

    def insert_new_customer(self):
        self.connect_db.insert_new_customer(self.lineEdit.text())
        self.lineEdit.clear()
        self.refresh_table()

    def refresh_table(self):
        try:
            all_customers = self.connect_db.select_all_customers()
            row_customers = 0
            self.listCustomers.setRowCount(len(all_customers))
            for customer in all_customers:
                # print(driver)
                self.listCustomers.setItem(row_customers, 0, QTableWidgetItem(str(customer[0])))
                self.listCustomers.setItem(row_customers, 1, QTableWidgetItem(str(customer[1])))
                row_customers += 1
            # таблица не изменяемая и только для чтения
            self.listCustomers.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # вибирать только строки
            self.listCustomers.setSelectionBehavior(QAbstractItemView.SelectRows)

            # выравнивание столбцов по содержимому
            self.listCustomers.resizeColumnsToContents()
            self.listCustomers.resizeRowsToContents()

        except Exception as e:
            print(str(e))
            QMessageBox.error(self,
                              "Ошибка списка заказчиков",
                              "При формировании списка произошла ошибка\n" + str(e),
                              QMessageBox.Ok)


