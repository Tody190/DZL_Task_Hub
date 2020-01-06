# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets
from PySide2 import QtGui




class Message_Box(QtWidgets.QMessageBox):
    def __init__(self, icon):
        super(Message_Box, self).__init__()
        self.setWindowIcon(QtGui.QIcon(icon))

    def __msg_info(self, title, text, buttons):
        self.setWindowTitle(title)
        self.setText(text)
        if buttons:
            self.setStandardButtons(buttons)
        self.exec()
        return self.clickedButton()

    def warning(self, text, buttons=None):
        self.setIcon(QtWidgets.QMessageBox.Warning)
        return self.__msg_info("警告", text, buttons)