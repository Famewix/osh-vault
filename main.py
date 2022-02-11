import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
from osh_vault.movie_card import movie_card

class MainWindow(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Osh Vault")
		self.setLayout(qtw.QVBoxLayout())
		self.navbar()
		self.movies()

		self.show()
	def navbar(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QHBoxLayout())
		home_btn = qtw.QPushButton("Home")
		movies_btn = qtw.QPushButton("Movies")
		gallery_btn = qtw.QPushButton("Gallery")
		favorite_btn = qtw.QPushButton("Favorites")
		studio_btn = qtw.QPushButton("Studios")
		settings_btn = qtw.QPushButton("Settings")

		container.layout().addWidget(home_btn)
		container.layout().addWidget(movies_btn)
		container.layout().addWidget(gallery_btn)
		container.layout().addWidget(favorite_btn)
		container.layout().addWidget(studio_btn)
		container.layout().addWidget(settings_btn)
		self.layout().addWidget(container)

	def movies(self):
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())
		movie = movie_card()
		movie2 = movie_card()
		container.layout().addWidget(movie,0,0,1,1)
		container.layout().addWidget(movie2,0,1,1,1)
		self.layout().addWidget(container)


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()