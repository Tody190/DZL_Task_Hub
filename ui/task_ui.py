# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets
from PySide2 import QtCore




class Task_List_Widget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(Task_List_Widget, self).__init__(parent)

    def __task_item(self, id, name, info):
        wight = QtWidgets.QWidget()
        item_layout = QtWidgets.QVBoxLayout()
        task_name_label = QtWidgets.QLabel("<b><font size=\"10\" color=\"#5B5B5B\">%s</font></b> \
                                           <font size=\"1\" color=\"#5B5B5B\">  %s</font>"%(name, id))
        link_label = QtWidgets.QLabel("<font size=\"3\" color=\"#ADADAD\">%s</font>"%info)
        item_layout.addWidget(task_name_label)
        item_layout.addWidget(link_label)
        wight.setLayout(item_layout)
        return wight

    def set_task_item(self, name, info, id=None):
        task_table_item = QtWidgets.QListWidgetItem()
        task_table_item.setSizeHint(QtCore.QSize(200, 90))
        if id:
            task_table_item.id = id
        task_item = self.__task_item(id, name, " | ".join(info))
        self.addItem(task_table_item)
        self.setItemWidget(task_table_item, task_item)