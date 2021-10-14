# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customerListForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customers(object):
    def setupUi(self, customers):
        customers.setObjectName("customers")
        customers.resize(456, 326)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(customers)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listCustomers = QtWidgets.QTableWidget(customers)
        self.listCustomers.setObjectName("listCustomers")
        self.listCustomers.setColumnCount(2)
        self.listCustomers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listCustomers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listCustomers.setHorizontalHeaderItem(1, item)
        self.listCustomers.horizontalHeader().setVisible(True)
        self.listCustomers.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.listCustomers)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.updateCustomers = QtWidgets.QPushButton(customers)
        self.updateCustomers.setMinimumSize(QtCore.QSize(0, 30))
        self.updateCustomers.setObjectName("updateCustomers")
        self.verticalLayout.addWidget(self.updateCustomers)
        self.deleteCustomer = QtWidgets.QPushButton(customers)
        self.deleteCustomer.setObjectName("deleteCustomer")
        self.verticalLayout.addWidget(self.deleteCustomer)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lineEdit = QtWidgets.QLineEdit(customers)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.insertCustomer = QtWidgets.QPushButton(customers)
        self.insertCustomer.setMaximumSize(QtCore.QSize(120, 16777215))
        self.insertCustomer.setObjectName("insertCustomer")
        self.verticalLayout_2.addWidget(self.insertCustomer)

        self.retranslateUi(customers)
        QtCore.QMetaObject.connectSlotsByName(customers)

    def retranslateUi(self, customers):
        _translate = QtCore.QCoreApplication.translate
        customers.setWindowTitle(_translate("customers", "Список заказчиков"))
        item = self.listCustomers.horizontalHeaderItem(0)
        item.setText(_translate("customers", "№"))
        item = self.listCustomers.horizontalHeaderItem(1)
        item.setText(_translate("customers", "Заказчик"))
        self.updateCustomers.setText(_translate("customers", "Изменить\n"
"заказчика"))
        self.deleteCustomer.setText(_translate("customers", "Удалить\n"
"заказчика"))
        self.insertCustomer.setText(_translate("customers", "Добавить заказчика"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customers = QtWidgets.QDialog()
    ui = Ui_customers()
    ui.setupUi(customers)
    customers.show()
    sys.exit(app.exec_())
