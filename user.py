import sys
from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

from hehe.user_menu import Ui_MainWindow
from hehe.login import Ui_Login
from hehe.changepass import changepass

class CountdownTimer(QtCore.QObject):
    time_changed = QtCore.pyqtSignal(str)
    timer_finished = QtCore.pyqtSignal()

    def __init__(self, time_str):
        super().__init__()
        self.time_left_seconds = self.parse_time(time_str)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)

    def parse_time(self, time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds

    def start(self):
        self.timer.start(1000)  # Update every second

    def stop(self):
        self.timer.stop()

    def update_time(self):
        if self.time_left_seconds > 0:
            self.time_left_seconds -= 1
            self.time_changed.emit(self.format_time(self.time_left_seconds))
        else:
            self.timer.stop()
            self.timer_finished.emit()

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("Đăng nhập")
        self.ui.login_btn.clicked.connect(self.login)

    def login(self):
        username = self.ui.username_text.text()
        password = self.ui.password_text.text()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python42"
            )
            cursor = db.cursor()

            query = "SELECT * FROM thanhvien WHERE user = %s AND pass = %s"
            values = (username, password)
            cursor.execute(query, values)

            if cursor.fetchone():
                self.show_user_menu(username)
            else:
                QMessageBox.warning(self, "Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Failed to connect to database: {err}")

        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    def show_user_menu(self, username):
        self.user_menu = UserMenuWindow(username)
        self.user_menu.show()
        self.close()


class UserMenuWindow(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username

        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python42"
            )
            self.cursor = self.mydb.cursor()

            sql = "SELECT Id_kh, time FROM thanhvien WHERE user = %s"
            self.cursor.execute(sql, (username,))
            result = self.cursor.fetchone()

            if result:
                self.id_kh = result[0]
                self.time_value = result[1]
            else:
                self.id_kh = None
                self.time_value = "00:00:00"

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Failed to connect to database: {err}")

        finally:
            if self.cursor:
                self.cursor.close()
            if self.mydb:
                self.mydb.close()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.idmay_text.setText("1")
        self.ui.idkh_txt.setText(str(self.id_kh))
        self.ui.user_txt.setText(username)

        self.timer = CountdownTimer(self.time_value)
        self.timer.time_changed.connect(self.ui.timeleft_text.setText)
        self.timer.timer_finished.connect(self.time_up)
        self.timer.start()

        self.ui.doimk_btn.clicked.connect(lambda: self.handle_doimk(username))
        self.ui.logout_btn.clicked.connect(self.handle_logout)
        self.insertHistory()
    def insertHistory(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python42"
        )

        # Create a cursor object using cursor() method
        mycursor = mydb.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Example INSERT statement
        sql = "INSERT INTO history (id_kh, id_may, login_time) VALUES (%s, %s, %s)"
        val = (self.id_kh, "1", current_time)

        # Execute the SQL command
        mycursor.execute(sql, val)

        # Commit changes to the database
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
    def time_up(self):
        QMessageBox.information(self, "Thông báo", "Thời gian sử dụng đã hết!")
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python42"
            )
            cursor = db.cursor()

            query = "UPDATE thanhvien SET time = %s WHERE user = %s"
            values = ("00:00:00", self.username)
            cursor.execute(query, values)
            db.commit()


        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Failed to update time in database: {err}")

        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

        self.handle_logout()
    def handle_doimk(self, username):
        self.changepass = Password(username)
        self.changepass.show()

    def handle_logout(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()


class Password(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self.ui = changepass()
        self.ui.setupUi(self)
        self.ui.change_tn.clicked.connect(self.updatepass)

    def updatepass(self):
        new_password = self.ui.newpass_txt.text()

        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python42"
            )
            cursor = db.cursor()

            query = "UPDATE thanhvien SET pass = %s WHERE user = %s"
            values = (new_password, self.username)
            cursor.execute(query, values)
            db.commit()

            QMessageBox.information(self, "Thành công", "Mật khẩu đã được cập nhật!")
            self.close()

        except mysql.connector.Error as err:
            QMessageBox.warning(self, "Lỗi", f"Failed to connect to database: {err}")

        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
