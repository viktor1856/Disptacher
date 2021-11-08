from FixedDriverForm import Ui_FixedDriverList
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from AddFixDriverClass import AddFixDriverClass


class FixedDriverClass(QDialog, Ui_FixedDriverList):
    def __init__(self, data_base_connection):
        super().__init__()
        self.db_connection = data_base_connection
        self.setupUi(self)
        self.insertFixedDriver.clicked.connect(self.new_form_insert_fixed_driver)
        self.refresh_table()

    def new_form_insert_fixed_driver(self):
        try:
            form = AddFixDriverClass(self.db_connection)
            if form.exec_() == form.Accepted:
                self.refresh_table()
        except Exception as e:
            print('Error: FixedDriverClass->new_form_insert_fixed_driver() ' + str(e))

    def refresh_table(self):
        try:
            all_fixed_drivers = self.db_connection.select_all_fixed_drivers()
            row_driver = 0
            self.fixedDriverTable.setRowCount(len(all_fixed_drivers))
            for fix_driver in all_fixed_drivers:
                #print(driver)
                self.fixedDriverTable.setItem(row_driver, 0, QTableWidgetItem(str(fix_driver[0])))
                # self.fixedDriverTable.setItem(row_driver, 1, QTableWidgetItem(fix_driver[1]+' '+fix_driver[2]+' '+fix_driver[3]))
                # self.fixedDriverTable.setItem(row_driver, 2, QTableWidgetItem(fix_driver[4]))
                row_driver += 1
            #таблица не изменяемая и только для чтения
            self.fixedDriverTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # вибирать только строки
            self.fixedDriverTable.setSelectionBehavior(QAbstractItemView.SelectRows)

            #выравнивание столбцов по содержимому
            self.fixedDriverTable.resizeColumnsToContents()
            self.fixedDriverTable.resizeRowsToContents()

        except Exception as e:
            print('Error: FixedDriverClass->refresh_table() ' + str(e))
            QMessageBox.error(self,
            "Ошибка списка закрепления водителей",
            "При формировании списка произошла ошибка\n"+str(e),
            QMessageBox.Ok)
