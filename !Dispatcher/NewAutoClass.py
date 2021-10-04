from PyQt5.QtWidgets import QDialog
from newAutoForm import Ui_newAuto


class NewAutoClass(QDialog, Ui_newAuto):
    def __init__(self, in_connect_db):
        super().__init__()
        self.setupUi(self)
        self.connect_db = in_connect_db
        self.noNomer.stateChanged.connect(self.set_gos_number_enable)
        try:
            self.typeAuto.addItems(self.connect_db.select_auto_type())
            self.set_category_list()
            self.typeAuto.currentIndexChanged.connect(self.set_category_list)
        except Exception as e:
            print('Error: NewAutoClass->__init__' + str(e))

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
                        print(cat)
                        self.cat_auto.addItem(cat[0], cat[1])
        except Exception as e:
            print('Error: NewAutoClass->set_category_list ' + str(e))


def main():
    pass


if __name__ == '__main__':
    main()
