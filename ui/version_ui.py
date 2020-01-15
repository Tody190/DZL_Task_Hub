# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets




class Versions_Widget(QtWidgets.QTableWidget):
    def __init__(self):
        super(Versions_Widget, self).__init__()
        self.verticalHeader().setHidden(True)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.horizontalHeader().setStretchLastSection(True)

    def clear_items(self):
        self.setColumnCount(0)
        self.setRowCount(0)
        self.clear()

    def add_item(self, head_labels, items_info):
        # 设置列头和列
        self.setColumnCount(len(head_labels))
        self.setHorizontalHeaderLabels(head_labels)

        # 设置行
        self.setRowCount(len(items_info))
        for row in range(len(items_info)):
            column_text_list = items_info[row]
            for column in range(len(column_text_list)):
                item_text = column_text_list[column]
                item = QtWidgets.QTableWidgetItem(item_text)
                self.setItem(row, column, item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication()
    mw = Versions_Widget()
    mw.clear_items()
    mw.add_item(['type', 'id', 'code', 'created_at', 'description'],
                [['Version', '25880', 'WTS_b15020_concept_v02', '2020-01-14 18:03:47+08:00', 'SKX'],
                 ['Version', '25879', 'WTS_b15020_concept_colorkey_a', '2020-01-14 18:02:35+08:00', 'SKX'],
                 ['Version', '25870', 'WTS_b15020_concept_colorkey_b', '2020-01-14 17:18:46+08:00', 'SKX'],
                 ['Version', '25851', 'WTS_b15020_concept_v02', '2020-01-13 17:15:33+08:00', 'SKX'],
                 ['Version', '25850', 'WTS_b15020_concept_colorkey_b', '2020-01-13 17:09:55+08:00', 'SKX'],
                 ['Version', '25838', 'WTS_b15020_concept_colorkey_a_v02', '2020-01-13 16:04:24+08:00', 'SKX，去掉多余辉光效果'],
                 ['Version', '25815', 'WTS_Colorkey_b15020_v1', '2020-01-10 10:55:23+08:00', '太阳光从正面打过来']])
    mw.show()
    sys.exit(app.exec_())