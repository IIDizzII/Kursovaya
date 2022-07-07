import sys
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtTextToSpeech
from PyQt5.QtWidgets import *
from KMPmethod import *
from Authorization import *
from Main_Form import *
from database_check import *
from Light import *
from PyQt5.QtGui import *

import sqlite3

class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Authorization()
        self.ui.setupUi(self)
        self.mainwindow = MainWindow()

        self.ui.pushButton_2.clicked.connect(self.reg)
        self.ui.pushButton.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    # Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    # Обработчик сигналов
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        if value == "Успешная авторизация!":
            self.mainwindow.name = self.ui.lineEdit.text()
            self.mainwindow.show()

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormM()
        self.ui.setupUi(self)
        self.method = KMP_method()
        self.name = str
        self.searchHighLight = SearchHighLight(self.ui.textEdit.document())

        self.ui.pushButton.clicked.connect(self.read_from_file)
        self.ui.pushButton_2.clicked.connect(self.kmp_method)
        self.ui.pushButton_3.clicked.connect(self.to_database)
        self.ui.pushButton_4.clicked.connect(self.from_database)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, "Оповещение", value)

    def read_from_file(self):
        some_file = QFileDialog.getOpenFileName(self)[0]
        try:
            f = open(some_file, 'r')
            with f:
                data = f.read()
                self.ui.textEdit.setText(data)
            f.close()
        except FileNotFoundError:
            self.signal_handler('Файл не выбран!')

    def kmp_method(self):
        self.searchHighLight.searchText(self.ui.lineEdit_2.text())

    def to_database(self):
        con = sqlite3.connect(f'db/KMPdatabase.db')
        cur = con.cursor()

        text = self.ui.textEdit.toPlainText()

        cur.execute(f"INSERT INTO dbase (login, text) VALUES ('{self.name}','{text}');")
        self.signal_handler('Tекст успешно записан в базу данных!')
        con.commit()

        cur.close()
        con.close()

    def from_database(self):
        connection = sqlite3.connect(f'db/KMPdatabase.db')
        cur = connection.cursor()
        sqlquery = f'SELECT * FROM dbase WHERE login="{self.name}"'

        list_of_rows = list(cur.execute(sqlquery))

        self.ui.tableWidget.setRowCount(len(list_of_rows))
        tablerow= 0
        for row in list_of_rows:
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablerow += 1

        connection.close()

    def save_to_file(self):
        some_file = QFileDialog.getSaveFileName(self)[0]

        try:
            f = open(some_file, 'w')
            text = self.lineEdit_4.text()
            f.write(text)
            f.close()
        except FileNotFoundError:
            self.signal_handler('Файл не выбран!')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())