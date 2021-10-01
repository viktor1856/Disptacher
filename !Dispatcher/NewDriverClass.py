# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     10.09.2021
# Copyright:   (c) Admin 2021
# Licence:     <your licence>
# -------------------------------------------------------------------------------

from newDriverForm import Ui_newDriver
from PyQt5.QtWidgets import QDialog, QCheckBox, QDialogButtonBox
from PyQt5.QtCore import QDate


class NewDriverClass(QDialog, Ui_newDriver):
    def __init__(self, in_database_connect,  id_driver=0):
        super().__init__()
        self.database_connect = in_database_connect
        self.id_driver = id_driver
        self.setupUi(self)
        self.skzi_date.setVisible(False)
        self.label_10.setVisible(False)
        self.skzi.stateChanged.connect(self.visible_date_skzi)
        self.estr_date.setVisible(False)
        self.label_11.setVisible(False)
        self.estr.stateChanged.connect(self.visible_date_estr)
        if id_driver > 0:
            self.set_driver_info(id_driver)
            # self.buttonBox->button(QDialogButtonBox::Ok)->setText("Run");
            self.buttonBox.button(QDialogButtonBox.Ok).setText("Сохранить изменения")

    def set_driver_info(self, id_driver):
        try:
            driver_info = self.database_connect.select_driver_info(id_driver)
            print(driver_info)
            self.fam.setText(driver_info[1])
            self.nam.setText(driver_info[2])
            self.patr.setText(driver_info[3])
            print(driver_info[4])

            self.date_birth.setDate(QDate.fromString(driver_info[4], "dd.MM.yyyy"))
            self.end_drivers_document.setDate(QDate.fromString(driver_info[5], "dd.MM.yyyy"))
            if driver_info[6]:
                self.skzi.setChecked(True)
                self.skzi_date.setDate(QDate.fromString(driver_info[7], "dd.MM.yyyy"))
            if driver_info[8]:
                self.estr.setChecked(True)
                self.estr_date.setDate(QDate.fromString(driver_info[9], "dd.MM.yyyy"))
            if driver_info[10]:
                driver_category_list = driver_info[10].split(';')
                widgets = (self.auto_category.itemAt(i).widget() for i in range(self.auto_category.count()))
                for w in widgets:
                    if isinstance(w, QCheckBox):
                        if w.objectName() in driver_category_list:
                            w.setChecked(True)
            if driver_info[11]:
                driver_category_list = driver_info[11].split(';')
                widgets = (self.tractor_category.itemAt(i).widget() for i in range(self.tractor_category.count()))
                for w in widgets:
                    if isinstance(w, QCheckBox):
                        if w.objectName() in driver_category_list:
                            w.setChecked(True)
        except Exception as e:
            print('Error: newDriverClass->set_driver_info ' + str(e))

    def visible_date_skzi(self):
        if self.skzi.isChecked():
            self.skzi_date.setVisible(True)
            self.label_10.setVisible(True)
        else:
            self.skzi_date.setVisible(False)
            self.label_10.setVisible(False)

    def visible_date_estr(self):
        if self.estr.isChecked():
            self.estr_date.setVisible(True)
            self.label_11.setVisible(True)
        else:
            self.estr_date.setVisible(False)
            self.label_11.setVisible(False)

    def accept(self):
        try:
            param_sql_insert = [self.fam.text(), self.nam.text(), self.patr.text(), self.date_birth.text(),
                                self.end_drivers_document.text(), self.skzi.isChecked()]

            if self.skzi.isChecked():
                param_sql_insert.append(self.skzi_date.text())
            else:
                param_sql_insert.append(None)

            param_sql_insert.append(self.estr.isChecked())
            if self.estr.isChecked():
                param_sql_insert.append(self.estr_date.text())
            else:
                param_sql_insert.append(None)

            auto_category = ''

            widgets = (self.auto_category.itemAt(i).widget() for i in range(self.auto_category.count()))
            for w in widgets:
                if isinstance(w, QCheckBox):
                    if w.isChecked():
                        auto_category += w.objectName() + ';'

            param_sql_insert.append(auto_category)

            tractor_category = ''
            widgets = (self.tractor_category.itemAt(i).widget() for i in range(self.tractor_category.count()))
            for w in widgets:
                if isinstance(w, QCheckBox):
                    if w.isChecked():
                        tractor_category += w.objectName() + ';'

            param_sql_insert.append(tractor_category)
            if self.id_driver == 0:
                self.database_connect.insert_new_driver(param_sql_insert)
            else:
                param_sql_insert.append(self.id_driver)
                self.database_connect.update_driver(param_sql_insert)
        except Exception as e:
            print('Error: newDriverClass->accept()' + str(e))
        super(NewDriverClass, self).accept()


def main():
    pass


if __name__ == '__main__':
    main()
