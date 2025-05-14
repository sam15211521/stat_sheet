
import os
import pickle
from Character import Character
from stats import Stat
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #boiler plate logic
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)
        
        self.stat = Stat("Default")

        self.usable_mana = QDoubleSpinBox()
        self.usable_mana.setValue(0)
        self.usable_mana.setSingleStep(1)
        self.usable_mana.setDecimals(0)
        self.usable_mana.valueChanged.connect(self.print_value)


        self.mana_to_next_level = QLabel(f'Mana to next level: {self.stat.mana_to_next_level}')
        self.total_mana = QLabel(f'Total Mana: {self.stat._total_mana_used}')

        self.increase_level_button = QPushButton("Increase Level")

        self.central_layout.addWidget(self.usable_mana,0,0)
        self.central_layout.addWidget(self.mana_to_next_level,1,0)
        self.central_layout.addWidget(self.total_mana,2,0)
        self.central_layout.addWidget(self.increase_level_button,3,0)

    def print_value(self):
        print(self.usable_mana.value())
    
    def increase_level(self):
        pass

#a = Stat("default")
#current_level = a.mana_to_next_level
#next_level = a.mana_to_next_level * 1.008

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())