
import os
import pickle
from Character import Character
from stats import Stat
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *



class stat_increase_window(QMainWindow):
    def __init__(self, character : Character):
        super().__init__()
        #boiler plate logic
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)
        
        self.character = character

        self.usable_mana = QDoubleSpinBox()
        
        self.usable_mana.setValue(self.character.condensed_mana.level)
        #self.usable_mana.lineEdit().setReadOnly(True)
        self.usable_mana.setSingleStep(1)
        self.usable_mana.setDecimals(0)
        self.usable_mana.setMaximum(1000)
        self.usable_mana.valueChanged.connect(self.set_con_mana)

        self.character_name =f"{self.character.name}: {self.character.magic_endurance.name} | {self.character.magic_endurance.level}"
        self.character_name = QLabel(f"{self.character.name}: {self.character.magic_endurance.name} | {self.character.magic_endurance.level}")
        self.text_mana_to_next_level = QLabel(f'Mana to next level: {self.character.magic_endurance.mana_to_next_level}')
        self.text_total_mana = QLabel(f'Total Mana: {self.character.magic_endurance._total_mana_used}')
        self.power_label = QLabel(f'Power: {self.character.magic_endurance.power}')

        self.increase_level_button = QPushButton("Increase Level")
        self.increase_level_button.clicked.connect(self.increase_level)

        self.central_layout.addWidget(self.character_name,0,0)
        self.central_layout.addWidget(self.usable_mana,1,0)
        self.central_layout.addWidget(self.text_mana_to_next_level,2,0)
        self.central_layout.addWidget(self.text_total_mana,3,0)
        self.central_layout.addWidget(self.power_label, 4, 0)
        self.central_layout.addWidget(self.increase_level_button,5,0)

    def set_con_mana(self):
        self.character.condensed_mana.level = int(self.usable_mana.value())

    
    def increase_level(self):
        #current_requirment = self.character.mana_to_next_level
        if self.character.condensed_mana.level >= self.character.magic_endurance.mana_to_next_level:
            self.character.use_con_mana_to_increase_stat_level(self.character.magic_endurance)
            self.usable_mana.setValue(self.character.condensed_mana.level)
            self.character_name.setText(f"{self.character.name}: {self.character.magic_endurance.name} | {self.character.magic_endurance.level}")
            self.text_total_mana.setText(f'Total Mana: {self.character.magic_endurance._total_mana_used}')
            self.text_mana_to_next_level.setText(f'Mana to next level: {self.character.magic_endurance.mana_to_next_level}')
            self.power_label.setText(f'Power: {self.character.magic_endurance.power}')


#a = Stat("default")
#current_level = a.mana_to_next_level
#next_level = a.mana_to_next_level * 1.008

if __name__ == "__main__":
    app = QApplication()
    window = stat_increase_window(Character("Ben"))
    window.show()

    sys.exit(app.exec())