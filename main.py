import os
import random
import pickle
from Character import Character
#from characters.ben import ben
cur_path = os.path.dirname(__file__)
file_path = 'characters/ben.dat'
abs_file_path = os.path.join(cur_path, file_path)

def clearscreen():
    os.system('cls')
####################
clearscreen()
print("\n")
ben = Character("Ben",body_mana_multiplier=2722) #hiden stat = 15.327
with open(abs_file_path,'wb') as file:
    pickle.dump(ben, file)

with open(abs_file_path, 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)



print("\n")

