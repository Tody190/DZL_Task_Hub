# -*- coding: utf-8 -*-
__author__ = "yangtao"

import sys
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui




class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ok = "OK"
        self.cancel = "Cancel"

        self.__init_ui()
        self.__init_connect()

    def __init_ui(self):
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.setMinimumSize(350, 160)
        # shotgun url
        sgurl_label = QtWidgets.QLabel("shotgun 地址: ")
        self.sgurl_edit = QtWidgets.QLineEdit()
        # login name
        logname_label = QtWidgets.QLabel("用户名: ")
        self.logname_edit = QtWidgets.QLineEdit()
        # password
        password_label = QtWidgets.QLabel("密码: ")
        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        # user
        user_label = QtWidgets.QLabel("当前身份: ")
        self.user_edit = QtWidgets.QLineEdit()
        self.user_edit.setPlaceholderText("身份同为登录账户时，此处为空")
        # button
        self.cancel_button = QtWidgets.QPushButton(self.cancel)
        self.login_button = QtWidgets.QPushButton(self.ok)
        self.login_button.setDefault(True)

        # layout
        form_layout = QtWidgets.QFormLayout()
        form_layout.setLabelAlignment(QtCore.Qt.AlignRight)
        form_layout.setFormAlignment(QtCore.Qt.AlignLeft)
        form_layout.addRow(sgurl_label, self.sgurl_edit)
        form_layout.addRow(logname_label, self.logname_edit)
        form_layout.addRow(password_label, self.password_edit)
        form_layout.addRow(user_label, self.user_edit)

        button_groups = QtWidgets.QHBoxLayout()
        button_groups.addWidget(self.cancel_button)
        button_groups.addWidget(self.login_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_groups)

    def __init_connect(self):
        self.login_button.clicked.connect(self.__button_click)
        self.cancel_button.clicked.connect(self.__button_click)

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
                                              "登陆失败",
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
