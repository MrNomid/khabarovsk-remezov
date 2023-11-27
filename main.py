from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt5 import uic

import sqlite3
import sys


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.print_db()

    def print_db(self):
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        res = cur.execute("""SELECT * FROM coffee""").fetchall()
        print(res)

        for line in res:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(line[0])))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(line[1])))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(line[2])))
            self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(line[3])))
            self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(line[4])))
            self.tableWidget.setItem(rowPosition, 5, QTableWidgetItem(str(line[5])))
            self.tableWidget.setItem(rowPosition, 6, QTableWidgetItem(str(line[6])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())

