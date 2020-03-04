# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets
from PySide2 import QtCore
from core import language




class Task_List_Widget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(Task_List_Widget, self).__init__(parent)

        # 界面语言
        self.lan = language.lan()
        self.current_lan = self.lan.get_language()

        # 添加搜索框
        self.search_line = QtWidgets.QLineEdit(self)
        self.search_line.setPlaceholderText(self.current_lan.search)
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 10, 0)
        main_layout.addStretch()
        main_layout.addWidget(self.search_line)
        # 设置滑块宽度
        self.verticalScrollBar().setStyleSheet("QScrollBar{width:10px;}")
        # 连接搜索
        self.search_line.textChanged.connect(self.filter_item)

    def filter_item(self):
        search_line_text = self.search_line.text()
        for i in range(self.count()):
            item = self.item(i)
            if search_line_text in item.title:
                item.setHidden(False)
            else:
                item.setHidden(True)

    def __task_item(self, title, subtitle, info):
        wight = QtWidgets.QWidget()
        item_layout = QtWidgets.QVBoxLayout()

        title_info = "<b><font size=\"10\" color=\"#5B5B5B\">%s</font></b>"%(title)
        if subtitle:
            title_info += "<font size=\"3\" color=\"#5B5B5B\">  %s</font>"%(subtitle)
        title_label = QtWidgets.QLabel(title_info)
        subtitle_label = QtWidgets.QLabel("<font size=\"3\" color=\"#ADADAD\">%s</font>"%info)
        item_layout.addWidget(title_label)
        item_layout.addWidget(subtitle_label)
        wight.setLayout(item_layout)
        return wight

    def set_task_item(self, title, subtitle, info, id):
        task_table_item = QtWidgets.QListWidgetItem()
        task_table_item.setSizeHint(QtCore.QSize(200, 90))
        task_table_item.id = id
        task_table_item.title = title

        info = " | ".join(info)
        task_item = self.__task_item(title, subtitle, info)
        self.addItem(task_table_item)
        self.setItemWidget(task_table_item, task_item)