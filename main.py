from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt5 import uic

import sqlite3
import sys


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.print_db()
        self.add_btn.clicked.connect(self.add_edit_coffee_form_open)

    def print_db(self):
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        res = cur.execute("""SELECT * FROM coffee""").fetchall()

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

    def add_edit_coffee_form_open(self):
        add_form = AddEditCoffeeWidget(self)
        add_form.show()
        self.hide()


class AddEditCoffeeWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add_btn.clicked.connect(self.put_values_in_db)

    def get_values(self):
        name = self.name.text()
        roasting_degree = self.roasting_degree.text()
        corn_or_ground = self.buttonGroup.checkedButton().text()
        flavour = self.flavour.text()
        price = self.price.text()
        pack_volume = self.pack_volume.text()

        return [name, roasting_degree, corn_or_ground, flavour, price, pack_volume]

    def put_values_in_db(self):
        val = self.get_values()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()

        res = cur.execute("""INSERT INTO coffee(name, roasting_degree, ground_or_corn, flavour, price, pack_volume)
        VALUES(?, ?, ?, ?, ?, ?)""", (val[0], val[1], val[2], val[3], val[4], val[5]))

        con.commit()

        self.hide()
        self.parent.show()
        self.parent.print_db()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec())

