import sys
import os
import pickle

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from stats import Stat
from Character import Character




class MainWindow(QMainWindow):
    def __init__(self, character_sheet: dict):
        super().__init__()
        self.setMaximumSize(500, 400)

        current_working_dictionary = os.path.dirname(__file__)
        self.save_folder = os.path.join(current_working_dictionary, 'characters')
        self.character_dict_with_path_names = {}

        self.load_character_path = ''
        for character in os.listdir(self.save_folder):
            if character.endswith(".dat"):
                filepath = os.path.join(self.save_folder, character)
                self.character_dict_with_path_names[character.removesuffix(".dat")] = filepath


        self._dict_of_stats = {}
        self._dict_of_loaded_characters = {"Maple":Character("Maple")}
        self.character_list_names_model = list_model(self.character_dict_with_path_names)
        self.setwindowtitle = "Character Stats"
        central_widget = QWidget()

        #####left side of the screen
        self.left_widget = LeftWidget(self)

       ###### Right side of the screen 
        self.right_widget = RightWidget(self)

        ### Popup Windows ###
        self.another_window = None

        ### Buttons ###
        self.right_hide_button = QPushButton("Hide/Show")
        self.right_hide_button.setCheckable(True)
        self.right_hide_button.toggled.connect(self.right_widget.setHidden)

        self.exit_button = QPushButton("Quit")
        self.exit_button.clicked.connect(self.close)

        self.left_hide_button = QPushButton("Hide/Show")
        self.left_hide_button.setCheckable(True)
        self.left_hide_button.toggled.connect(self.left_widget.setHidden)

        ##### Main Layout ########
        
        central_layout = QGridLayout(central_widget)
        central_widget.setLayout(central_layout)
        central_layout.addWidget(self.left_widget,0,0)
        central_layout.addWidget(self.right_widget,0,2)
        central_layout.addWidget(self.exit_button,1,1)
        central_layout.addWidget(self.left_hide_button,1,0)
        central_layout.addWidget(self.right_hide_button,1,2)
        self.setCentralWidget(central_widget)

        ######## The Menu #######
        menu = self.menuBar()
        #File menu#
        file_menu = menu.addMenu("File")
        self.quit_action = QAction("Quit", self)
        self.quit_action.triggered.connect(self.closeEvent)
        ### Menu addition ###
        file_menu.addAction(self.quit_action)

        
    def add_to_character_paths(self): #when a character is added gives a
        pass# link to where the save data for it is
    
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()

    def add_characters(self):
        pass

    def save(self):
        pass
    def load(self):
        with open(self.load_character_path, 'rb') as file:
            return pickle.load(file)


class LeftWidget(QWidget):
    def __init__(self, parent: MainWindow):
        super().__init__()
        left_layout = QVBoxLayout(self)
        self._parent = parent
        self.setLayout(left_layout)

        self.character_name = QLabel

        self.open_button = QPushButton("Select Character")
        self.open_button.setCheckable(True)
        self.open_button.toggled.connect(self.select_character)
        self.open_button.clicked.connect(self.select_character)
        #print(self.__parent)


        # layout
        left_layout.addWidget(self.open_button)
    
    def select_character(self, clicked):
        if clicked:
            self.win = CharacterSelectScreen(self)
            self.win.show()
        else:
            self.win.close()

