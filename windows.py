import sys
import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from stats import Stat




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setwindowtitle = "Character Stats"
        central_widget = QWidget()
        central_layout = QGridLayout(central_widget)
        central_widget.setLayout(central_layout)

        #####left side of the screen
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_widget.setLayout(left_layout)

        left_text = QLabel("Left")
        left_layout.addWidget(left_text)
        left_text.setAlignment(Qt.AlignCenter )

       ###### Right side of the screen 
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_widget.setLayout(right_layout)
        
        right_text = QLabel("right")
        right_layout.addWidget(right_text)
        right_text.setAlignment(Qt.AlignCenter)

        #####central buttons 
        Exit_Button = QPushButton("Quit")
        Exit_Button.clicked.connect(self.close)
        left_hide_button = QPushButton("Hide/Show")

        ##### Main Layout ########
        central_layout.addWidget(left_widget,0,0)
        central_layout.addWidget(right_widget,0,3)
        central_layout.addWidget(Exit_Button,1,1)
        central_layout.addWidget(left_hide_button,1,0)
        self.setCentralWidget(central_widget)

        ######## The Menu #######
        menu = self.menuBar()
        #File menu#
        file_menu = menu.addMenu("File")
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close)
        ### Menu addition ###
        file_menu.addAction(quit_action)

        stylesheet = """
            QLabel{
                background-color: green;
                border: 2px solid blue;
                
            }
            """
        
        self.setStyleSheet(stylesheet)
    def hide_show(self):
        pass


    


class Character_Stat_Screen(QFrame):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication()
    app.setStyle('Fusion')

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
