import sys
import time

import keyboard
from PyQt5 import QtWidgets, uic
from PyQt5.Qt import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import quantizer


# Class responsible for opening new threads for processes
class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.func(*self.args, **self.kwargs)


# Main UI class
class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui.ui", self)

        self.threadpool = QThreadPool()

        self.sample_pack_path = None

        self.load_sample_pack_button = self.findChild(
            QtWidgets.QPushButton, "load_sample_pack_button"
        )
        self.tempo_label = self.findChild(QtWidgets.QLabel, "tempo_label")
        self.tempo_slider = self.findChild(QtWidgets.QSlider, "tempo_slider")
        self.metronome_radio_button = self.findChild(
            QtWidgets.QCheckBox, "metronome_radio_button"
        )
        self.quantize_radio_button = self.findChild(
            QtWidgets.QCheckBox, "quantize_radio_button"
        )
        self.play_button = self.findChild(QtWidgets.QPushButton, "playtronic_button")

        self.tempo_slider.valueChanged.connect(self.tempo_value)
        self.load_sample_pack_button.clicked.connect(self.load_sample_pack)
        self.play_button.clicked.connect(self.session_thread)

        self.show()

    def session_thread(self, *args, **kwargs):
        if self.sample_pack_path:
            thread = Worker(
                quantizer.Player,
                self.quantize_radio_button.isChecked(),
                self.sample_pack_path,
                self.metronome_radio_button.isChecked(),
                self.tempo_slider.value(),
            )
            self.threadpool.start(thread)
            self.play_button.setEnabled(False)
            self.load_sample_pack_button.setEnabled(False)
            self.play_button.setText("R E A D Y")
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(
                "Please load a sample pack using the SAMPLES button :)"
            )
            error_dialog.exec_()

    def tempo_value(self):
        self.tempo_label.setText(f"Tempo: {self.tempo_slider.value()}")

    def load_sample_pack(self):
        dialog = QtWidgets.QFileDialog(self)
        folder = dialog.getExistingDirectory()
        self.sample_pack_path = folder
        self.load_sample_pack_button.setText(folder.split("/")[-1])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.play_button.setEnabled(True)
            self.play_button.setText("P L A Y T R O N")
            self.load_sample_pack_button.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec_()
