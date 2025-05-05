import sys
import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from stats import Stat


class Stat_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setwindowtitle = "Character Stats"
        
        strength = Stat('strength')
        widget = QWidget()
        label = QLabel()
        label.setText(', '.join([str(val) for val in [strength.name, 
                                                      strength.level]]))


        self.setCentralWidget(label)

app = QApplication()
window = Stat_Window()
window.show()

sys.exit(app.exec())

