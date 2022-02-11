import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import os

# def movie_card():
# 	path = os.path.dirname(os.path.abspath(__file__))
# 	movie_container = qtw.QWidget()
# 	movie_container.setLayout(qtw.QVBoxLayout())
# 	label = qtw.QLabel()
# 	pixmap = QPixmap(os.path.join(path, '..\\res\\wd-poster.jpg'))
# 	pixmap2 = pixmap.scaled(340, 340, QtCore.Qt.KeepAspectRatio)
# 	label.setPixmap(pixmap2)

# 	title = qtw.QLabel(text='Movie')
# 	title.setStyleSheet("QLabel {color: red;}")

# 	movie_container.layout().addWidget(label)
# 	movie_container.layout().addWidget(title)
# 	return movie_container

class MovieCard:
	def __init__(self, _title):
		self.container = qtw.QWidget()
		self.container.setLayout(qtw.QVBoxLayout())
		self.path = os.path.dirname(os.path.abspath(__file__))
		self.set_image()
		self.set_title(_title)

	def set_image(self):
		label = qtw.QLabel()
		pixmap = QPixmap(os.path.join(self.path, '..\\res\\wd-poster.jpg'))
		pixmap2 = pixmap.scaled(340, 340, QtCore.Qt.KeepAspectRatio)
		label.setPixmap(pixmap2)
		self.container.layout().addWidget(label)

	def set_title(self, _title):
		title = qtw.QLabel(text=_title)
		title.setStyleSheet("QLabel {color: red;}")
		self.container.layout().addWidget(title)

	def get_widget(self):
		return self.container