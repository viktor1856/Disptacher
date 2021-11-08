from addFixDriverForm import Ui_addFixDriver
from PyQt5.QtWidgets import QDialog, QMessageBox
import datetime


class AddFixDriverClass(QDialog, Ui_addFixDriver):
    def __init__(self, data_base_connection):
        super().__init__()
        self.setupUi(self)
        self.db_connection = data_base_connection
        self.set_all_info_in_combobox()
        self.autosBox.currentIndexChanged.connect(self.fits_category)
        self.driversBox.currentIndexChanged.connect(self.fits_category)
        self.category.clear()

    def set_all_info_in_combobox(self):
        all_autos_list = self.db_connection.select_all_autos()
        # print(all_autos_list)
        for auto in all_autos_list:
            self.autosBox.addItem(auto[1] + ' ' + auto[2], [auto[0], auto[3], auto[4], auto[5]])
        self.autosBox.setCurrentIndex(-1)
        # self.cat_auto.itemData(self.cat_auto.currentIndex())

        all_drivers_list = self.db_connection.select_all_drivers()
        # print(all_drivers_list)
        for driver in all_drivers_list:
            self.driversBox.addItem(driver[1] + ' ' + driver[2][0] + '.' + driver[3][0] + '.', [driver[0],
                                                                                                driver[5], driver[6],
                                                                                                driver[7], driver[8],
                                                                                                driver[9], driver[10]])
        self.driversBox.setCurrentIndex(-1)

    def accept(self) -> None:
        try:
            sql_param = [self.autosBox.itemData(self.autosBox.currentIndex())[0],
                         self.driversBox.itemData(self.driversBox.currentIndex())[0]]
            fixed_repeat = self.db_connection.select_repeat_fixed(sql_param)
            if fixed_repeat <= 0:
                self.db_connection.insert_fixed_drivers(sql_param)
                super(AddFixDriverClass, self).accept()
            elif fixed_repeat == 1:
                QMessageBox.warning(self,
                                  "Ошибка закрепления водителей",
                                  "За автомобилем уже закреплен водитель",
                                  QMessageBox.Ok)
            elif fixed_repeat == 2:
                QMessageBox.warning(self,
                                  "Ошибка закрепления водителей",
                                  "Водитель закреплен на другом автомобиле",
                                  QMessageBox.Ok)
            elif fixed_repeat == 3:
                QMessageBox.warning(self,
                                  "Ошибка закрепления водителей",
                                  "Такое закрепление уже существует",
                                  QMessageBox.Ok)
        except Exception as e:
            print('Error: AddFixDriverClass->accept ' + str(e))


    def fits_category(self):
        if self.autosBox.currentIndex() >= 0 and self.driversBox.currentIndex() >= 0:
            # print(self.autosBox.itemData(self.autosBox.currentIndex())[1])
            # print(self.driversBox.itemData(self.driversBox.currentIndex())[1])
            message_fixed_error = ''

            # проверка на категории
            category_autos = self.autosBox.itemData(self.autosBox.currentIndex())[1]
            all_category = []
            category_driver_auto = self.driversBox.itemData(self.driversBox.currentIndex())[1]
            if category_driver_auto:
                all_category += category_driver_auto.split(';')

            category_driver_tractor = self.driversBox.itemData(self.driversBox.currentIndex())[2]
            if category_driver_tractor:
                all_category += category_driver_tractor.split(';')
            if all_category:
                if category_autos not in all_category:
                    message_fixed_error += '<font color="red">У водителя нет необходимой категории для управления ТС</font><br>'
            else:
                message_fixed_error += '<font color="red">У водителя нет необходимой категории для управления ТС</font><br>'
            # проверка на СКЗИ
            if self.autosBox.itemData(self.autosBox.currentIndex())[2]:
                if self.driversBox.itemData(self.driversBox.currentIndex())[3]:
                    if self.driversBox.itemData(self.driversBox.currentIndex())[5] <= datetime.datetime.now().strftime('%d.%m.%Y'):
                        message_fixed_error += '<font color="red">У водителя истекает(истек) срок карты СКЗИ</font><br>'
                else:
                    message_fixed_error += '<font color="red">У водителя нет карточки СКЗИ для управления ТС</font><br>'

            # проверка карты ЕСТР
            if self.autosBox.itemData(self.autosBox.currentIndex())[3]:
                if self.driversBox.itemData(self.driversBox.currentIndex())[4]:
                    if self.driversBox.itemData(self.driversBox.currentIndex())[6] <= datetime.datetime.now().strftime('%d.%m.%Y'):
                        message_fixed_error += '<font color="red">У водителя истекает(истек) срок карты ЕСТР</font><br>'
                else:
                    message_fixed_error += '<font color="red">У водителя нет карточки ЕСТР для управления ТС</font><br>'

            self.category.setText(message_fixed_error)
