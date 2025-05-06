import sys
import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from stats import Stat


class Stat_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setwindowtitle = "Character Stats"
        
        widget = QWidget()
        self.setCentralWidget(widget)

class Character_Stat_Screen(QFrame):
    def __init__(self):
        super().__init__()


app = QApplication()
window = Stat_Window()
window.show()

sys.exit(app.exec())

