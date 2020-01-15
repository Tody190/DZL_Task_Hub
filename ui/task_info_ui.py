# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets




class Task_Info_Widget(QtWidgets.QTableWidget):
    def __init__(self):
        super(Task_Info_Widget, self).__init__()
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.setColumnCount(2)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.horizontalHeader().setStretchLastSection(True)

    def clear_items(self):
        self.setRowCount(0)
        self.clear()

    def add_items(self, items_info):
        self.setRowCount(len(items_info))
        row = 0
        for label in items_info:
            label_item = QtWidgets.QTableWidgetItem(str(label))
            self.setItem(row, 0, label_item)
            info_item = QtWidgets.QTableWidgetItem(str(items_info[label]))
            self.setItem(row, 1, info_item)
            row += 1