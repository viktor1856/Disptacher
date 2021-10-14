from PyQt5.QtWidgets import QDialog, QDialogButtonBox
from newAutoForm import Ui_newAuto


class NewAutoClass(QDialog, Ui_newAuto):
    def __init__(self, in_connect_db, id_auto=0):
        super().__init__()
        self.setupUi(self)
        self.id_auto = id_auto
        self.connect_db = in_connect_db
        self.noNomer.stateChanged.connect(self.set_gos_number_enable)
        self.typeAuto.currentIndexChanged.connect(self.set_category_list)
        self.typeAuto.addItems(self.connect_db.select_auto_type())
        if id_auto > 0:
            self.set_auto_info(id_auto=id_auto)
        else:
            self.set_category_list()

    def set_auto_info(self, id_auto):
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Сохранить изменения")
        try:
            auto_info_list = self.connect_db.select_auto_info(id_auto)

            self.modelAuto.setText(auto_info_list[1])

            if auto_info_list[2] == 'Безномерная':
                self.noNomer.setChecked(True)
            else:
                self.gosNomer.setText(auto_info_list[2])

            self.typeAuto.setCurrentText(auto_info_list[4])
            self.set_category_list()

            for index in range(1, self.cat_auto.count()):
                if self.cat_auto.itemData(index) == auto_info_list[3]:
                    self.cat_auto.setCurrentIndex(index)
                    break

            if auto_info_list[5]:
                self.skzi.setChecked(True)

            if auto_info_list[6]:
                self.estr.setChecked(True)
        except Exception as e:
            print('Error: NewAutoClass->set_auto_info' + str(e))

    def set_gos_number_enable(self):
        if self.noNomer.isChecked():
            self.gosNomer.setEnabled(False)
        else:
            self.gosNomer.setEnabled(True)

    def accept(self):
        try:
            sql_param_list = [self.modelAuto.text(), self.typeAuto.currentText(),
                              self.cat_auto.itemData(self.cat_auto.currentIndex()),
                              self.skzi.isChecked(), self.estr.isChecked()]
            if self.noNomer.isChecked():
                sql_param_list.append('Безномерная')
            else:
                sql_param_list.append(self.gosNomer.text())

            if self.id_auto > 0:
                sql_param_list.append(self.id_auto)
                self.connect_db.update_auto(sql_param_list)
            else:
                self.connect_db.insert_new_auto(sql_param_list)
        except Exception as e:
            print('Error: NewAutoClass->accept()' + str(e))
        super(NewAutoClass, self).accept()

    def set_category_list(self):
        try:
            if self.typeAuto.currentText():
                self.cat_auto.clear()
                self.cat_auto.addItem('Без категории')
                cat_auto_list = self.connect_db.select_category_auto(self.typeAuto.currentText())
                if cat_auto_list:
                    for cat in cat_auto_list:
                        self.cat_auto.addItem(cat[0], cat[1])
        except Exception as e:
            print('Error: NewAutoClass->set_category_list ' + str(e))


def main():
    pass


if __name__ == '__main__':
    main()
