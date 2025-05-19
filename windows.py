import sys
import os
import pickle

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from stats import Stat, MajorStat, Skill, SkillStat
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
        self._dict_of_loaded_characters = {}
        self.character_list_names_model = list_model(self.character_dict_with_path_names)
        self.setwindowtitle = "Character Stats"
        central_widget = QWidget()

        #####left side of the screen
        self.left_widget = LeftWidget(self)

        self.center_widget = CenterWidget(self)

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
        central_layout.addWidget(self.center_widget,0,1)
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

class CenterWidget(QWidget):
    def __init__(self, parent : MainWindow): 
        super().__init__()
        self._parent = parent
        self.setObjectName = "centerwidget"
        self.center_layout = QGridLayout(self)
        self.setLayout(self.center_layout)

        self.new_character_button = QPushButton("Create New Character")



        self.center_layout.addWidget(self.new_character_button)

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
        self.character_select_button.setDisabled(True)
        self.right_text.itemSelectionChanged.connect(self.character_selection)
        
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
    
    def character_selection(self):
        if self.character_select_button:
            self.character_select_button.setDisabled(False)

class Character_screen(QMainWindow):
    def __init__(self, character: Character = Character(name= "Default", race= "Human" )):
        super().__init__()
        self.central_widget = QWidget()
        self.central_widget_layout = QStackedLayout()
        self.character = character
        self.skill_window_layout = QGridLayout()

        self.stat_window = QFrame()
        self.skill_window = Skill_Screen(parent=self, character=self.character)

        self.central_widget_layout.addWidget(self.stat_window)
        self.central_widget_layout.addWidget(self.skill_window)

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
        self.health = MainStatFrame(self.character.health, 
                                    self.character,
                                    self
                                    )
        self.level = MainStatFrame(self.character.level, 
                                self.character,
                                self
                                )
        ##      Row 3
        self.mana = MainStatFrame("Mana", 
                                self.character,
                                f"{self.character.current_mana.level}/{self.character.max_mana.level} {self.character.max_mana.mana_unit}", 
                                self
                                )
        self.condensed_mana = MainStatFrame(self.character.condensed_mana,
                                            self.character,
                                            self
                                            )
        ##      Row 4
        self.resistance = MainStatFrame(self.character.resistance, 
                                        self.character,
                                        self
                                        )
        self.strength = MainStatFrame(self.character.strength, 
                                    self.character,
                                    self
                                    )
        ##      Row 5
        self.physical_resistance = MainStatFrame(self.character.physical_resistance, 
                                                self.character,
                                                self,
                                                parent_stat=self.resistance,
                                                mainstat=False
                                            )
        self.physical_strength = MainStatFrame(self.character.physical_strength, 
                                            self.character,
                                            self,
                                            parent_stat=self.strength,
                                            mainstat=False
                                            )
        ##      Row 6
        self.magic_resistance = MainStatFrame(self.character.magic_resistance, 
                                            self.character,
                                            self,
                                            parent_stat=self.resistance,
                                            mainstat=False
                                            )
        self.magic_strength = MainStatFrame(self.character.magical_strength, 
                                            self.character,
                                            self,
                                            parent_stat=self.strength,
                                            mainstat=False
                                            )
        ##      Row 7
        self.spiritual_resistance = MainStatFrame(self.character.spiritual_resistance, 
                                                self.character,
                                                self,
                                                parent_stat=self.resistance,
                                                mainstat=False)
        self.endurance = MainStatFrame(self.character.endurance, 
                                    self.character,
                                    self,)
        ##      Row 8
        self.regeneration = MainStatFrame(self.character.regeneration,
                                        self.character,
                                        self,)
        self.physical_endurance = MainStatFrame(self.character.physical_endurance,
                                        self.character,
                                        self,
                                        parent_stat=self.endurance,
                                        mainstat=False)
        ##      Row 9
        self.health_regeneration = MainStatFrame(self.character.health_regen,
                                        self.character,
                                        self,
                                        parent_stat=self.regeneration,
                                        mainstat=False)
        self.magic_endurance = MainStatFrame(self.character.magic_endurance,
                                        self.character,
                                        self,
                                        parent_stat=self.endurance,
                                        mainstat=False)
        ##      Row 10
        self.magic_regeneration = MainStatFrame(self.character.mana_regen,
                                        self.character,
                                        self,
                                        parent_stat=self.regeneration,
                                        mainstat=False)
        self.agility = MainStatFrame(self.character.agility,
                                        self.character,
                                        self,)
        ##      Row 11
        self.energy_potential = MainStatFrame(self.character.energy_potential,
                                        self.character,
                                        self,)
                        ## energy potential is on both row 11 and 12
        self.speed = MainStatFrame(self.character.speed,
                                        self.character,
                                        self,
                                        parent_stat=self.agility,
                                        mainstat=False)
        ##      Row 12
        self.coordination = MainStatFrame(self.character.coordination,
                                        self.character,
                                        self,
                                        parent_stat=self.agility,
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
        #self.skillScreen = Skill_Screen(parent=self, character=self.character)
        #self.skill_window_layout.addWidget(self.skill_screen_tab)
        


class Skill_Screen(QFrame):
    def __init__(self, parent: Character_screen, character:Character = None):
        super().__init__()
        #self.setMinimumSize(200, 200)
        self._parent = parent
        self.skill_window_layout = self._parent.skill_window_layout
        self.character = character
        self.setLayout(self.skill_window_layout)
        #print(self.character.skills_level.name)
        self.stylesheet = """
                        QLabel#skillname { padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #0e2841;
                                    font: 18pt;
                                    color: white
                                    }
                        QLabel#skilllevel { padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #0e2841;
                                    font: 18pt;
                                    color: white
                                    }
"""
        self.setStyleSheet(self.stylesheet)

        #self.skill_name_and_level_frame = QFrame()
        #self.skill_name_and_level_frame_layout = QGridLayout()
        #self.skill_name_and_level_frame_layout.setSpacing(0)

        #Row 1
        self.skill_name = QLabel(self.character.skills_level.name)
        self.skill_name.setObjectName("skillname")
        self.skill_name.setAlignment(Qt.AlignCenter)
        self.skill_name.setStyleSheet("QLabel { border: 2px solid black; padding 5px}")
        self.skill_name.setFixedHeight(30)

        self.skill_level = QLabel(str(self.character.skills_level.level))
        self.skill_level.setObjectName("skilllevel")
        self.skill_level.setAlignment(Qt.AlignCenter)
        self.skill_level.setStyleSheet("QLabel { border: 2px solid black; padding 5px}")
        self.skill_level.setFixedHeight(30)

        #Row2
        self.list_of_skills = Skills_list(self.character)

        #within the scrollarea
        self.skill_button_list = {}


        #layout logic
        self.skill_window_layout.setSpacing(0)
        #row 1

        self.skill_window_layout.addWidget(self.skill_name,0,0)
        self.skill_window_layout.addWidget(self.skill_level,0,1)

        #Row2
        self.skill_window_layout.addWidget(self.list_of_skills,1,0,1,2)

        # Within the skill list

class Skills_list(QFrame):
    def __init__(self, character: Character):
        super().__init__()
        self.setStyleSheet("QFrame {border: 2px solid blue}")
        self.character = character
        self.skills = self.character.skills_level.dict_of_skills

        self.skill_buttons = {}

        self.row = 0
        self._layout = QGridLayout()
        self.add_skills()
        self._layout.setAlignment(Qt.AlignTop)

        self.setLayout(self._layout)
        self._current_skill = None
        self._layout.setSpacing(0)
        self.sheet =  """
                QPushButton {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #1c548b;
                                    font: 18pt;
                                    color: black; 
                                    }
                                    """
        self.setStyleSheet(self.sheet)

    
    def add_skills(self):
        #Skill Name | Skill Level | Basics | Mastery | Discription | Tagged Stats | Mult | Total lvl Cost
        for skill in self.skills.values():
            skill : Skill
            skill_name = skill.name
            print(skill_name)
            skill_name_button = QPushButton(skill.name)
            skill_level_button = QPushButton(str(skill.level))
            skill_basics_button = QPushButton(str(skill.basics))
            skill_mastery_button = QPushButton(skill.mastery.name)
            skill_tagged_stats = QPushButton('press_for_more')
            skill_multipliable = QPushButton()


            skill_name_button.clicked.connect(lambda checked=True, name=skill.name: print(name))
            skill_level_button.clicked.connect(lambda checked=True, level=skill.level: print(level))
            skill_basics_button.clicked.connect(lambda checked=True, basics=skill.basics: print(basics))

            self._layout.addWidget(skill_name_button,self.row, 0 )
            self._layout.addWidget(skill_level_button, self.row, 1)
            self._layout.addWidget(skill_basics_button, self.row, 2)
            self._layout.addWidget(skill_mastery_button, self.row, 3)
            self._layout.addWidget(skill_tagged_stats, self.row, 4)

            self.row += 1
    
    
    def print_skill_name(self, n):
        print(n)
    
    def print_level_name(self, level):
        print(level)

class skill_button(QPushButton):
    def __init__(self,skill, kind):
        #Skill Name | Skill Level | Basics | Mastery | Discription | Tagged Stats | Mult | Total lvl Cost
        super().__init__()
        self._skill = skill
        if kind == "name":
            self.setText(self._skill.name)
        if kind == "level":
            self.setText(str(self._skill.level))
        if kind == "basics":
            self.setText(self._skill.name)
        self.sheet =  """
                QPushButton {padding: 0px; 
                                    margin: 0px; 
                                    border: 2px solid black; 
                                    background-color: #1c548b;
                                    font: 18pt;
                                    color: black; 
                                    }
                                    """
        self.setStyleSheet(self.sheet)


class MainStatFrame(QLabel):
    def __init__(self,
                 stat:Stat | str | MajorStat, 
                 character:Character, 
                 parent:Character_screen, 
                 parent_stat: Stat = False, 
                 mainstat = True,):
        super().__init__()
        self.mainstat = mainstat
        self.stat = stat
        self._character = character
        self._parent = parent
        self.parent_stat = parent_stat
        if isinstance(self.stat, Stat) or isinstance(self.stat, MajorStat):
            self.statname = self.stat.name
            self.statlevel = self.stat.level
            
        elif isinstance(self.stat, str):
            self.statname = self._character.max_mana.name
            self.stat = self._character.max_mana
            self.statlevel = parent

        #print(self.statname)

        self._name = QPushButton(self.statname)
        self._name.setObjectName("Stat_Name")
        self._name.clicked.connect(self.print_conf_name)
        
        self._level = QPushButton(str(self.statlevel))
        self._level.setObjectName("Stat_Level")
        self._level.clicked.connect(self.print_conf_level)
        if isinstance(self.stat, Stat):
            self._level_changer =StatIncreaseWindow(self, self._character, self.stat)
            self._level.clicked.connect(self._level_changer.show)
        


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
    def update_frames(self):
        self._name.setText(self.stat.name)
        self._level.setText(str(self.stat.level))
        if self.parent_stat:
            self.parent_stat.update_frames()

    def print_conf_name(self):
         print(f"button {self.statname} Name is pressed")
    def print_conf_level(self):
         print(f"button {self.statname} Level: {self.statlevel} is pressed")
    
class StatIncreaseWindow(QMainWindow):
    def __init__(self, 
                 parent : MainStatFrame, 
                 character : Character, 
                 stat : Stat,):
                 
        super().__init__()
        #boiler plate logic
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)


        self._parent = parent
        
        self.character = character
        self.stat = stat

        self.usable_mana = QSpinBox()
        self.usable_mana.setValue(self.character.condensed_mana.level)
        
        self.usable_mana.setValue(self.character.condensed_mana.level)
        self.usable_mana.lineEdit().setReadOnly(True)
        self.usable_mana.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.usable_mana.setSingleStep(1)
        self.usable_mana.setMaximum(100000)
        self.usable_mana.valueChanged.connect(self.set_con_mana)

        self.character_name =f"{self.character.name}: {self.stat.name} | {self.stat.level}"
        self.character_name = QLabel(f"{self.character.name}: {self.stat.name} | {self.stat.level}")
        self.text_mana_to_next_level = QLabel(f'Mana to next level: {self.stat.mana_to_next_level}')
        self.text_total_mana = QLabel(f'Total Mana: {self.stat._total_mana_used}')
        self.power_label = QLabel(f'Power: {self.stat.power}')

        self.increase_level_button = QPushButton("Increase Level")
        self.increase_level_button.clicked.connect(self.increase_level)
        self.mana_increase_button = QPushButton("Increase Con-Mana")
        self.mana_increase_button.clicked.connect(self.increase_conmana)
        self.mana_increase_button.pressed.connect(self.increase_conmana)

        self.print_stats_button = QPushButton("Print Stats")
        self.print_stats_button.clicked.connect(self.print_stats)

        self.central_layout.addWidget(self.character_name,0,0)
        self.central_layout.addWidget(self.usable_mana,1,0)
        self.central_layout.addWidget(self.text_mana_to_next_level,2,0)
        self.central_layout.addWidget(self.text_total_mana,3,0)
        self.central_layout.addWidget(self.power_label, 4, 0)
        self.central_layout.addWidget(self.increase_level_button,5,0)
        self.central_layout.addWidget(self.mana_increase_button,6,0)
        self.central_layout.addWidget(self.print_stats_button,7,0)
    
    def print_stats(self):
        print(self.character)

    def show(self):
        self.update_screens()
        return super().show()
    
    def update_screens(self):
        self.usable_mana.setValue(self.character.condensed_mana.level)
        self.character_name.setText(f"{self.character.name}: {self.stat.name} | {self.stat.level}")
        self.text_total_mana.setText(f'Total Mana: {self.stat._total_mana_used}')
        self.text_mana_to_next_level.setText(f'Mana to next level: {self.stat.mana_to_next_level}')
        self.power_label.setText(f'Power: {self.stat.power}')

    def set_con_mana(self):
        self.character.condensed_mana.level = int(self.usable_mana.value())
    
    def increase_conmana(self):
        self.character.add_condensed_mana(10)
        self.usable_mana.setValue(self.character.condensed_mana.level)
        self._parent._parent.condensed_mana.update_frames()

    
    def increase_level(self):
        if self.character.condensed_mana.level >= self.stat.mana_to_next_level:
            self.character.increase_stat_or_skill_level(self.stat)
            self.update_screens()
            self._parent.update_frames()
            self._parent._parent.condensed_mana.update_frames()
            self._parent._parent.level.update_frames()





    pass

def main():
    app = QApplication()
    app.setStyle('Fusion')

    window = MainWindow('ex')
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()


