#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     10.09.2021
# Copyright:   (c) Admin 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from listDriverForm import Ui_listDriverForm
from NewDriverClass import NewDriverClass
from PyQt5.QtWidgets import QDialog, QTableWidgetItem,QAbstractItemView,QMessageBox


class ListDriverClass(QDialog, Ui_listDriverForm):
    def __init__(self, data_base_connection):
        super().__init__()
        self.db_connection = data_base_connection
        self.setupUi(self)
        # сигнал двойного нажатия на строку таблицы
        # self.tableDriver.itemDoubleClicked.connect(self.newDriverForm)

        self.newDriver.clicked.connect(self.new_driver_form)
        self.deleteDriver.clicked.connect(self.delete_driver)
        self.editDriver.clicked.connect(self.edit_driver)
        self.refresh_table()

    def edit_driver(self):
        try:
            id_driver = int(self.tableDriver.model().index(self.tableDriver.currentIndex().row(), 0).data())
            form = NewDriverClass(self.db_connection, id_driver=id_driver)
            if form.exec_() == form.Accepted:
                self.refresh_table()
        except Exception as e:
            print('edit_driver ' + str(e))

    def delete_driver(self):
        try:
            id_driver = self.tableDriver.model().index(self.tableDriver.currentIndex().row(), 0).data()
            if int(id_driver) > 0:
                if QMessageBox.warning(self,
                                  "Удаление водителя",
                                  "Вы уверены что хотите удалить водителя?\n"+
                                self.tableDriver.model().index(self.tableDriver.currentIndex().row(), 1).data(),
                                  QMessageBox.Ok | QMessageBox.Cancel) ==QMessageBox.Ok:
                    self.db_connection.delete_driver(id_driver)

                    self.refresh_table()
        except Exception as e:
            print(str(e))

    def new_driver_form(self):
        try:
            form = NewDriverClass(self.db_connection)
            if form.exec_() == form.Accepted:
                self.refresh_table()
        except Exception as e:
            print(str(e))

    def refresh_table(self):
        try:
            all_drivers = self.db_connection.select_all_drivers()
            row_driver = 0
            self.tableDriver.setRowCount(len(all_drivers))
            for driver in all_drivers:
                #print(driver)
                self.tableDriver.setItem(row_driver, 0, QTableWidgetItem(str(driver[0])))
                self.tableDriver.setItem(row_driver, 1, QTableWidgetItem(driver[1]+' '+driver[2]+' '+driver[3]))
                self.tableDriver.setItem(row_driver, 2, QTableWidgetItem(driver[4]))
                row_driver += 1
            #таблица не изменяемая и только для чтения
            self.tableDriver.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # вибирать только строки
            self.tableDriver.setSelectionBehavior(QAbstractItemView.SelectRows)

            #выравнивание столбцов по содержимому
            self.tableDriver.resizeColumnsToContents()
            self.tableDriver.resizeRowsToContents()

        except Exception as e:
            print(str(e))
            QMessageBox.error(self,
            "Ошибка списка водителей",
            "При формировании списка произошла ошибка\n"+str(e),
            QMessageBox.Ok)


def main():
    a = ListDriverClass()
    a.new_driver_form

if __name__ == '__main__':
    main()
