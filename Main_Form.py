# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main (2).ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormM(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 482)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 220, 151, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 220, 251, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 200, 571, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 170, 151, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 280, 571, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 170, 151, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 250, 571, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 220, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 571, 151))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Открыть из файла"))
        self.pushButton_2.setText(_translate("Form", "Поиск"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Найти"))
        self.pushButton_3.setText(_translate("Form", "Сохранить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "login"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "text"))
        self.pushButton_4.setText(_translate("Form", "Открыть из истории"))
        self.textEdit.setPlaceholderText(_translate("Form", "Text..."))
