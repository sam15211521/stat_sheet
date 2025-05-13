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
        print(self.load_character_path)
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




        #self.select_button.pressed.connect()
        #self.aproval_dialog_box()
        


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
