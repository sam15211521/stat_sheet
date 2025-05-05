from statistics import mean
import os
from math import floor
from mastery import Mastery, basic, beginner, intermediate, expert, master

# all classes need a: name, mana_to_next_level, total_mana_invested, power, discription

class Attribute():
    _attribute_dictionary = {}
    def __init__(self, name='', discription= ''):
        self._name = name
        self._level = 0
        
        self._mana_to_next_level = 1
        self._total_mana_used = 0
        
        self._discription = discription

        self._power = 1
        

        self._attribute_dictionary[self._name] = self
    
    def __str__(self):
        line1 = f"{self.name} | Level: {self.level} "
        line2 = f"mana to next level: {self.mana}"
        line3 = self.discription
        return "\n".join([line1, line2, line3])
    
    #getter and setter functions of _name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    #getter and setter function of _level
    @property
    def level(self):
        return self._level
   
    @level.setter
    def level(self, level):
        self._level = level
        self.power = 1 *(1.01 ** self.level)
   
    #getter and setter functions of _mana_to_next_level
    @property
    def mana_to_next_level(self):
        return self._mana_to_next_level
    
    @mana_to_next_level.setter
    def mana_to_next_level(self, mana):
        self.mana_to_next_level = mana
    
    #getter and setter functions of _total_mana_used
    @property
    def mana(self):
        return self._total_mana_used
   
    @mana.setter
    def mana(self, mana):
        self._total_mana_used = mana
    
    #getter and setter funcitons of _power
    
    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, power):
        self._power = 1.01 ** self.level
    
    #getter and setter of the discription
    @property
    def discription(self):
        return self._discription
    
    @discription.setter
    def discription(self, discription):
        self._discription = discription

    #gets the number of diffrent attributes
    @property
    def number_of_attributes(self):
        return self._attribute_dictionary
    
    


class MajorStat(Attribute):
    def __init__(self, name='', discription=''):
        super().__init__(name, discription)


class Stat(Attribute):
    def __init__(self, 
                 name='',
                 discription='', 
                 isparent = False,
                 childstats = {}

                 ):
        super().__init__(name, discription)
        
        self._acronym = self.name[:3]

        self._isparent = isparent
        self._child_stats = {}
        self._parent_stat = None
    
    @property
    def isparent(self):
        return self._isparent
    
    @isparent.setter
    def isparent(self, stat):
        if isinstance(stat, bool):
            self._isparent = stat
        else:
              print(f'ERROR: {self.name}.isparent Must be type <bool>')
    
    @property
    def child_stats(self):
        return self._child_stats
    
    @property
    def parent_stat(self):
        return self._parent_stat
    
    @parent_stat.setter
    def parent_stat(self, parent):
        self._parent_stat = parent

    
    @property
    def level(self):
        if self.isparent:
            #self._level = floor(self.average_values())
            return self._level
        else:
            return self._level
    
    @ level.setter
    def level(self, level=None):
        if not self.isparent:
            self._level = level
            if isinstance(self.parent_stat, Stat):
                self.parent_stat.level = None #just need it to equal to something
        else:
            self._level = floor(self.average_levels())
            if isinstance(self.parent_stat, Stat):
                self.parent_stat.level = None

    
    def add_child_stat(self, stat):
        if self.isparent and isinstance(stat, Stat):
            stat.parent_stat = self
            self._child_stats[stat.name] = stat
        elif not self.isparent:
            print(f"\n<{self.name}> is a Child Stat\n")
            return
        else:
            print(f'\nThe added stat <{stat.name}> is not a Child Stat\n')
    
    
    def print_child_stats(self):
        print(f'the Child Stats of {self.name} are:')
        if self.child_stats == {}:
            print(f"\n{self.name} has no Child Stats\n")
        else:
            for name, stat in self.child_stats.items():
                print(f'Name: {name}, Level: {stat.level}')
    
    # used to calculate the level of a parent stat based on 
    # the average of the levels of the childstats
    def average_levels(self):
        return mean(stat.level for name, stat in self.child_stats.items())
    
    def level_overide(self, level_increase):
        pass
        

class Skill(Attribute):
    def __init__(self, name='', discription=''):
        super().__init__(name, discription)
        self._basics = False
        self._mastery = basic
        self._tagged_stats = {}
        self._stat_multiplier = self.mastery.multiplier
    
    @property
    def level(self):
        return self._level
   
    @level.setter
    def level(self, level):
        self._level = level
        self.power = None
        self.master = None
    
    @property
    def basics(self):
        return self._basics
    @basics.setter
    def basics(self, basics):
        if isinstance(basics, bool):
            self._basics = basics
        else:
            print(f'Error: {self.name}.basics.setter :\nthe value <{basics}> is not type bool')
    
    @property
    def mastery(self):
        return self._mastery
    
    @mastery.setter
    def mastery(self):
        if not self.basics:
            if self.level == 0:
                self._mastery = basic
            elif self.level > 0 and self.level <= 100:
                self._mastery = beginner
        else:
            if self.level == 0:
                self._mastery = beginner
            elif self.level > 0 and self.level <= 109:
                self._mastery = intermediate
            elif self.level > 109 and self.level <= 1000:
                self._mastery = expert
            elif self.level > 1001 and self.level <= 10000:
                self._master = master

os.system('cls')

    



skill = Skill(name ='cutting')

os.system('cls')
a = Attribute(name = 'a')
b = Stat(name = 'b', isparent=True)
b1 = Stat(name= 'b1')
b2 = Stat(name= 'b2', isparent=True)

b2_1 = Stat(name= 'b2_1')
b2_2 = Stat(name = 'b2_2')
b2_3 = Stat(name= 'b2_3')

b.add_child_stat(b1)
b.add_child_stat(b2)

b2.add_child_stat(b2_1)
b2.add_child_stat(b2_2)
b2.add_child_stat(b2_3)

b.level = 2
b1.level = 9
b2.level = 2
b2_1.level = 8
b2_2.level = 8
b2_3.level = 8

print(f'{b.name}: {b.level}')
print(f'{b1.name}: {b1.level}')
print(f'{b2.name}: {b2.level}')
print(f'{b2_1.name}: {b2_1.level}')
print(f'{b2_2.name}: {b2_2.level}')
print(f'{b2_3.name}: {b2_3.level}')

print('#\n\n')

print(skill.mastery.name, skill.level, skill.basics)
skill.level = 4
print(skill.mastery.name, skill.level, skill.basics)
print('\n\n')

