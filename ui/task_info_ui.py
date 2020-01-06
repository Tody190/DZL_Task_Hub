# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets




class Task_Info_Widget(QtWidgets.QTableWidget):
    def __init__(self):
        super(Task_Info_Widget, self).__init__()
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setColumnCount(2)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.row = 0

    def clear_items(self):
        self.row = 0
        self.clear()

    def add_item(self, label, info):
        label_item = QtWidgets.QTableWidgetItem(label)
        self.setItem(self.row, 0, label_item)
        info_item = QtWidgets.QTableWidgetItem(str(info))
        self.setItem(self.row, 1, info_item)
        self.row += 1