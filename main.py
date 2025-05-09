import os
import random
import pickle
#from characters.ben import ben
cur_path = os.path.dirname(__file__)
file_path = 'characters/ben.dat'
abs_file_path = os.path.join(cur_path, file_path)

def clearscreen():
    os.system('cls')
####################
clearscreen()
print("\n")

with open(abs_file_path, 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)



print("\n")

