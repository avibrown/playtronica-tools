from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import keyboard
import sys
import quantizer
import time

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
		uic.loadUi('ui.ui', self)
		
		self.threadpool = QThreadPool()

		self.sample_pack_path = None
		
		self.load_sample_pack_button = self.findChild(QtWidgets.QPushButton, 'load_sample_pack_button')
		self.tempo_label = self.findChild(QtWidgets.QLabel, 'tempo_label')
		self.tempo_slider = self.findChild(QtWidgets.QSlider, 'tempo_slider')
		self.metronome_radio_button = self.findChild(QtWidgets.QCheckBox, 'metronome_radio_button')
		self.quantize_radio_button = self.findChild(QtWidgets.QCheckBox, 'quantize_radio_button')
		self.play_button = self.findChild(QtWidgets.QPushButton, 'playtronic_button')

		self.tempo_slider.valueChanged.connect(self.tempo_value)
		self.load_sample_pack_button.clicked.connect(self.load_sample_pack)
		self.play_button.clicked.connect(self.session_thread)
		
		self.show()
	
	def session_thread(self, *args, **kwargs):
		thread = Worker(quantizer.Player,
						self.quantize_radio_button.isChecked(),
						self.sample_pack_path,
						self.metronome_radio_button.isChecked(), 
						self.tempo_slider.value()
						) 
		self.threadpool.start(thread)

	def tempo_value(self):
		self.tempo_label.setText(f'Tempo: {self.tempo_slider.value()}')

	def load_sample_pack(self):
		dialog = QtWidgets.QFileDialog(self)
		folder = dialog.getExistingDirectory()
		self.sample_pack_path = folder


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = UI()
	app.exec_()