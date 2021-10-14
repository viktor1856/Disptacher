import sys

import PyQt5.QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTranslator, QLocale
from mainForm import Ui_MainWindow
from dbClass import SqlLiteDb
from ListDriverClass import ListDriverClass
from ListAutoClass import ListAutoClass
from ListCustomersClass import ListCustomersClass


class MainClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connectDb = SqlLiteDb()
        self.newAuto.triggered.connect(self.list_auto_form)
        self.newDriver.triggered.connect(self.list_drivers_form)
        self.customers.triggered.connect(self.list_customers)
        # self.newAuto.triggered.connect(self.newAuto)
        self.calendarWidget.clicked.connect(self.get_task_day)
        self.get_task_day()

    def get_task_day(self):
        self.label.setText('Техника на ' + self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
        self.label_2.setText('Напоминания на ' + self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
        # print(self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))

        all_task_day = self.connectDb.get_task_day(self.calendarWidget.selectedDate().toString('dd.MM.yyyy'))
        print(all_task_day)
        row_task = 0
        self.tableWidget.setRowCount(len(all_task_day))
        color_list = [QColor(0, 150, 0, 120), QColor(0, 0, 150, 120)]
        index_color_list = 0
        memory_row = 0
        for task in all_task_day:
            if self.tableWidget.item(row_task-(1+memory_row), 0):
                if self.tableWidget.item(row_task - (1+memory_row), 0).text() != str(task[1]):
                    memory_row = 0
                    if index_color_list == 0:
                        index_color_list = 1
                    else:
                        index_color_list = 0
                    newitem = QTableWidgetItem(str(task[1]))
                    newitem.setBackground(color_list[index_color_list])
                    self.tableWidget.setItem(row_task, 0, newitem)

                    newitem = QTableWidgetItem(str(task[2] + ' ' + task[3][0] + '.' + task[4][0] + '.'))
                    newitem.setBackground(color_list[index_color_list])
                    self.tableWidget.setItem(row_task, 1, newitem)

                else:
                    memory_row += 1
            else:
                newitem = QTableWidgetItem(str(task[1]))
                newitem.setBackground(color_list[index_color_list])
                self.tableWidget.setItem(row_task, 0, newitem)

                newitem = QTableWidgetItem(str(task[2] + ' ' + task[3][0] + '.' + task[4][0] + '.'))
                newitem.setBackground(color_list[index_color_list])
                self.tableWidget.setItem(row_task, 1, newitem)




            newitem = QTableWidgetItem(str(task[5]))
            newitem.setBackground(color_list[index_color_list])
            self.tableWidget.setItem(row_task, 2, newitem)

            newitem = QTableWidgetItem(str(task[6]))
            newitem.setBackground(color_list[index_color_list])
            self.tableWidget.setItem(row_task, 3, newitem)

            newitem = QTableWidgetItem(str(task[7]))
            newitem.setBackground(color_list[index_color_list])
            self.tableWidget.setItem(row_task, 4, newitem)
            row_task += 1





        # таблица не изменяемая и только для чтения
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # вибирать только строки
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # выравнивание столбцов по содержимому
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def list_customers(self):
        form = ListCustomersClass(self.connectDb)
        form.exec_()

    def list_auto_form(self):
        form = ListAutoClass(self.connectDb)
        form.exec_()

    def list_drivers_form(self):
        form = ListDriverClass(self.connectDb)
        form.exec_()


app = QtWidgets.QApplication(sys.argv)
# получаем локаль для определения языка машины
locale = QLocale.system().name()
# создаем экзепляр переводчика для приложения
qtTranslator = QTranslator(app)
# привязываем зяковой пакет к переводчику
qtTranslator.load('qtbase_ru.qm')
# устанавливаем переводчик на приложение
app.installTranslator(qtTranslator)
mainForm = MainClass()
mainForm.show()
sys.exit(app.exec_())
