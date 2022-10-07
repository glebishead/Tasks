import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from flag import Ui_MainWindow


class Flag(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		
		self.setupUi(self)
		self.setWindowTitle('Текстовый флаг')
		self.pushButton.clicked.connect(self.show_info)
		
	def show_info(self):
		result = ["Цвета:"]
		if self.radioButton.isChecked():
			result.append(self.radioButton.text())
		elif self.radioButton_2.isChecked():
			result.append(self.radioButton_2.text())
		elif self.radioButton_3.isChecked():
			result.append(self.radioButton_3.text())
		
		if self.radioButton_4.isChecked():
			result.append(self.radioButton_4.text())
		elif self.radioButton_5.isChecked():
			result.append(self.radioButton_5.text())
		elif self.radioButton_6.isChecked():
			result.append(self.radioButton_6.text())
		
		if self.radioButton_7.isChecked():
			result.append(self.radioButton_7.text())
		elif self.radioButton_8.isChecked():
			result.append(self.radioButton_8.text())
		elif self.radioButton_9.isChecked():
			result.append(self.radioButton_9.text())
		
		if self.radioButton_10.isChecked():
			result.append(self.radioButton_10.text())
		elif self.radioButton_11.isChecked():
			result.append(self.radioButton_11.text())
		elif self.radioButton_12.isChecked():
			result.append(self.radioButton_12.text())
		
		self.label_5.setText(", ".join(result).replace(',', '', 1))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Flag()
	ex.setFixedSize(565, 240)
	ex.show()
	sys.exit(app.exec())