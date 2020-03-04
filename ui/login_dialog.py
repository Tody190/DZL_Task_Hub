# -*- coding: utf-8 -*-
__author__ = "yangtao"

import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from core import language




class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ok = "OK"
        self.cancel = "Cancel"

        # 界面语言
        self.lan = language.lan()
        self.current_lan = self.lan.get_language()

        self.__init_ui()
        self.__init_connect()

    def __init_ui(self):
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setMinimumSize(350, 160)
        # shotgun url
        sgurl_label = QtWidgets.QLabel(self.current_lan.shotgun_url)
        self.sgurl_edit = QtWidgets.QLineEdit()
        # login name
        logname_label = QtWidgets.QLabel(self.current_lan.user_name)
        self.logname_edit = QtWidgets.QLineEdit()
        # password
        password_label = QtWidgets.QLabel(self.current_lan.password)
        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        # user
        user_label = QtWidgets.QLabel(self.current_lan.current_user)
        self.user_edit = QtWidgets.QLineEdit()
        self.user_edit.setPlaceholderText(self.current_lan.current_user_placeholder_text)
        # lan
        language_label = QtWidgets.QLabel(self.current_lan.language)
        self.language_combobox = QtWidgets.QComboBox()
        # button
        self.cancel_button = QtWidgets.QPushButton(self.cancel)
        self.login_button = QtWidgets.QPushButton(self.ok)
        self.login_button.setDefault(True)

        # layout
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(sgurl_label, 0, 0)
        grid_layout.addWidget(self.sgurl_edit, 0, 1)
        grid_layout.addWidget(logname_label, 1, 0)
        grid_layout.addWidget(self.logname_edit, 1, 1)
        grid_layout.addWidget(password_label, 2, 0)
        grid_layout.addWidget(self.password_edit, 2, 1)
        grid_layout.addWidget(user_label, 3, 0)
        grid_layout.addWidget(self.user_edit, 3, 1)
        grid_layout.addWidget(language_label, 4, 0)
        grid_layout.addWidget(self.language_combobox, 4, 1)

        button_groups = QtWidgets.QHBoxLayout()
        button_groups.addWidget(self.cancel_button)
        button_groups.addWidget(self.login_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(grid_layout)
        main_layout.addLayout(button_groups)

    def __init_connect(self):
        self.login_button.clicked.connect(self.__button_click)
        self.cancel_button.clicked.connect(self.__button_click)

    def set_language_box(self, language_list, current_language):
        self.language_combobox.addItems(language_list)
        self.language_combobox.setCurrentText(current_language)

    def set_title(self, name, icon_path=None):
        self.setWindowTitle(name)
        if icon_path:
            self.setWindowIcon(QtGui.QIcon(icon_path))

    def set_defaults_values(self, sgurl, logname, user):
        if sgurl:
            self.sgurl_edit.setText(sgurl)
        if logname:
            self.logname_edit.setText(logname)
        if user:
            self.user_edit.setText(user)

    def get_current_values(self):
        user = self.user_edit.text()
        if not user:
            user = self.logname_edit.text()
        return {"sgurl":self.sgurl_edit.text(),
                "logname": self.logname_edit.text(),
                "password": self.password_edit.text(),
                "user": user}

    def __button_click(self):
        if self.sender().text() == self.ok:
            self.done(1)
        elif self.sender().text() == self.cancel:
            self.done(0)

    def show_retry_messagebox(self, info):
        self.close()
        reply = QtWidgets.QMessageBox.critical(self,
                                              self.current_lan.login_failed,
                                              info,
                                              QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Retry)
        if reply == QtWidgets.QMessageBox.Cancel:
            self.close()
        if reply == QtWidgets.QMessageBox.Retry:
            self.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    pd = Dialog()
    pd.show()
    sys.exit(app.exec_())
