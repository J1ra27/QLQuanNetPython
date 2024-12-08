from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import mysql.connector
from hehe.main import Ui_MainWindow

def convert_to_seconds(timelabel):
    time_mapping = {
        '10000': 30,      # 30 giây
        '20000': 60,      # 1 phút = 60 giây
        '50000': 120,     # 2 phút = 120 giây
        '100000': 240,     # 4 phút = 240 giây
        '200000': 480,    # 8 phút = 480 giây
    }
    return time_mapping.get(timelabel, 0)  # Mặc định trả về 0 nếu không tìm thấy

class MAIN_HANDLE(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MAIN_HANDLE, self).__init__()
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="", database="python42")
        self.setupUi(self)
        self.showinfo()
        self.showinfocomputer()
        self.load_btn.clicked.connect(self.showinfo)
        self.tiennap_cbox.currentIndexChanged.connect(self.handle_combobox_change)
        self.add_btn.clicked.connect(self.insert_data)
        self.update_btn.clicked.connect(self.update_data)
        self.sql_tv.itemSelectionChanged.connect(self.get_item_by_select)
        self.sql_may.itemSelectionChanged.connect(self.get_item_by_select_may)
        self.delete_btn.clicked.connect(self.delete_byid)
        self.clear_btn.clicked.connect(self.clear)
        self.clear_btn2.clicked.connect(self.clear_may)
        self.fixm_btn.clicked.connect(self.update_data_may)
        self.showinfoHistory()

    def showinfo(self):
        cursor = self.mydb.cursor()
        try:
            cursor.execute("SELECT * FROM thanhvien")
            result = cursor.fetchall()

            self.sql_tv.setRowCount(len(result))
            self.sql_tv.setColumnCount(4)

            for table_row, row in enumerate(result):
                self.sql_tv.setItem(table_row, 0, QTableWidgetItem(str(row[0])))
                self.sql_tv.setItem(table_row, 1, QTableWidgetItem(row[1]))
                self.sql_tv.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
                self.sql_tv.setItem(table_row, 3, QTableWidgetItem(str(row[3])))

        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")

        finally:
            cursor.close()

    def handle_combobox_change(self, index):
        timelabel = self.tiennap_cbox.currentText()
        seconds = convert_to_seconds(timelabel)
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        self.time_label.setText(f"{hours} giờ, {minutes} phút, {seconds} giây")

    def insert_data(self):
        user_val = self.user_tbox.text()
        pass_val = self.pass_tbox.text()
        time_label_text = self.time_label.text()

        # Convert time_label_text to seconds
        time_seconds = self.convert_time_label_to_seconds(time_label_text)
        if user_val and pass_val and time_seconds:
            mycursor = self.mydb.cursor()
            sql = "INSERT INTO thanhvien (user, pass, time) VALUES (%s, %s, %s)"
            val = (user_val, pass_val, time_seconds)
            mycursor.execute(sql, val)
            self.mydb.commit()
            self.showinfo()
            QtWidgets.QMessageBox.information(None, "Success", "Data inserted successfully!")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Please fill in all fields.")

    def convert_time_label_to_seconds(self, time_label_text):
        # Assuming time_label_text is in format "x giờ, y phút, z giây"
        time_parts = time_label_text.split(',')
        hours = 0
        minutes = 0
        seconds = 0

        for part in time_parts:
            if 'giờ' in part:
                hours = int(part.split()[0])
            elif 'phút' in part:
                minutes = int(part.split()[0])
            elif 'giây' in part:
                seconds = int(part.split()[0])

        time_seconds = f"{hours:02}:{minutes:02}:{seconds:02}"
        return time_seconds

    def get_item_by_select(self):
        selected_row = self.sql_tv.currentRow()
        self.id = int(self.sql_tv.item(selected_row, 0).text())  # Assuming ID is in the first column

        cursor = self.mydb.cursor()
        try:
            sql = "SELECT Id_kh,user,pass,time FROM thanhvien WHERE Id_kh = %s"
            cursor.execute(sql, (self.id,))
            result = cursor.fetchone()

            if result:
                self.id_tbox.setText(str(result[0]))  # Convert ID to string if necessary
                self.user_tbox.setText(result[1])
                self.pass_tbox.setText(result[2])
            else:
                # Clear text boxes if no matching record found
                self.id_tbox.clear()
                self.user_tbox.clear()
                self.pass_tbox.clear()

        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")

        finally:
            cursor.close()

    def update_data(self):
        id_kh_val = self.id_tbox.text()
        user_val = self.user_tbox.text()
        pass_val = self.pass_tbox.text()
        time_label_text = self.time_label.text()

        # Convert time_label_text to seconds
        time_seconds = self.convert_time_label_to_seconds(time_label_text)
        if user_val and pass_val and time_seconds:
            mycursor = self.mydb.cursor()
            sql = """
        UPDATE thanhvien 
        SET user = %s, pass = %s, time = %s 
        WHERE id_kh = %s
        """
            val = (user_val, pass_val, time_seconds, id_kh_val)
            mycursor.execute(sql, val)
            self.mydb.commit()
            self.showinfo()
            QtWidgets.QMessageBox.information(None, "Success", "Data update successfully!")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Please fill in all fields.")

    def clear(self):
        self.id_tbox.clear()
        self.user_tbox.clear()
        self.pass_tbox.clear()
    def delete_byid(self):
        # Get the selected row and retrieve the ID
        selected_row = self.sql_tv.currentRow()
        id_to_delete = int(self.sql_tv.item(selected_row, 0).text())  # Assuming ID is in the first column

        # Execute the delete query
        mycursor = self.mydb.cursor()
        sql = "DELETE FROM thanhvien WHERE id_kh = %s"
        val = (id_to_delete,)

        try:
            mycursor.execute(sql, val)
            self.mydb.commit()
            QtWidgets.QMessageBox.information(None, "Success", f"Deleted successfully!")
            self.showinfo()  # Refresh the table view after deletion

        except mysql.connector.Error as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error deleting record: {e}")

        finally:
            mycursor.close()

    def showinfocomputer(self):
        cursor = self.mydb.cursor()
        try:
            cursor.execute("SELECT * FROM computer")
            result = cursor.fetchall()

            self.sql_may.setRowCount(len(result))
            self.sql_may.setColumnCount(5)

            for table_row, row in enumerate(result):
                self.sql_may.setItem(table_row, 0, QTableWidgetItem(str(row[0])))
                self.sql_may.setItem(table_row, 1, QTableWidgetItem(str(row[1])))
                self.sql_may.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
                self.sql_may.setItem(table_row, 3, QTableWidgetItem(str(row[3])))
                self.sql_may.setItem(table_row, 4, QTableWidgetItem(str(row[4])))

        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")

        finally:
            cursor.close()
    def get_item_by_select_may(self):
        selected_row = self.sql_may.currentRow()
        self.idmay = int(self.sql_may.item(selected_row, 0).text())  # Assuming ID is in the first column

        cursor = self.mydb.cursor()
        try:
            sql = "SELECT Id_may,CPU,GPU,RAM FROM computer WHERE id_may = %s"
            cursor.execute(sql, (self.idmay,))
            result = cursor.fetchone()

            if result:
                self.id_may.setText(str(result[0]))  # Convert ID to string if necessary
                self.cpu_txt.setText(result[1])
                self.gpu_txt.setText(result[2])
                self.ram_txt.setText(result[3])
            else:
                # Clear text boxes if no matching record found
                self.id_may.clear()
                self.cpu_text.clear()
                self.gpu_text.clear()
                self.ram_text.clear()

        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")

        finally:
            cursor.close()

    def update_data_may(self):
        id_may_val = self.id_may.text()
        cpu_val = self.cpu_txt.text()
        gpu_val = self.gpu_txt.text()
        ram_val = self.ram_txt.text()
        tinhtrang_val = self.tinhtrang_cbox.currentText()

        if cpu_val and gpu_val and ram_val and tinhtrang_val:
            mycursor = self.mydb.cursor()
            sql = """
        UPDATE computer 
        SET cpu = %s, gpu = %s, ram = %s ,tinhtrang = %s 
        WHERE id_may = %s
        """
            val = (cpu_val, gpu_val, ram_val, tinhtrang_val, id_may_val)
            mycursor.execute(sql, val)
            self.mydb.commit()
            self.showinfocomputer()
            QtWidgets.QMessageBox.information(None, "Success", "Data update successfully!")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Please fill in all fields.")

    def clear_may(self):
        self.id_may.clear()
        self.cpu_txt.clear()
        self.gpu_txt.clear()
        self.ram_txt.clear()

    def showinfoHistory(self):
        cursor = self.mydb.cursor()
        try:
            cursor.execute("SELECT * FROM history")
            result = cursor.fetchall()

            self.sql_his.setRowCount(len(result))
            self.sql_his.setColumnCount(4)

            for table_row, row in enumerate(result):
                self.sql_his.setItem(table_row, 0, QTableWidgetItem(str(row[0])))
                self.sql_his.setItem(table_row, 1, QTableWidgetItem(str(row[1])))
                self.sql_his.setItem(table_row, 2, QTableWidgetItem(str(row[2])))
                self.sql_his.setItem(table_row, 3, QTableWidgetItem(str(row[3])))

        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL: {e}")

        finally:
            cursor.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MAIN_HANDLE()
    ui.show()
    sys.exit(app.exec_())
