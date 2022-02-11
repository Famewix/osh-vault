import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5 import QtCore
from osh_vault.movie_card import MovieCard
import json
import os, sys

path = os.path.dirname(os.path.abspath(__file__))
with open('config.json', 'r') as f:
	config = json.load(f)

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Osh Vault")
		self.setLayout(qtw.QVBoxLayout())
		self.key_shortcuts()
		self.navbar()
		self.movies()


		self.show()
		print(self.layout().count())

	def key_shortcuts(self):
		self.shortcut_close = qtw.QShortcut(QKeySequence('Ctrl+W'), self)
		self.shortcut_close.activated.connect(lambda : app.quit())

	def navbar(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QHBoxLayout())
		
		home_btn = qtw.QPushButton()
		home_btn.setIcon(QIcon("res\\home.png"))
		movies_btn = qtw.QPushButton("Movies")
		gallery_btn = qtw.QPushButton("Gallery")
		favorite_btn = qtw.QPushButton("Favorites")
		studio_btn = qtw.QPushButton("Studios")
		settings_btn = qtw.QPushButton()
		settings_btn.setIcon(QIcon("res\\gear.png"))
		settings_btn.clicked.connect(self.open_settings)

		container.layout().addWidget(home_btn)
		container.layout().addWidget(movies_btn)
		container.layout().addWidget(gallery_btn)
		container.layout().addWidget(favorite_btn)
		container.layout().addWidget(studio_btn)
		container.layout().addWidget(settings_btn)
		self.layout().addWidget(container)

	def open_settings(self):
		if sys.platform == 'win32':
			os.system("config.json")
		else:
			os.system("open config.json")

	def movies(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		column = 0
		row = 0
		for i, _file in enumerate(os.listdir(config["BASE_DIR"])):
			movie = MovieCard(_file).get_widget()

			if column > 4:
				column = 0
				row += 1

			container.layout().addWidget(movie,row,column,1,1)
			column += 1

		self.layout().addWidget(container)


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()