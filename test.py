import os
import pickle
from Character import Character
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.center_widget = QWidget()
        self.setCentralWidget(self.center_widget)
        self.center_layout = QVBoxLayout()
        self.center_widget.setLayout(self.center_layout)

        #self.name = QLabel()
        #self.name_change = QTextEdit()
        #self.name_change_button = QPushButton("change name")
        #self.name_change_button.clicked.connect(self.change_name)
        

        self.basdir = os.path.dirname(__file__)

        save_folder = os.path.join(self.basdir,'characters\\ben.dat')

        with open(save_folder, 'rb') as file:
            self.character = pickle.load(file)

        #self.name.setText(self.character.name)

        #self.center_layout.addWidget(self.name)
        #self.center_layout.addWidget(self.name_change)
        #self.center_layout.addWidget(self.name_change_button)

    def change_name(self):
        self.character.name = self.name_change.toPlainText()
        self.name.setText(self.character.name)
        self.name_change.clear()
    
    
class Character_screen(QMainWindow):
    def __init__(self, character: Character = Character(name= "Default", race= "Human")):
        super().__init__()
        self.central_widget = QFrame()
        self.setCentralWidget(self.central_widget)
        self.character = character

        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)

        ## Widgets of the Screen
        ##      Row 1
        self.character_name = QLabel(self.character.name)
        self.character_name.setObjectName('charactername')
        self.character_name.setAlignment(Qt.AlignCenter)
        ##      Row 2
        self.health = MainStatFrame(self.character.health.name, str(self.character.health.level),self)
        self.level = MainStatFrame(self.character.level.name, str(self.character.level.level),self)

        ##Layout of the screen
        self.central_layout.setSpacing(0)
        #row1
        self.central_layout.addWidget(self.character_name, 0, 0, 1, 6)
        #row2
        self.central_layout.addWidget(self.health._name, 1, 0,)
        self.central_layout.addWidget(self.health._level, 1, 1,1,2)
        self.central_layout.addWidget(self.level._name, 1, 3,)
        self.central_layout.addWidget(self.level._level, 1, 4,1,2)
        #row3
        #self.central_layout.addWidget(self.health_name, 1, 0,)
        #self.central_layout.addWidget(self.health_level, 1, 1,1,2)
        #self.central_layout.addWidget(self.level_name, 1, 3,)
        #self.central_layout.addWidget(self.level_level, 1, 4,1,2)



        self.stylesheet = """
                        QLabel#charactername { padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #0e2841;
                                    font: 18pt
                                    }
"""

        


        self.setStyleSheet(self.stylesheet)

class MainStatFrame(QLabel):
    def __init__(self, stat_name, stat_level,parent):
        super().__init__()
        self._parent = parent
        self._name = QLabel(stat_name)
        self._name.setObjectName("Stat_Name")
        self._name.setAlignment(Qt.AlignCenter)
        self._level = QLabel(stat_level)
        self._level.setObjectName("Stat_Level")
        self._level.setAlignment(Qt.AlignCenter)
        self._name.setStyleSheet( """
                QLabel#Stat_Name {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #315f8c;
                                    font: 18pt;}
                                    """
        )
        self._level.setStyleSheet("""
                QLabel#Stat_Level {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #0e2841;
                                    font: 18pt;}
                            
""")
        #self.setStyleSheet(self.stylesheet)

class abc(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        text = QLabel("Hello", widget)

        stylesheet = "QLabel {background-color: red}"
        self.setStyleSheet(stylesheet)
        

if __name__ == "__main__":
    app = QApplication()
    window = Character_screen()
    window.show()

    sys.exit(app.exec())