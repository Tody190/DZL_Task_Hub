# -*- coding: utf-8 -*-
__author__ = "yangtao"


import os

from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from core import language

class Drop_List(QtWidgets.QListWidget):
    drop_file = QtCore.Signal(str)
    def __init__(self, parent=None):
        super(Drop_List, self).__init__(parent)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(Drop_List, self).dragEnterEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url_object in event.mimeData().urls():
                url_text = url_object.toLocalFile()
                self.drop_file.emit(url_text)
        else:
            super(Drop_List, self).dropEvent(event)


class Creator_Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Creator_Widget, self).__init__(parent)

        # 界面语言
        self.lan = language.lan()
        self.current_lan = self.lan.get_language()

        self.__init_ui()
        self.__init_connect()

    def __init_ui(self):
        # 版本名
        self.version_name_label = QtWidgets.QLabel(self.current_lan.version_name)
        self.version_name_line_edit = QtWidgets.QLineEdit()
        self.version_name_description_label = QtWidgets.QLabel(self.current_lan.name_description)
        self.version_name_description = QtWidgets.QLineEdit()
        self.version_name_description.setMaximumWidth(150)
        version_name_layout = QtWidgets.QHBoxLayout()
        version_name_layout.addWidget(self.version_name_line_edit)
        version_name_layout.addWidget(self.version_name_description_label)
        version_name_layout.addWidget(self.version_name_description)
        # 上传框
        self.uploaded_label = QtWidgets.QLabel(self.current_lan.upload)
        self.uploaded_list = Drop_List()
        self.uploaded_list.setMaximumHeight(60)
        self.uploaded_list.setViewMode(QtWidgets.QListView.IconMode)
        self.uploaded_list.setWrapping(False)
        self.uploaded_list.setFlow(QtWidgets.QListView.LeftToRight)
        self.uploaded_list.setHorizontalScrollMode(QtWidgets.QListWidget.ScrollPerPixel)
        self.uploaded_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.uploaded_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # 清空上传按钮
        self.clear_uploaded_button = QtWidgets.QPushButton(self.current_lan.clear)
        self.uploaded_layout = QtWidgets.QVBoxLayout()
        self.uploaded_layout.addWidget(self.uploaded_list)
        self.uploaded_layout.addWidget(self.clear_uploaded_button)
        self.uploaded_layout.setSpacing(0)
        self.uploaded_layout.setMargin(0)
        # 描述
        self.description_label = QtWidgets.QLabel(self.current_lan.description)
        self.description_text_edit = QtWidgets.QTextEdit()
        # # 任务总用时
        # self.time_logged_label = QtWidgets.QLabel("任务总用时")
        # self.time_logged_num_label = QtWidgets.QLabel("0天")
        # 当前版本用时
        self.current_time_logged_label = QtWidgets.QLabel(self.current_lan.time_logged)
        self.current_time_logged_spinbox = QtWidgets.QSpinBox()
        self.current_time_logged_spinbox.setMaximumWidth(50)
        self.current_time_logged_spinbox.setMaximum(999)
        # 提交按钮
        self.submit_button = QtWidgets.QPushButton(self.current_lan.submit)

        grid_layout = QtWidgets.QGridLayout(self)
        grid_layout.addWidget(self.version_name_label, 0, 0)
        grid_layout.addLayout(version_name_layout, 0, 1)
        grid_layout.addWidget(self.uploaded_label, 1, 0)
        grid_layout.addLayout(self.uploaded_layout, 1, 1)
        grid_layout.addWidget(self.description_label, 2, 0)
        grid_layout.addWidget(self.description_text_edit, 3, 1)
        grid_layout.addWidget(self.description_label, 3, 0)
        grid_layout.addWidget(self.description_text_edit, 3, 1)
        grid_layout.addWidget(self.current_time_logged_label, 4, 0)
        grid_layout.addWidget(self.current_time_logged_spinbox, 4, 1)
        grid_layout.addWidget(self.submit_button, 5, 0, 1, 0)


    def __init_connect(self):
        self.uploaded_list.drop_file.connect(self.replace_uploaded_item)
        self.clear_uploaded_button.clicked.connect(self.uploaded_list.clear)
        #self.submit_button.clicked.connect(self.get_current_edit_info)

    def clear_info(self):
        self.version_name_line_edit.clear()
        self.version_name_description.clear()
        self.uploaded_list.clear()
        self.description_text_edit.clear()
        self.current_time_logged_spinbox.setValue(0)

    def clear_version_name(self):
        self.version_name_line_edit.clear()
        self.version_name_description.clear()

    def add_uploaded_item(self, path):
        img_icon = QtGui.QIcon()
        img_icon.addFile(path)
        item = QtWidgets.QListWidgetItem(img_icon, os.path.basename(path))
        item.file = path
        self.uploaded_list.addItem(item)

    def replace_uploaded_item(self, path):
        self.uploaded_list.clear()
        self.add_uploaded_item(path)

    def get_current_edit_info(self):
        current_edit_info = {"version_name": None,
                             "upload_files": [],
                             "description": None,
                             "logged_time": 0}

        current_edit_info["version_name"] = self.version_name_line_edit.text()

        uploaded_list_count = self.uploaded_list.count()
        for item in range(uploaded_list_count):
            current_edit_info["upload_files"].append(self.uploaded_list.item(item).file)

        current_edit_info["description"] = self.description_text_edit.toPlainText()
        current_edit_info["logged_time"] = self.current_time_logged_spinbox.value()

        return current_edit_info

    @QtCore.Slot(str, str)
    def messagebox(self, type, info):
        if type == "warning":
            QtWidgets.QMessageBox.warning(self, self.current_lan.submission_status, info, QtWidgets.QMessageBox.Ok)
        if type == "critical":
            QtWidgets.QMessageBox.critical(self, self.current_lan.submission_status, info, QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, self.current_lan.submission_status, info, QtWidgets.QMessageBox.Ok)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    cw = Creator_Widget()
    cw.show()
    sys.exit(app.exec_())