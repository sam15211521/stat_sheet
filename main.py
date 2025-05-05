import os
import random
import typer
import tkinter as TK
import inspect
import inquirer
from character_objects import *

def clearscreen():
    os.system('cls')


current_races= []

####################
clearscreen()

print("\n\n\n")

for i in range(5):
    enemy = Character(name= f'bug{i}', race= 'bug')
    enemy.level.level= random.randint(1, 5) * 5
    ben.kills_character(enemy)


print (ben.get_kills())
print(ben.strength)
print(ben)
print("\nend")

print("\n\n\n")

