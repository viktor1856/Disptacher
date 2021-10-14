import sys
from PyQt5 import QtWidgets
import sqlite3
import os

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.setGeometry(300, 300, 300, 200)
window.setWindowTitle('Тест работы приложений')
button = QtWidgets.QPushButton(parent=window, text='НАЖМИ ДЛЯ ТЕСТА')
button.setGeometry(25, 25, 150, 150)


def start_test():
    try:
        path = os.path.abspath(os.curdir)
        connection_db = sqlite3.connect(path + '\\TestBase.db')
        cursor = connection_db.cursor()
        cursor.execute('create table TestTable(id INTEGER PRIMARY KEY AUTOINCREMENT,test1 VARCHAR)')
        connection_db.commit()
        cursor.execute('insert into TestTable (test1) values(:param)', ['"Я работаю!"'])
        connection_db.commit()
        select_test = cursor.execute('select * from TestTable')
        sel = select_test.fetchone()
        cursor.close()
        connection_db.close()
        os.remove(path + '\\TestBase.db')
        if (QtWidgets.QMessageBox.information(None, 'Успешный тест','Успешно проверено\nТестовая строка:\n'+sel[1]) ==
                QtWidgets.QMessageBox.Ok):
            window.close()
    except Exception as e:
        err = 'Произошла ошибка при тестировании\n'+str(e)
        QtWidgets.QMessageBox.warning(None, 'Ошибка теста', err, QtWidgets.QMessageBox.Ok)

button.clicked.connect(start_test)
window.show()
sys.exit(app.exec_())
