from interface import UI as UI
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = UI()
	app.exec_()