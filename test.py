import os
import pickle
from Character import Character
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #boiler plate logic
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)


        self.character_path_name ={"Ben": "here", "Cat": "There"}
        
        #The model
        self.model = list_model(self.character_path_name)
        self.modelView = QListView()
        self.modelView.setModel(self.model)

        #close button
        self.line_edit = QLineEdit()
        self.quitbutton = QPushButton("Quit")
        self.quitbutton.pressed.connect(self.close)

        #add button
        self.set_button = QPushButton("Set")
        self.set_button.pressed.connect(self.add)

        self.label = QLabel()




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


        #layout logic
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)

        ## Widgets of the Screen
        ##      Row 1
        self.character_name = QLabel(self.character.name)
        self.character_name.setObjectName('charactername')
        self.character_name.setAlignment(Qt.AlignCenter)
        ##      Row 2
        self.health = MainStatFrame(self.character.health.name, 
                                    str(self.character.health.level),
                                    self
                                    )
        self.level = MainStatFrame(self.character.level.name, 
                                   str(self.character.level.level),
                                   self
                                   )
        ##      Row 3
        self.mana = MainStatFrame("Mana", 
                                  f"{self.character.current_mana.level}/{self.character.max_mana.level}", 
                                  self
                                  )
        self.condensed_mana = MainStatFrame(self.character.condensed_mana.name,
                                            str(self.character.condensed_mana.level,), 
                                            self
                                            )
        ##      Row 4
        self.resistance = MainStatFrame(self.character.resistance.name, 
                                        str(self.character.resistance.level), 
                                        self
                                        )
        self.strength = MainStatFrame(self.character.strength.name, 
                                      str(self.character.strength.level), 
                                      self
                                      )
        ##      Row 5
        self.physical_resistance = MainStatFrame(self.character.physical_resistance.name, 
                                                 str(self.character.physical_resistance.level), 
                                                 self, 
                                                 mainstat=False
                                            )
        self.physical_strength = MainStatFrame(self.character.physical_strength.name, 
                                               str(self.character.physical_strength.level), 
                                               self,
                                               mainstat=False
                                            )
        ##      Row 6
        self.magic_resistance = MainStatFrame(self.character.magic_resistance.name, 
                                              str(self.character.magic_resistance.level), 
                                              self,
                                              mainstat=False
                                            )
        self.magic_strength = MainStatFrame(self.character.magical_strength.name, 
                                            str(self.character.magical_strength.level), 
                                            self,
                                            mainstat=False
                                            )
        ##      Row 7
        self.spiritual_resistance = MainStatFrame(self.character.spiritual_resistance.name, 
                                                  str(self.character.spiritual_resistance.level), 
                                                  self)
        self.endurance = MainStatFrame(self.character.endurance.name, 
                                       str(self.character.endurance.level), 
                                       self)

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
        self.central_layout.addWidget(self.mana._name, 2, 0,1,1)
        self.central_layout.addWidget(self.mana._level, 2, 1,1,2)
        self.central_layout.addWidget(self.condensed_mana._name, 2, 3,1,1)
        self.central_layout.addWidget(self.condensed_mana._level, 2, 4,1,2)
        #Row 4
        self.central_layout.addWidget(self.resistance._name, 3, 0,1,1)
        self.central_layout.addWidget(self.resistance._level, 3, 1,1,2)
        self.central_layout.addWidget(self.strength._name, 3, 3,1,1)
        self.central_layout.addWidget(self.strength._level, 3, 4,1,2)
        #Row 5
        self.central_layout.addWidget(self.physical_resistance._name, 4, 0,1,1)
        self.central_layout.addWidget(self.physical_resistance._level, 4, 1,1,2)
        self.central_layout.addWidget(self.physical_strength._name, 4, 3,1,1)
        self.central_layout.addWidget(self.physical_strength._level, 4, 4,1,2)
        # Row 6
        self.central_layout.addWidget(self.magic_resistance._name, 5, 0,1,1)
        self.central_layout.addWidget(self.magic_resistance._level, 5, 1,1,2)
        self.central_layout.addWidget(self.magic_strength._name, 5, 3,1,1)
        self.central_layout.addWidget(self.magic_strength._level, 5, 4,1,2)
        # Row 7
        self.central_layout.addWidget(self.spiritual_resistance._name, 6, 0,1,1)
        self.central_layout.addWidget(self.spiritual_resistance._level, 6, 1,1,2)
        self.central_layout.addWidget(self.endurance._name, 6, 3,1,1)
        self.central_layout.addWidget(self.endurance._level, 6, 4,1,2)
        

        
        



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
    def __init__(self, stat_name, stat_level,parent, mainstat = True):
        super().__init__()
        self.mainstat = mainstat
        self._parent = parent
        self._name = QLabel(stat_name)
        self._name.setObjectName("Stat_Name")
        self._name.setAlignment(Qt.AlignCenter)
        self._level = QLabel(stat_level)
        self._level.setObjectName("Stat_Level")
        self._level.setAlignment(Qt.AlignCenter)
        if mainstat:
                self._name.setStyleSheet( """
                QLabel#Stat_Name {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #1c548b;
                                    font: 18pt;}
                                    """
                )
        else:
                self._name.setStyleSheet( """
                QLabel#Stat_Name {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #4f78a1;
                                    font: 18pt;}
                                    """
                )
                self._name.setAlignment(Qt.AlignRight)
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