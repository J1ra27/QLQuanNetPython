# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 655)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 931, 661))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setStyleSheet("background-color: rgb(232, 222, 255);\n"
"font: 63 10pt \"Segoe UI Semibold\";")
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.tabWidget.setIconSize(QtCore.QSize(60, 40))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab1.setStyleSheet("")
        self.tab1.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.tab1.setObjectName("tab1")
        self.groupBox = QtWidgets.QGroupBox(self.tab1)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 351))
        self.groupBox.setStyleSheet("background-color: rgb(164, 255, 195);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.user_tbox = QtWidgets.QLineEdit(self.groupBox)
        self.user_tbox.setGeometry(QtCore.QRect(160, 100, 211, 31))
        self.user_tbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_tbox.setObjectName("user_tbox")
        self.pass_tbox = QtWidgets.QLineEdit(self.groupBox)
        self.pass_tbox.setGeometry(QtCore.QRect(160, 170, 211, 31))
        self.pass_tbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pass_tbox.setObjectName("pass_tbox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 100, 121, 31))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 121, 31))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 240, 121, 31))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.tiennap_cbox = QtWidgets.QComboBox(self.groupBox)
        self.tiennap_cbox.setGeometry(QtCore.QRect(160, 240, 211, 31))
        self.tiennap_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tiennap_cbox.setObjectName("tiennap_cbox")
        self.tiennap_cbox.addItem("")
        self.tiennap_cbox.addItem("")
        self.tiennap_cbox.addItem("")
        self.tiennap_cbox.addItem("")
        self.tiennap_cbox.addItem("")
        self.tiennap_cbox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 121, 31))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.time_label = QtWidgets.QLabel(self.groupBox)
        self.time_label.setGeometry(QtCore.QRect(160, 300, 211, 31))
        self.time_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.id_tbox = QtWidgets.QLineEdit(self.groupBox)
        self.id_tbox.setEnabled(False)
        self.id_tbox.setGeometry(QtCore.QRect(160, 40, 211, 31))
        self.id_tbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_tbox.setObjectName("id_tbox")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab1)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 370, 391, 231))
        self.groupBox_3.setStyleSheet("background-color: rgb(164, 255, 195);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.add_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.add_btn.setGeometry(QtCore.QRect(20, 40, 101, 71))
        self.add_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.add_btn.setObjectName("add_btn")
        self.update_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.update_btn.setGeometry(QtCore.QRect(150, 40, 101, 71))
        self.update_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.update_btn.setObjectName("update_btn")
        self.delete_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_btn.setGeometry(QtCore.QRect(20, 140, 101, 71))
        self.delete_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_btn.setObjectName("delete_btn")
        self.clear_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.clear_btn.setGeometry(QtCore.QRect(150, 140, 101, 71))
        self.clear_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clear_btn.setObjectName("clear_btn")
        self.load_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.load_btn.setGeometry(QtCore.QRect(280, 80, 101, 71))
        self.load_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.load_btn.setObjectName("load_btn")
        self.sql_tv = QtWidgets.QTableWidget(self.tab1)
        self.sql_tv.setEnabled(True)
        self.sql_tv.setGeometry(QtCore.QRect(410, 10, 501, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sql_tv.sizePolicy().hasHeightForWidth())
        self.sql_tv.setSizePolicy(sizePolicy)
        self.sql_tv.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sql_tv.setAutoFillBackground(False)
        self.sql_tv.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"header.setSectionResizeMode(col, header.ResizeToContents)")
        self.sql_tv.setInputMethodHints(QtCore.Qt.ImhNoEditMenu)
        self.sql_tv.setObjectName("sql_tv")
        self.sql_tv.setColumnCount(4)
        self.sql_tv.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sql_tv.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_tv.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_tv.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_tv.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.tab_2.setFont(font)
        self.tab_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab_2.setLocale(QtCore.QLocale(QtCore.QLocale.Vietnamese, QtCore.QLocale.Vietnam))
        self.tab_2.setObjectName("tab_2")
        self.sql_may = QtWidgets.QTableWidget(self.tab_2)
        self.sql_may.setGeometry(QtCore.QRect(10, 400, 901, 211))
        self.sql_may.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sql_may.setObjectName("sql_may")
        self.sql_may.setColumnCount(5)
        self.sql_may.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sql_may.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_may.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_may.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_may.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_may.setHorizontalHeaderItem(4, item)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 10, 671, 371))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(188, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.id_may = QtWidgets.QLineEdit(self.groupBox_2)
        self.id_may.setEnabled(False)
        self.id_may.setGeometry(QtCore.QRect(190, 30, 241, 31))
        self.id_may.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_may.setObjectName("id_may")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(80, 30, 111, 31))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.cpu_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.cpu_txt.setEnabled(True)
        self.cpu_txt.setGeometry(QtCore.QRect(190, 90, 241, 31))
        self.cpu_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cpu_txt.setObjectName("cpu_txt")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(80, 90, 111, 31))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.gpu_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.gpu_txt.setEnabled(True)
        self.gpu_txt.setGeometry(QtCore.QRect(190, 150, 241, 31))
        self.gpu_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gpu_txt.setObjectName("gpu_txt")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(80, 150, 111, 31))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.ram_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.ram_txt.setEnabled(True)
        self.ram_txt.setGeometry(QtCore.QRect(190, 210, 241, 31))
        self.ram_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ram_txt.setObjectName("ram_txt")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(80, 210, 111, 31))
        self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(80, 270, 111, 31))
        self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.tinhtrang_cbox = QtWidgets.QComboBox(self.groupBox_2)
        self.tinhtrang_cbox.setGeometry(QtCore.QRect(190, 270, 241, 31))
        self.tinhtrang_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tinhtrang_cbox.setObjectName("tinhtrang_cbox")
        self.tinhtrang_cbox.addItem("")
        self.tinhtrang_cbox.addItem("")
        self.tinhtrang_cbox.addItem("")
        self.tinhtrang_cbox.addItem("")
        self.tinhtrang_cbox.addItem("")
        self.tinhtrang_cbox.setItemText(4, "")
        self.fixm_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.fixm_btn.setGeometry(QtCore.QRect(490, 220, 151, 81))
        self.fixm_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.fixm_btn.setObjectName("fixm_btn")
        self.clear_btn2 = QtWidgets.QPushButton(self.groupBox_2)
        self.clear_btn2.setGeometry(QtCore.QRect(490, 30, 151, 81))
        self.clear_btn2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.clear_btn2.setObjectName("clear_btn2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.sql_his = QtWidgets.QTableWidget(self.tab_3)
        self.sql_his.setGeometry(QtCore.QRect(10, 10, 901, 601))
        self.sql_his.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sql_his.setObjectName("sql_his")
        self.sql_his.setColumnCount(4)
        self.sql_his.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.sql_his.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_his.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_his.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sql_his.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý quán NET"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông Tin"))
        self.label.setText(_translate("MainWindow", "Tên tài khoản :"))
        self.label_2.setText(_translate("MainWindow", "Mật khẩu :"))
        self.label_3.setText(_translate("MainWindow", "Tiền nạp :"))
        self.tiennap_cbox.setItemText(0, _translate("MainWindow", "..."))
        self.tiennap_cbox.setItemText(1, _translate("MainWindow", "10000"))
        self.tiennap_cbox.setItemText(2, _translate("MainWindow", "20000"))
        self.tiennap_cbox.setItemText(3, _translate("MainWindow", "50000"))
        self.tiennap_cbox.setItemText(4, _translate("MainWindow", "100000"))
        self.tiennap_cbox.setItemText(5, _translate("MainWindow", "200000"))
        self.label_4.setText(_translate("MainWindow", "Thời gian :"))
        self.label_5.setText(_translate("MainWindow", "ID :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chức Năng"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.update_btn.setText(_translate("MainWindow", "Update"))
        self.delete_btn.setText(_translate("MainWindow", "Delete"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.load_btn.setText(_translate("MainWindow", "Refresh"))
        item = self.sql_tv.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.sql_tv.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên tài khoản"))
        item = self.sql_tv.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mật khẩu"))
        item = self.sql_tv.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thời gian còn"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tài Khoản Thành Viên"))
        item = self.sql_may.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.sql_may.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPU"))
        item = self.sql_may.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "GPU"))
        item = self.sql_may.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "RAM"))
        item = self.sql_may.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tình trạng"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Quản thông tin máy"))
        self.label_6.setText(_translate("MainWindow", "Id máy:"))
        self.label_7.setText(_translate("MainWindow", "CPU:"))
        self.label_8.setText(_translate("MainWindow", "GPU:"))
        self.label_9.setText(_translate("MainWindow", "RAM:"))
        self.label_10.setText(_translate("MainWindow", "Tình trạng"))
        self.tinhtrang_cbox.setItemText(0, _translate("MainWindow", "available"))
        self.tinhtrang_cbox.setItemText(1, _translate("MainWindow", "used"))
        self.tinhtrang_cbox.setItemText(2, _translate("MainWindow", "disable"))
        self.tinhtrang_cbox.setItemText(3, _translate("MainWindow", "maintained"))
        self.fixm_btn.setText(_translate("MainWindow", "Thay đổi thông tin"))
        self.clear_btn2.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Quản Lý Máy"))
        item = self.sql_his.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Log Id"))
        item = self.sql_his.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id Khách hàng"))
        item = self.sql_his.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Máy"))
        item = self.sql_his.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thời gian đăng nhập"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Lịch Sử Đăng Nhập"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
