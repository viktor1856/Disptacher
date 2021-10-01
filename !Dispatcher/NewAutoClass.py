from PyQt5.QtWidgets import QDialog
from newAutoForm import Ui_newAuto


class NewAutoClass(QDialog, Ui_newAuto):
    def __init__(self, in_connect_db):
        super().__init__()
        self.setupUi(self)
        self.connect_db = in_connect_db
        try:
            self.typeAuto.addItems(self.connect_db.select_auto_type())
            self.set_category_list()
            self.typeAuto.currentIndexChanged.connect(self.set_category_list)
        except Exception as e:
            print('Error: NewAutoClass->__init__' + str(e))

    def accept(self):
        print("тест закрытия формы")


    def _set_category_list(self):
        try:
            if self.typeAuto.currentText():
                self.cat_auto.clear()
                self.cat_auto.addItem('Без категории')
                cat_auto_list = self.connect_db.select_category_auto(self.typeAuto.currentText())
                if cat_auto_list:
                    self.cat_auto.addItems(cat_auto_list)

        except Exception as e:
            print('Error: NewAutoClass->set_category_list' + str(e))


def main():
    pass


if __name__ == '__main__':
    main()
