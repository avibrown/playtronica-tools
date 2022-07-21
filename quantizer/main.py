import sys

from PyQt5 import QtWidgets

from interface import UI as UI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
