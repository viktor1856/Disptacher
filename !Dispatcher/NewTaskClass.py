from PyQt5.QtWidgets import QDialog
from newTaskForm import Ui_newTask
import datetime


class NewTask(QDialog, Ui_newTask):
    def __init__(self, in_connect_db, in_date_task):
        super().__init__()
        self.setupUi(self)
        self.connect_db = in_connect_db
        self.date_task = in_date_task
        self.setWindowTitle('Новая задача на ' + in_date_task)
        times = datetime.datetime.now()
        self.timeEdit.setTime(times.time())
        self.set_all_info_in_combobox()
        # self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.set_visible_remaind)
        self.dateTimeEdit.hide()
        self.label_6.hide()
        self.textEdit_2.hide()

    def accept(self):
        # self.cat_auto.itemData(self.cat_auto.currentIndex())
        all_param_for_insert = [self.comboBox.itemData(self.comboBox.currentIndex()),
                                self.comboBox_2.itemData(self.comboBox_2.currentIndex()),
                                self.textEdit.toPlainText(),
                                self.timeEdit.time().toString('H:mm'),
                                self.comboBox_3.itemData(self.comboBox_3.currentIndex()),
                                self.date_task]

        self.connect_db.insert_new_task(all_param_for_insert)
        super(NewTask, self).accept()

    def set_all_info_in_combobox(self):
        all_autos_list = self.connect_db.select_all_autos()
        # print(all_autos_list)
        for auto in all_autos_list:
            self.comboBox.addItem(auto[1] + ' ' + auto[2], auto[0])

        all_drivers_list = self.connect_db.select_all_drivers()
        for driver in all_drivers_list:
            self.comboBox_2.addItem(driver[1] + ' ' + driver[2][0] + '.' + driver[3][0] + '.', driver[0])

        all_customers_list = self.connect_db.select_all_customers()
        for customer in all_customers_list:
            self.comboBox_3.addItem(customer[1], customer[0])

    def set_visible_remaind(self):
        if self.checkBox.isChecked():
            self.dateTimeEdit.show()
            self.label_6.show()
            self.textEdit_2.show()
            self.dateTimeEdit.setDateTime(datetime.datetime.now())
        else:
            self.label_6.hide()
            self.textEdit_2.hide()
            self.dateTimeEdit.hide()