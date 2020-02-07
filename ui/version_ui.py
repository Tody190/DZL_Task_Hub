# -*- coding: utf-8 -*-
__author__ = "yangtao"


from PySide2 import QtWidgets
from PySide2 import QtCore




class Versions_Widget(QtWidgets.QTableWidget):
    def __init__(self):
        super(Versions_Widget, self).__init__()
        self.verticalHeader().setHidden(True)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.horizontalHeader().setStretchLastSection(True)
        # 不能编辑
        #self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 选中一行
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 只能单选
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # 添加删除按钮
        self.del_button = QtWidgets.QPushButton(self)
        self.del_button.setText("删除")
        self.del_button.setVisible(False)
        #self.del_button.setMaximumWidth(100)
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(30, 0, 30, 10)
        main_layout.addStretch()
        main_layout.addWidget(self.del_button)
        #main_layout.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)

    def clear_items(self):
        self.setColumnCount(0)
        self.setRowCount(0)
        self.clear()

    def set_head_labels(self, head_labels):
        # 设置列头和列
        self.setColumnCount(len(head_labels))
        self.setHorizontalHeaderLabels(head_labels)

    def add_row(self):
        row_index = self.rowCount()
        self.setRowCount(row_index + 1)
        return row_index

    def add_item(self, id, created_time, item_info):
        row_index = self.add_row()
        for column in range(len(item_info)):
            item = QtWidgets.QTableWidgetItem(item_info[column])
            # 添加属性
            item.id = id
            item.created_time = created_time
            self.setItem(row_index, column, item)

    def add_items(self, head_labels, items_info):
        self.set_head_labels(head_labels)
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
    mw.add_items(['type', 'id', 'code', 'created_at', 'description'],
                [['Version', '25880', 'WTS_b15020_concept_v02', '2020-01-14 18:03:47+08:00', 'SKX'],
                 ['Version', '25879', 'WTS_b15020_concept_colorkey_a', '2020-01-14 18:02:35+08:00', 'SKX'],
                 ['Version', '25870', 'WTS_b15020_concept_colorkey_b', '2020-01-14 17:18:46+08:00', 'SKX'],
                 ['Version', '25851', 'WTS_b15020_concept_v02', '2020-01-13 17:15:33+08:00', 'SKX'],
                 ['Version', '25850', 'WTS_b15020_concept_colorkey_b', '2020-01-13 17:09:55+08:00', 'SKX'],
                 ['Version', '25838', 'WTS_b15020_concept_colorkey_a_v02', '2020-01-13 16:04:24+08:00', 'SKX，去掉多余辉光效果'],
                 ['Version', '25815', 'WTS_Colorkey_b15020_v1', '2020-01-10 10:55:23+08:00', '太阳光从正面打过来']])
    # mw.add_item(['id', 'code', 'sg_status_list', 'created_at', 'description'],
    #             [['25869', 'WTS_b35290_concept_v02', 'apr', '2020-01-14 17:13:19+08:00', 'WTS_keylight_b35290_v01_200113'], ['25852', 'WTS_b35290_concept_v01', 'na', '2020-01-13 17:32:30+08:00', 'WTS_keylight_b35290_v01_200113']])
    mw.show()
    sys.exit(app.exec_())