# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newTaskForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newTask(object):
    def setupUi(self, newTask):
        newTask.setObjectName("newTask")
        newTask.resize(324, 496)
        self.horizontalLayout = QtWidgets.QHBoxLayout(newTask)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(newTask)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(newTask)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(newTask)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(newTask)
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(newTask)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(newTask)
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.label_3 = QtWidgets.QLabel(newTask)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(newTask)
        self.timeEdit.setCalendarPopup(False)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.label_5 = QtWidgets.QLabel(newTask)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(newTask)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.line = QtWidgets.QFrame(newTask)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.checkBox = QtWidgets.QCheckBox(newTask)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(newTask)
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateTimeEdit.setProperty("showGroupSeparator", True)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.label_6 = QtWidgets.QLabel(newTask)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.textEdit_2 = QtWidgets.QTextEdit(newTask)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(newTask)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(newTask)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label.setBuddy(self.comboBox)
        self.label_2.setBuddy(self.comboBox_2)
        self.label_4.setBuddy(self.comboBox_3)
        self.label_3.setBuddy(self.timeEdit)
        self.label_5.setBuddy(self.textEdit)
        self.label_6.setBuddy(self.textEdit_2)

        self.retranslateUi(newTask)
        self.pushButton.clicked.connect(newTask.reject)
        self.pushButton_2.clicked.connect(newTask.accept)
        QtCore.QMetaObject.connectSlotsByName(newTask)

    def retranslateUi(self, newTask):
        _translate = QtCore.QCoreApplication.translate
        newTask.setWindowTitle(_translate("newTask", "Новая задача"))
        self.label.setText(_translate("newTask", "Транспортное средство"))
        self.label_2.setText(_translate("newTask", "Водитель"))
        self.label_4.setText(_translate("newTask", "Заказчик"))
        self.label_3.setText(_translate("newTask", "Время начала работы"))
        self.label_5.setText(_translate("newTask", "Задача"))
        self.checkBox.setText(_translate("newTask", "Напомнить"))
        self.label_6.setText(_translate("newTask", "Текст напоминания"))
        self.pushButton_2.setText(_translate("newTask", "Создать"))
        self.pushButton.setText(_translate("newTask", "Отмена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newTask = QtWidgets.QDialog()
    ui = Ui_newTask()
    ui.setupUi(newTask)
    newTask.show()
    sys.exit(app.exec_())