class CharacterSelectScreen(QMainWindow):
    def __init__(self, parent: LeftWidget):
        super().__init__()
        self.central = QWidget()
        self._parent = parent

        self.selected_character_label = QLabel()
        self.selected_character_label.setObjectName("CharacterLabel")
        self.selected_character_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.style_sheet = """QLabel#CharacterLabel {font-size: 20px; 
                                                    border: 2px solid;
                                                    }"""
        self.setStyleSheet(self.style_sheet)
        self._model = self._parent._parent.character_list_names_model
        self.view_model = QListView()
        self.view_model.setModel(self._model)
        self.view_model.clicked.connect(self.show_name_in_label)

        self.instructions = QLabel("Please select the character of wich you want to view stats")
        self.instructions.setWordWrap(True)

        #buttons
        self.close_button = QPushButton("Close")
        self.close_button.pressed.connect(self.close)
        self.close_button.setGeometry(1,1,5,19)

        self.select_button = QPushButton("Select")
        self.select_button.pressed.connect(self.select_name)
        
        #layout
        self.central_layout = QGridLayout()
        self.central_layout.addWidget(self.instructions,0,0)
        self.central_layout.addWidget(self.view_model,2,0, 1, 2)
        self.central_layout.addWidget(self.close_button, 3,1)
        self.central_layout.addWidget(self.select_button,3,0)
        self.central_layout.addWidget(self.selected_character_label, 1,0)

        self.central.setLayout(self.central_layout)
        self.setCentralWidget(self.central)
    def print_result(self):
        print(self.load_character_dialog.result())
        
    def show_name_in_label(self):
        self.selected_character_label.setText(self.view_model.currentIndex().data())
    
    def select_name(self):
        character_name = self.view_model.currentIndex().data()
        character_datapath = self._parent._parent.character_dict_with_path_names[character_name]
        self._parent._parent.load_character_path = character_datapath
        file = self._parent._parent.load()
        self._parent._parent._dict_of_loaded_characters[file.name] = file
        #print(self._parent._parent._dict_of_loaded_characters)
        self._parent._parent.right_widget.show_selected_characters()
        self.close()
        
    def aproval_dialog_box(self):
        self.load_character_dialog = QDialog()

        self.dialog_buttons = (QDialogButtonBox.Ok | QDialogButtonBox.No | QDialogButtonBox.Cancel)
        self.dialog_button_box = QDialogButtonBox(self.dialog_buttons)

        self.dialog_button_box.accepted.connect(self.load_character_dialog.accept)
        self.dialog_button_box.rejected.connect(self.load_character_dialog.reject)

        self.load_character_dialog_layout = QVBoxLayout()
        self.load_character_dialog_layout.addWidget(self.dialog_button_box)
        self.load_character_dialog.setLayout(self.load_character_dialog_layout)
        if self.load_character_dialog.isVisible():
            print(self.load_character_dialog.isVisible())
    
class list_model(QAbstractListModel):
    def __init__(self, lst={}):
        super().__init__()
        self._list = list(lst.keys()) or {}
    
    def data(self, index, role = ...):
        if role == Qt.DisplayRole:
            text = self._list[index.row()]
            return text
    
    def rowCount(self, index):
        return len(self._list)


class RightWidget(QWidget):
    def __init__(self, parent : MainWindow): 
        super().__init__()
        self._parent = parent
        self.setObjectName = "rightwidget"
        self.right_layout = QGridLayout(self)
        self.setLayout(self.right_layout)

        self.selected_characters = list(self._parent._dict_of_loaded_characters.keys())

        self.right_text = QListWidget()
        self.setMaximumSize(150,300)
        self.show_selected_characters()

        self.character_select_button = QPushButton('Select Character')
        self.character_select_button.clicked.connect(self.select_character)
        
        self.right_layout.addWidget(self.right_text,0,0)
        self.right_layout.addWidget(self.character_select_button,1,0)
        self.dict_of_stat_windows ={}
    
    @Slot()
    def show_selected_characters(self):
        self.selected_characters = list(self._parent._dict_of_loaded_characters.keys())
        self.right_text.clear()
        self.right_text.addItems(self.selected_characters)
    
    def select_character(self):
        character_name = self.right_text.currentIndex().data()
        current_character = self._parent._dict_of_loaded_characters[character_name]
        self.dict_of_stat_windows[character_name] = Character_screen(current_character)
        self.dict_of_stat_windows[character_name].show()

