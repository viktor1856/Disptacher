# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listDriverForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_listDriverForm(object):
    def setupUi(self, listDriverForm):
        listDriverForm.setObjectName("listDriverForm")
        listDriverForm.resize(509, 610)
        self.horizontalLayout = QtWidgets.QHBoxLayout(listDriverForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableDriver = QtWidgets.QTableWidget(listDriverForm)
        self.tableDriver.setMinimumSize(QtCore.QSize(379, 0))
        self.tableDriver.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableDriver.setObjectName("tableDriver")
        self.tableDriver.setColumnCount(3)
        self.tableDriver.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableDriver.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDriver.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDriver.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDriver.setHorizontalHeaderItem(2, item)
        self.tableDriver.horizontalHeader().setVisible(False)
        self.tableDriver.horizontalHeader().setDefaultSectionSize(100)
        self.tableDriver.horizontalHeader().setHighlightSections(True)
        self.tableDriver.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableDriver)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.newDriver = QtWidgets.QPushButton(listDriverForm)
        self.newDriver.setObjectName("newDriver")
        self.verticalLayout.addWidget(self.newDriver)
        self.editDriver = QtWidgets.QPushButton(listDriverForm)
        self.editDriver.setObjectName("editDriver")
        self.verticalLayout.addWidget(self.editDriver)
        self.deleteDriver = QtWidgets.QPushButton(listDriverForm)
        self.deleteDriver.setObjectName("deleteDriver")
        self.verticalLayout.addWidget(self.deleteDriver)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(listDriverForm)
        QtCore.QMetaObject.connectSlotsByName(listDriverForm)

    def retranslateUi(self, listDriverForm):
        _translate = QtCore.QCoreApplication.translate
        listDriverForm.setWindowTitle(_translate("listDriverForm", "???????????? ??????????????????"))
        item = self.tableDriver.verticalHeaderItem(0)
        item.setText(_translate("listDriverForm", "1"))
        item = self.tableDriver.horizontalHeaderItem(0)
        item.setText(_translate("listDriverForm", "???"))
        item = self.tableDriver.horizontalHeaderItem(1)
        item.setText(_translate("listDriverForm", "?????? ????????????????"))
        item = self.tableDriver.horizontalHeaderItem(2)
        item.setText(_translate("listDriverForm", "???????? ????????????????"))
        self.newDriver.setText(_translate("listDriverForm", "?????????? ????????????????"))
        self.editDriver.setText(_translate("listDriverForm", "??????????????????????????"))
        self.deleteDriver.setText(_translate("listDriverForm", "?????????????? ????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listDriverForm = QtWidgets.QDialog()
    ui = Ui_listDriverForm()
    ui.setupUi(listDriverForm)
    listDriverForm.show()
    sys.exit(app.exec_())
