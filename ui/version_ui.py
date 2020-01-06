# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets




class Versions_Widget(QtWidgets.QTableWidget):
    def __init__(self):
        super(Versions_Widget, self).__init__()
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setColumnCount(3)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.row = 0

    def clear_items(self):
        self.row = 0
        self.clear()

    def add_item(self, name, created_time, description):
        name_item = QtWidgets.QTableWidgetItem(name)
        self.setItem(self.row, 0, name_item)
        created_time_item = QtWidgets.QTableWidgetItem(created_time)
        self.setItem(self.row, 1, created_time_item)
        description_item = QtWidgets.QTableWidgetItem(description)
        self.setItem(self.row, 2, description_item)
        self.row += 1