class Character_screen(QMainWindow):
    def __init__(self, character: Character = Character(name= "Default", race= "Human" )):
        super().__init__()
        self.central_widget = QWidget()
        self.central_widget_layout = QStackedLayout()

        self.stat_window = QFrame()
        self.skill_window = QFrame()

        self.central_widget_layout.addWidget(self.stat_window)
        self.central_widget_layout.addWidget(self.skill_window)
        self.character = character

        self.stat_screen_button = QAction("Stats", self)
        self.stat_screen_button.setCheckable(True)
        self.stat_screen_button.triggered.connect(self.stat_screen)

        self.skill_screen_button = QAction("Skills", self)
        self.skill_screen_button.setCheckable(True)
        self.skill_screen_button.triggered.connect(self.skill_screen)
        
        self.tool_bar = QToolBar()
        self.addToolBar(self.tool_bar)
        self.tool_bar.addAction(self.stat_screen_button)
        self.tool_bar.addAction(self.skill_screen_button)

        #layout logic
        self.stat_window_layout = QGridLayout()
        self.stat_window.setLayout(self.stat_window_layout)

        self.skill_window_layout = QGridLayout()
        self.skill_window.setLayout(self.skill_window_layout)

        self.central_widget.setLayout(self.central_widget_layout)
        self.setCentralWidget(self.central_widget)
        self.stat_screen()




    def stat_screen(self):
        self.skill_screen_button.setChecked(False)
        self.central_widget_layout.setCurrentIndex(0)
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
                                f"{self.character.current_mana.level}/{self.character.max_mana.level} {self.character.max_mana.mana_unit}", 
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
                                                self,
                                                mainstat=False)
        self.endurance = MainStatFrame(self.character.endurance.name, 
                                    str(self.character.endurance.level), 
                                    self,)
        ##      Row 8
        self.regeneration = MainStatFrame(self.character.regeneration.name,
                                        str(self.character.regeneration.level),
                                        self,)
        self.physical_endurance = MainStatFrame(self.character.physical_endurance.name,
                                        str(self.character.physical_endurance.level),
                                        self,
                                        mainstat=False)
        ##      Row 9
        self.health_regeneration = MainStatFrame(self.character.health_regen.name,
                                        str(self.character.health_regen.level),
                                        self,
                                        mainstat=False)
        self.magic_endurance = MainStatFrame(self.character.magic_endurance.name,
                                        str(self.character.magic_endurance.level),
                                        self,
                                        mainstat=False)
        ##      Row 10
        self.magic_regeneration = MainStatFrame(self.character.mana_regen.name,
                                        str(self.character.mana_regen.level),
                                        self,
                                        mainstat=False)
        self.agility = MainStatFrame(self.character.agility.name,
                                        str(self.character.agility.level),
                                        self,)
        ##      Row 11
        self.energy_potential = MainStatFrame(self.character.energy_potential.name,
                                        str(self.character.energy_potential.level),
                                        self,)
                        ## energy potential is on both row 11 and 12
        self.speed = MainStatFrame(self.character.speed.name,
                                        str(self.character.speed.level),
                                        self,
                                        mainstat=False)
        ##      Row 12
        self.coordination = MainStatFrame(self.character.coordination.name,
                                        str(self.character.coordination.level),
                                        self,
                                        mainstat=False)

        ##Layout of the screen
        self.stat_window_layout.setSpacing(0)
        #Row 1
        self.stat_window_layout.addWidget(self.character_name, 0, 0, 1, 6)
        #Row 2
        self.stat_window_layout.addWidget(self.health._name, 1, 0,)
        self.stat_window_layout.addWidget(self.health._level, 1, 1,1,2)
        self.stat_window_layout.addWidget(self.level._name, 1, 3,)
        self.stat_window_layout.addWidget(self.level._level, 1, 4,1,2)
        #Row 3
        self.stat_window_layout.addWidget(self.mana._name, 2, 0,1,1)
        self.stat_window_layout.addWidget(self.mana._level, 2, 1,1,2)
        self.stat_window_layout.addWidget(self.condensed_mana._name, 2, 3,1,1)
        self.stat_window_layout.addWidget(self.condensed_mana._level, 2, 4,1,2)
        #Row 4
        self.stat_window_layout.addWidget(self.resistance._name, 3, 0,1,1)
        self.stat_window_layout.addWidget(self.resistance._level, 3, 1,1,2)
        self.stat_window_layout.addWidget(self.strength._name, 3, 3,1,1)
        self.stat_window_layout.addWidget(self.strength._level, 3, 4,1,2)
        #Row 5
        self.stat_window_layout.addWidget(self.physical_resistance._name, 4, 0,1,1)
        self.stat_window_layout.addWidget(self.physical_resistance._level, 4, 1,1,2)
        self.stat_window_layout.addWidget(self.physical_strength._name, 4, 3,1,1)
        self.stat_window_layout.addWidget(self.physical_strength._level, 4, 4,1,2)
        # Row 6
        self.stat_window_layout.addWidget(self.magic_resistance._name, 5, 0,1,1)
        self.stat_window_layout.addWidget(self.magic_resistance._level, 5, 1,1,2)
        self.stat_window_layout.addWidget(self.magic_strength._name, 5, 3,1,1)
        self.stat_window_layout.addWidget(self.magic_strength._level, 5, 4,1,2)
        # Row 7
        self.stat_window_layout.addWidget(self.spiritual_resistance._name, 6, 0,1,1)
        self.stat_window_layout.addWidget(self.spiritual_resistance._level, 6, 1,1,2)
        self.stat_window_layout.addWidget(self.endurance._name, 6, 3,1,1)
        self.stat_window_layout.addWidget(self.endurance._level, 6, 4,1,2)
        # Row 8
        self.stat_window_layout.addWidget(self.regeneration._name, 7, 0,1,1)
        self.stat_window_layout.addWidget(self.regeneration._level, 7, 1,1,2)
        self.stat_window_layout.addWidget(self.physical_endurance._name, 7, 3,1,1)
        self.stat_window_layout.addWidget(self.physical_endurance._level, 7, 4,1,2)
        # Row 9
        self.stat_window_layout.addWidget(self.health_regeneration._name, 8, 0,1,1)
        self.stat_window_layout.addWidget(self.health_regeneration._level, 8, 1,1,2)
        self.stat_window_layout.addWidget(self.magic_endurance._name, 8, 3,1,1)
        self.stat_window_layout.addWidget(self.magic_endurance._level, 8, 4,1,2)
        # Row 10
        self.stat_window_layout.addWidget(self.magic_regeneration._name, 9, 0,1,1)
        self.stat_window_layout.addWidget(self.magic_regeneration._level, 9, 1,1,2)
        self.stat_window_layout.addWidget(self.agility._name, 9, 3,1,1)
        self.stat_window_layout.addWidget(self.agility._level, 9, 4,1,2)
        # Row 11
        self.stat_window_layout.addWidget(self.energy_potential._name, 10, 0,2,1)
        self.stat_window_layout.addWidget(self.energy_potential._level, 10, 1,2,2)
        self.stat_window_layout.addWidget(self.speed._name, 10, 3,1,1)
        self.stat_window_layout.addWidget(self.speed._level, 10, 4,1,2)
        # Row 12
        self.stat_window_layout.addWidget(self.coordination._name, 11, 3,1,1)
        self.stat_window_layout.addWidget(self.coordination._level, 11, 4,1,2)

        self.stylesheet = """
                        QLabel#charactername { padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #0e2841;
                                    font: 18pt;
                                    color: white
                                    }
"""
        self.setStyleSheet(self.stylesheet)
    def skill_screen(self):
        self.stat_screen_button.setChecked(False)
        self.central_widget_layout.setCurrentIndex(1)
        self.testing = QLabel("Hello")
        self.skill_window_layout.addWidget(self.testing,0,0)
             

