import os
import random
from sys import exit as sys_exit
import pickle
from characters.ben import ben
from Character import Character
from windows import MainWindow 
from PySide6.QtWidgets import QApplication
from Character import Character
#from characters.ben import ben
cur_path = os.path.dirname(__file__)
file_path = 'characters/cat.dat'
abs_file_path = os.path.join(cur_path, file_path)

def clearscreen():
    os.system('cls')
####################

info = Character
def save():
    with open(abs_file_path, 'wb') as File:
        pickle.dump(ben, File)

def load():
    global info
    with open(abs_file_path, "rb") as File:
        info = pickle.load(File)
        return info


def main():
    app = QApplication()
    window = MainWindow('ex')
    window.show()
    sys_exit(app.exec())



if __name__ == "__main__":
    save()
clearscreen()
print("\n")
ben = Character("Ben",body_mana_multiplier=2722) #hiden stat = 15.327
with open(abs_file_path,'wb') as file:
    pickle.dump(ben, file)

with open(abs_file_path, 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)



print("\n")

