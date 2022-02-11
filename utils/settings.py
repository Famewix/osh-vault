import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtCore
import json
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(dir_path, '..\\config.json')

with open(conf_path, 'r') as f:
	config = json.load(f)

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Settings")
		self.setLayout(qtw.QVBoxLayout())
		self.key_shortcuts()
		self.inputs()

		self.show()
		print(self.layout().count())

	def key_shortcuts(self):
		self.shortcut_close = qtw.QShortcut(QKeySequence('Ctrl+W'), self)
		self.shortcut_close.activated.connect(lambda : app.quit())

	def inputs(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QFormLayout())
		# base_dir_e = qtw.QLineEdit("BASE_DIR")
		# container.layout().addRow("BASE_DIR", base_dir_e)

		for key in config:
			line_edit = qtw.QLineEdit(str(config[key]))
			line_edit.editingFinished.connect(lambda: self.edit_json(key, line_edit.text()))
			container.layout().addRow(key, line_edit)

		self.layout().addWidget(container)

	def edit_json(self, key, value):
		print(key, value)

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()