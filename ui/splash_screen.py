# -*- coding: utf-8 -*-
__author__ = "yangtao"

import os
import sys
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore



class Screen(QtWidgets.QSplashScreen):
    def __init__(self, screen_imgs_path, parent=None,):
        super(Screen, self).__init__(parent)
        self.screen_imgs_path = screen_imgs_path

    def show_screen(self, screen_img_name=None, message=None):
        if screen_img_name:
            imgs_list = os.listdir(self.screen_imgs_path)
            if screen_img_name in imgs_list:
                screen_img_path = os.path.join(self.screen_imgs_path, screen_img_name)
                screen_img_pix = QtGui.QPixmap(screen_img_path)
                self.setPixmap(screen_img_pix)
            if message:
                self.show_message(message)
            self.show()

    def show_message(self, message):
        self.showMessage(message, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.white)