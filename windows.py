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
        self._dict_of_stats = {}
        self._dict_of_characters = {"Ben": Character("Ben", 'Human')}
        self.character_list_names_model = list_model(self._dict_of_characters)
        self.setwindowtitle = "Character Stats"
        central_widget = QWidget()

        #####left side of the screen
        self.left_widget = LeftWidget(self)

       ###### Right side of the screen 
        self.right_widget = RightWidget()

        ### Popup Windows ###
        self.another_window = None

        ### Buttons ###
        self.right_hide_button = QPushButton("Hide/Show")
        self.right_hide_button.setCheckable(True)
        self.right_hide_button.toggled.connect(self.right_widget.setHidden)

        self.exit_button = QPushButton("Quit")
        self.exit_button.clicked.connect(self.close)

        left_hide_button = QPushButton("Hide/Show")
        left_hide_button.setCheckable(True)
        left_hide_button.toggled.connect(self.left_widget.setHidden)

        ##### Main Layout ########
        
        central_layout = QGridLayout(central_widget)
        central_widget.setLayout(central_layout)
        central_layout.addWidget(self.left_widget,0,0)
        central_layout.addWidget(self.right_widget,0,2)
        central_layout.addWidget(self.exit_button,1,1)
        central_layout.addWidget(left_hide_button,1,0)
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

        current_working_dictionary = os.path.dirname(__file__)
        self.save_folder = os.path.join(current_working_dictionary, 'characters')

        self.character_path_names = {}
        self.load_character_path = ''
        for character in os.listdir(self.save_folder):
            if character.endswith(".dat"):
                filepath = os.path.join(self.save_folder, character)
                self.character_path_names[character.removesuffix(".dat")] = filepath
        
        self.load_character_path = self.character_path_names['Ben']
    
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

        self._model = self._parent._parent.character_list_names_model
        self.view_model = QListView()
        self.view_model.setModel(self._model)

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
        self.central_layout.addWidget(self.view_model,1,0, 1, 2)
        self.central_layout.addWidget(self.close_button, 2,1)
        self.central_layout.addWidget(self.select_button,2,0)

        self.central.setLayout(self.central_layout)
        self.setCentralWidget(self.central)
    
    def select_name(self):
        character_name = self.view_model.currentIndex().data()
    

        
        



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
    def __init__(self): 
        super().__init__()
        right_layout = QVBoxLayout(self)
        self.setLayout(right_layout)

        right_text = QLabel("right")
        right_layout.addWidget(right_text)
        right_text.setAlignment(Qt.AlignCenter )



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
