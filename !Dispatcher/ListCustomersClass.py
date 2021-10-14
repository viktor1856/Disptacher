from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QAbstractItemView, QMessageBox
from customerListForm import Ui_customers


class ListCustomersClass(QDialog, Ui_customers):
    """
    Класс функционала диалогового окна "Заказчик"

    Графическая оболочка от класса Ui_customers
    """

    def __init__(self, data_base_connection):
        """
        Конструктор диалогового окна "Заказчик"

        :param data_base_connection: экземпляр класса SqlLiteDb

        """
        super().__init__()
        self.setupUi(self)
        self.connect_db = data_base_connection
        self.refresh_table()
        self.insertCustomer.clicked.connect(self.insert_new_customer)
        self.deleteCustomer.clicked.connect(self.delete_customer)
        self.updateCustomers.clicked.connect(self.start_cancel_update_customer)
        self.update_customer_flag = False

    def start_cancel_update_customer(self):
        """
        Процедура изменения состояния состояния изменения заказчика

        Меняет названия кнопок, видимость кнопок, и привязки сигналов кнопок

        """
        if self.update_customer_flag:
            self.update_customer_flag = False
            self.deleteCustomer.setVisible(True)
            self.listCustomers.setEnabled(True)
            self.insertCustomer.setText('Добавить заказчика')
            self.updateCustomers.setText('Изменить\nзаказчика')
            self.insertCustomer.disconnect()
            self.insertCustomer.clicked.connect(self.start_cancel_update_customer)
            self.lineEdit.clear()
        else:
            try:
                id_customer = self.listCustomers.model().index(self.listCustomers.currentIndex().row(), 0).data()
                if id_customer:
                    self.update_customer_flag = True
                    self.deleteCustomer.setVisible(False)
                    self.listCustomers.setEnabled(False)
                    self.insertCustomer.setText('Сохранить изменения')
                    self.insertCustomer.disconnect()
                    self.insertCustomer.clicked.connect(self._update_customer)
                    self.updateCustomers.setText('Отмена')
                    self.lineEdit.setText(self.listCustomers.model().index(self.listCustomers.currentIndex().row(), 1).data())
            except Exception as e:
                print('Error: ListCustomersClass->start_cancel_update_customer(start update) ' + str(e))

    def _update_customer(self):
        """
        Процедура выполнения обновления заказчика

        Привязывается к сигналу кнопки "Сохранить изменения" после изменения состояния
        процедурой start_cancel_update_customer

        ->Собирает выбирает из таблицы параметры id_customer  и name_customer и помещает их в list

        ->вызывает функцию update_customer модуля БД

        ->вызывает функцию для изменения состояния изменения заказчика start_cancel_update_customer

        ->обновляет данные в таблице
        """
        try:
            id_customer = int(self.listCustomers.model().index(self.listCustomers.currentIndex().row(), 0).data())
            if id_customer > 0:
                name_customer = self.lineEdit.text()
                self.connect_db.update_customer(params=[name_customer, id_customer])
                self.start_cancel_update_customer()
                self.refresh_table()
        except Exception as e:
            print('Error: ListCustomersClass->_update_customer ' + str(e))

    def delete_customer(self):
        try:
            id_customer = self.listCustomers.model().index(self.listCustomers.currentIndex().row(), 0).data()
            if id_customer:
                if QMessageBox.warning(self, 'Удаление заказчика',
                                       ('Вы действительно хотите удалить заказчика?\n' +
                                        self.listCustomers.model().index(self.listCustomers.currentIndex().row(), 1).
                                        data()),
                                       QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                    self.connect_db.delete_customer(id_customer)
                    self.refresh_table()
        except Exception as e:
            print('Error: ListCustomersClass->delete_customer (delete) ' + str(e))

    def insert_new_customer(self):
        """
        Слот сигнала нажатия на кнопку "Добавить заказчика"

        ->Вызывает метод класса работы с БД для вставки заказчика в таблицу заказчиков

        ->Чистит поле ввода имен заказчика

        ->Вызывает метод для обновления таблицы заказчиков из БД
        """
        self.connect_db.insert_new_customer(self.lineEdit.text())
        self.lineEdit.clear()
        self.refresh_table()

    def refresh_table(self):
        """
        Метод для обновления данных в таблице заказчиков

        Делает запрос к БД и записывает все полученные данные в таблицу
        с последующей настройкой параметров таблицы

        """
        try:

            all_customers = self.connect_db.select_all_customers()
            row_customers = 0
            self.listCustomers.setRowCount(len(all_customers))
            for customer in all_customers:
                self.listCustomers.setItem(row_customers, 0, QTableWidgetItem(str(customer[0])))
                self.listCustomers.setItem(row_customers, 1, QTableWidgetItem(str(customer[1])))
                row_customers += 1

            # таблица не изменяемая и только для чтения
            self.listCustomers.setEditTriggers(QAbstractItemView.NoEditTriggers)

            # вибирать только строки
            self.listCustomers.setSelectionBehavior(QAbstractItemView.SelectRows)

            # выравнивание столбцов и строк по содержимому
            self.listCustomers.resizeColumnsToContents()
            self.listCustomers.resizeRowsToContents()

        except Exception as e:
            print(str(e))
            QMessageBox.error(self,
                              "Ошибка списка заказчиков",
                              "При формировании списка произошла ошибка\n" + str(e),
                              QMessageBox.Ok)
