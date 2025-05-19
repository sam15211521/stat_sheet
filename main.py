import os
import random
from sys import exit as sys_exit
import pickle
#from characters.ben import ben, cat
from Character import Character
from stats import Skill
from windows import MainWindow 
from PySide6.QtWidgets import QApplication
cur_path = os.path.dirname(__file__)
file_path = 'characters/ben1.dat'
abs_file_path = os.path.join(cur_path, file_path)

def clearscreen():
    os.system('cls')
####################
ben = Character("Ben",body_mana_multiplier=2722) #hiden stat = 15.327

#print(ben.skills_level.dict_of_skills)
ben.add_skill(Skill('Mana Circulation'))


#print(ben.dict_of_skills)

#info = Character()
def save():
    with open(abs_file_path, 'wb') as File:
        #print(ben.skills_level.dict_of_skills)
        pickle.dump(ben, File)

def load():
    global info  
    with open(abs_file_path, "rb") as File:
        info = pickle.load(File)
        return info


def main():
    #clearscreen()
    #app = QApplication()
    #window = MainWindow('ex')
    #window.show()
    #sys_exit(app.exec())
    save()
    person = load()
    #print(person.skills_level.dict_of_skills)


if __name__ == "__main__":
    main()
