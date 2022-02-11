import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def movie_card():
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    movie_container = qtw.QWidget()
    movie_container.setLayout(qtw.QVBoxLayout())
    label = qtw.QLabel()
    pixmap = QPixmap(os.path.join(path, '..\\res\\wd-poster.jpg'))
    pixmap2 = pixmap.scaled(340, 340, QtCore.Qt.KeepAspectRatio)
    label.setPixmap(pixmap2)

    title = qtw.QLabel(text='Movie')
    title.setStyleSheet("QLabel {color: red;}")

    movie_container.layout().addWidget(label)
    movie_container.layout().addWidget(title)
    return movie_container
