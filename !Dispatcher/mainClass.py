import sys
from PyQt5 import QtWidgets
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
