# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changepass.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class changepass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 141, 31))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.newpass_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.newpass_txt.setEnabled(True)
        self.newpass_txt.setGeometry(QtCore.QRect(40, 70, 241, 41))
        self.newpass_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newpass_txt.setObjectName("newpass_txt")
        self.change_tn = QtWidgets.QPushButton(self.centralwidget)
        self.change_tn.setGeometry(QtCore.QRect(90, 140, 141, 61))
        self.change_tn.setStyleSheet("background-color: rgb(125, 255, 147);")
        self.change_tn.setObjectName("change_tn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "💩"))
        self.label_2.setText(_translate("MainWindow", "Mật khẩu mới :"))
        self.change_tn.setText(_translate("MainWindow", "Xác nhận đổi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = changepass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
