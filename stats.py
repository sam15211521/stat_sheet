import statistics


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
        both_lines = line1 +'\n' + line2
        return both_lines
    
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
    
    def add_child_stat(self, stat):
        if self.isparent and isinstance(stat, Stat):
            self._child_stats[stat.name] = stat
            if stat.isparent:
                children = []
                for key in stat.child_stats.keys():
                    print('helloakdk', key)
                    children.append(key)
                print(f'{stat.name} is a Parent stat\n it children are:\n{', '.join(children)}')
        elif not self.isparent:
            print(f"\n<{self.name}> is a Child Stat\n")
            return
        else:
            print(f'\nThe added stat <{stat.name}> is not a Child Stat\n')
    
    @property
    def parent_stat(self):
        return self._parent_stat
    
    @parent_stat.setter
    def parent_stat(self, parent):
        if not self._isparent:
            print('isnotparent')
    
    def print_child_stats(self):
        print(f'the Child Stats of {self.name} are:')
        if self.child_stats == {}:
            print(f"\n{self.name} has no Child Stats\n")
        else:
            for name, stat in self.child_stats.items():
                print(f'Name: {name}, Level: {stat.level}')




class Skill(Attribute):
    pass


a = Attribute(name = 'a')
b = Stat(name = 'b', isparent=True)
c = Stat(name = 'c', isparent=True)
d = Stat(name = 'd')
c1 = Stat(name= 'c1')

c.add_child_stat(c1)
b.add_child_stat(c)
b.add_child_stat(d)


a.name= "we"
a.discription = "we the people"

b.print_child_stats()