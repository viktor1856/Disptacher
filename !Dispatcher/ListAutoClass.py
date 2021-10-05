from listAutoForm import Ui_autoList
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from NewAutoClass import NewAutoClass


class ListAutoClass(QDialog, Ui_autoList):
    def __init__(self, in_connect_db):
        super().__init__()
        self.setupUi(self)
        self.connect_db = in_connect_db
        self.newAuto.clicked.connect(self.new_auto_form)
        self.deleteAuto.clicked.connect(self.delete_auto)
        self.editAuto.clicked.connect(self.edit_auto)
        self.refresh_table()

    def edit_auto(self):
        try:
            id_auto = int(self.tableAuto.model().index(self.tableAuto.currentIndex().row(), 0).data())
            form = NewAutoClass(self.connect_db, id_auto=id_auto)
            if form.exec_() == form.Accepted:
                self.refresh_table()
        except Exception as e:
            print('Error: ListAutoClass->edit_auto ' + str(e))

    def delete_auto(self):
        try:
            id_auto = self.tableAuto.model().index(self.tableAuto.currentIndex().row(), 0).data()
            if int(id_auto) > 0:
                full_name_auto = (self.tableAuto.model().index(self.tableAuto.currentIndex().row(), 1).data() + ' ' +
                                  self.tableAuto.model().index(self.tableAuto.currentIndex().row(), 2).data())
                if QMessageBox.warning(self,
                                       "Удаление транспортного средства",
                                       "Вы уверены что хотите удалить Транспортное средство?\n" +
                                       full_name_auto,
                                       QMessageBox.Ok | QMessageBox.Cancel) == QMessageBox.Ok:
                    self.connect_db.delete_auto(id_auto)
                    self.refresh_table()
        except Exception as e:
            print('Error: ListAutoClass->deleteAuto ' + str(e))

    def refresh_table(self):
        try:
            all_autos = self.connect_db.select_all_autos()
            row_autos = 0
            self.tableAuto.setRowCount(len(all_autos))
            for auto in all_autos:
                # print(driver)
                self.tableAuto.setItem(row_autos, 0, QTableWidgetItem(str(auto[0])))
                self.tableAuto.setItem(row_autos, 1, QTableWidgetItem(str(auto[1])))
                self.tableAuto.setItem(row_autos, 2, QTableWidgetItem(str(auto[2])))
                row_autos += 1
            # таблица не изменяемая и только для чтения
            self.tableAuto.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # вибирать только строки
            self.tableAuto.setSelectionBehavior(QAbstractItemView.SelectRows)

            # выравнивание столбцов по содержимому
            self.tableAuto.resizeColumnsToContents()
            self.tableAuto.resizeRowsToContents()

        except Exception as e:
            print(str(e))
            QMessageBox.error(self,
                              "Ошибка списка водителей",
                              "При формировании списка произошла ошибка\n" + str(e),
                              QMessageBox.Ok)

    def new_auto_form(self):
        try:
            form = NewAutoClass(self.connect_db)
            if form.exec_() == form.Accepted:
                self.refresh_table()
        except Exception as e:
            print("Error: ListAutoClass->new_auto_form()" + str(e))
            # проеврка ветки