class MainStatFrame(QLabel):
    def __init__(self, stat_name, stat_level,parent, mainstat = True):
        super().__init__()
        self.mainstat = mainstat
        self.statname = stat_name
        self.statlevel = stat_level
        self._parent = parent

        self._name = QPushButton(stat_name)
        self._name.setObjectName("Stat_Name")
        self._name.clicked.connect(self.print_conf_name)
        
        self._level = QPushButton(stat_level)
        self._level.setObjectName("Stat_Level")
        self._level.clicked.connect(self.print_conf_level)
        


        if mainstat:
                self._name.setStyleSheet( """
                QPushButton#Stat_Name {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #1c548b;
                                    font: 18pt;
                                    color: black; 
                                    }
                                    """
                )
        else:
                self._name.setStyleSheet( """
                QPushButton#Stat_Name {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #4f78a1;
                                    font: 18pt ;
                                    color: black}
                                    """
                )
        if self.statname == "Energy Potential":
            self._name.setFixedHeight(72)
            self._level.setFixedHeight(72)
                #self._name.setAlignment(Qt.AlignRight)
        self._level.setStyleSheet("""
                QPushButton#Stat_Level {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #0e2841;
                                    font: 18pt;}
                            
""")

    def print_conf_name(self):
         print(f"button {self.statname} Name is pressed")
    def print_conf_level(self):
         print(f"button {self.statname} Level: {self.statlevel} is pressed")


def main():
    app = QApplication()
    app.setStyle('Fusion')

    window = MainWindow('ex')
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())



class Character_Stat_Screen(QFrame):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    main()
