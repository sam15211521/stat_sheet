from statistics import mean
from math import floor, ceil
from mastery import basic, beginner, intermediate, expert, master

# all classes need a: name, mana_to_next_level, total_mana_invested, power, discription

class Attribute():
    _attribute_dictionary = {}
    def __init__(self, name='', 
                 discription= '', 
                 mana_multiplier =1,
                 mana_capacity_flag = False,
                 level =0):
        self._name = name
        self._level = level
        
        self._mana_to_next_level = 1
        self._actual_mana_to_next_level =1
        self._total_mana_used = 0
        
        self._discription = discription

        self._power = 1
        
        self._mana_capasity_multiplier = mana_multiplier

        self._attribute_dictionary[self._name] = self
        self._affects_mana_capacity = mana_capacity_flag
        
    
    def __str__(self):
        line1 = f"{self.name} | Level: {self.level:,} "
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
        self.calculate_capacity_multiplier()
   
    #getter and setter functions of _mana_to_next_level
    @property
    def mana_to_next_level(self):
        return self._mana_to_next_level
    
    @mana_to_next_level.setter
    def mana_to_next_level(self, mana):
        self._mana_to_next_level = mana
    
    @property
    def actual_mana_to_next_level(self):
        return self._actual_mana_to_next_level
    @actual_mana_to_next_level.setter
    def actual_mana_to_next_level(self, value):
        self._mana_to_next_level = ceil(value)
        self._actual_mana_to_next_level = value 

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
        self._power = power
    
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
    
    @property
    def mana_capasity_multiplier(self):
        return self._mana_capasity_multiplier

    @mana_capasity_multiplier.setter
    def mana_capasity_multiplier(self, value):
        self._mana_capasity_multiplier = value
    
    @property
    def affects_mana_capacity(self):
        return self._affects_mana_capacity
    @affects_mana_capacity.setter
    def affects_mana_capacity(self, flag):
        if isinstance(flag, bool):
            self._affects_mana_capacity = flag
    
    def calculate_capacity_multiplier(self):
        #need an initial value based on the type of skill
        # will be multiplied by level
        if self.affects_mana_capacity:
            self.mana_capasity_multiplier= round(self.mana_capasity_multiplier * 1.01 ** self.level,2)

class MajorStat(Attribute):
    def __init__(self, name='', discription='', mana_multiplier= 1, mana_capacity_flag=False):
        super().__init__(name, discription, mana_multiplier, mana_capacity_flag)
        self._mana_unit = None
    @property
    def mana_unit(self):
        return self._mana_unit
    @mana_unit.setter
    def mana_unit(self, unit):
        self._mana_unit = unit
    def __str__(self):
        if self.name == "Max Mana" or self.name == "Mana":
            return f"{self.name}: {self.level:,} {self.mana_unit}"
        else:
            return super().__str__()

class HiddenManaStat(Attribute):
    def __init__(self, name='', discription='', mana_multiplier=1, mana_capacity_flag=False):
        super().__init__(name, discription, mana_multiplier, mana_capacity_flag)
    
    def calculate_capacity_multiplier(self):
        return None
    
    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, level):
        self._level = level
        
class CondensedMana(MajorStat):
    def __init__(self, name='', discription='', mana_multiplier=1,mana_capacity_flag=False):
        super().__init__(name, discription, mana_multiplier, mana_capacity_flag)
    
    def __str__(self):
        return_string = f"Con Mana: {self.level:,}"
        return return_string

class Stat(Attribute):
    def __init__(self, 
                 name='',
                 discription='', 
                 isparent = False,
                 childstats = {},
                 mana_multiplier=1, 
                 mana_capacity_flag=False,
                 level = 0
                 ):
        super().__init__(name, discription, mana_multiplier, mana_capacity_flag, level)
        
        self._acronym = self.name[:3]

        self._isparent = isparent
        self._child_stats = {}
        self._parent_stat = None
        self._power = 1
    
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
        if isinstance(parent, Stat):
            self._parent_stat = parent
        else:
            print("ERROR parent stat needs to be class <Stat>")

    
    @property
    def power(self):
        return self._power
    @power.setter
    def power(self, power):
        self._power = round(1.01 ** self.level, 2)

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
            self.power = None
            if isinstance(self.parent_stat, Stat):
                self.parent_stat.level = None #just need it to equal to something
        else:
            self._level = floor(self.average_levels())
            if isinstance(self.parent_stat, Stat):
                self.parent_stat.level = None
                self.power = None
        self.calculate_capacity_multiplier()

    
    def add_child_stat(self, *args):
        for stat in args:
            if isinstance(stat, Stat):
                self.isparent = True
                stat.parent_stat = self
                self._child_stats[stat.name] = stat
            else:
                print(f'\nThe added instance <{stat}> is not a class Stat\n')
    
    
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
    def __init__(self, name='', discription='', mana_multiplier=1, mana_capacity_flag=False):
        super().__init__(name, discription, mana_multiplier, mana_capacity_flag)
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
        self.calculate_capacity_multiplier()
        self.mastery= None
    
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
    def mastery(self, mastery):
        if not self.basics:
            if self.level == 0:
                self._mastery = basic
            elif self.level > 0 and self.level <= 100:
                if self.mastery.name != beginner.name:
                    self._mastery = beginner
                    self.calculate_capacity_multiplier()
        else:
            if self.level == 0:
                if self.mastery.name != beginner.name:
                    self._mastery = beginner
                    self.calculate_capacity_multiplier()
            elif self.level > 0 and self.level <= 109:
                if self.mastery.name != intermediate.name:
                    self._mastery = intermediate
                    self.calculate_capacity_multiplier()
            elif self.level > 109 and self.level <= 1000:
                if self.mastery.name != expert.name:
                    self._mastery = expert
                    self.calculate_capacity_multiplier()
            elif self.level > 1001 and self.level <= 10000:
                if self.mastery.name != master.name:
                    self._master = master
                    self.calculate_capacity_multiplier()
    
    def calculate_capacity_multiplier(self):
        #need an initial value based on the type of skill
        # will be multiplied by level
        #mastery multiplier will 
        if self.affects_mana_capacity:
            self.mana_capasity_multiplier = round(self.mana_capasity_multiplier * 1.01 ** (self.level* self.mastery.multiplier),2)