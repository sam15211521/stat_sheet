import shutil
import statistics 
from math import floor as mfloor
from mastery_objects import basic, beginner, intermediate, expert, master

#dict_of_skills = {}
#dict_of_stats = {}
#dict_of_major_stats = {}
#number_of_stats = []
#number_of_skills = []

class Attribute():
    def __init__(self, 
                amount_of_mana= 0, 
                total_mana_invested=0,
                name= ''
                ):
        self.amount_of_mana= amount_of_mana
        self.total_mana_invested= total_mana_invested
        self.name= name
        self.history={}

    def add_mana(self, mana):
        self.amount_of_mana = self.amount_of_mana + mana 
        print(self.amount_of_mana)
        return True



class MajorStats(Attribute):#objects: health, mana, level, condensed mana
    def __init__(self,
                name= '',
                level= 0,
                mana_to_next_level=1,
                power= 1,
                ):
        self.name= name
        self.level= level
        self.mana_to_next_level= mana_to_next_level
        self.power= power
        #dict_of_major_stats.update({name : self})

        
            



class Skills(Attribute):
    def __init__(self, 
                 name='',
                 basic=False,
                 level = None,
                 total_mana_invested = 0,
                 mana_to_next_level=1,
                 mastery= basic,
                 tagged_stats=[],
                 next_level_cost= 0,
                 stat_multiplier= None,
                 discription=''
                 ):
        self.name= name
        self.total_mana_invested= total_mana_invested
        self.mana_to_next_level= mana_to_next_level
        self.basic = basic
        self.level = level
        self.mastery = mastery
        self.next_level_cost = next_level_cost
        self.tagged_stats = tagged_stats
        self.stat_multiplier = stat_multiplier
        self.discription= discription
        self.get_mastery()
                
        

#methods to call properties
    

#methods to enact changes
    def get_mastery(self):
        if self.call_basic() is False and self.call_level() == 0:
            self.mastery = basic
        elif self.call_basic() is False and self.call_level() > 0 and self.call_level() <=100:
            self.mastery = beginner
        elif self.call_basic() is True and self.call_level() >0 and self.call_level() <=109:
            self.mastery = intermediate
        elif self.call_basic() is True and self.call_level() >109 and self.call_level() <=1000:
            self.mastery = expert
        elif self.call_basic() is True and self.call_level() >1000: 
            self.mastery = master 
        return self.center_string(self.mastery.name)
    
    def increase_level(self):
        pass
        
        

class Stat(Attribute):
    def __init__(self,
                 name= '', 
                 isparent= False,
                 childstats = [],
                 level = 0,
                 mana_to_next_level= 0,
                 total_mana_invested= 0,
                 parent_stat = None
                 ):
        self.name= name 
        self.mana_to_next_level= mana_to_next_level
        self.total_mana_invested= total_mana_invested
        self.acronym = name[:3]
        self.parent_stat= parent_stat

        self.isparent = isparent
        self.childstats = childstats
        #number_of_stats.append(self)
        #dict_of_stats[name] = self
        self._level = level 

        #calls the Main stat calculation if stat is a Main Stat
        if self.isparent is True:
            self.main_stat_calculation()

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        self._level = value
        if self.isparent is False:
            self.parent_stat.main_stat_calculation()

    def __str__(self):
        if self.isparent is True:
            line1=f"{self.name}  | level: {self.level}"
            line2=f"it is a {self.call_parent(text = True)}"
            line3=f"it's constituant stats are:"
            line4=self.extract_child_stats()
            return self.center_string(strings= [line1,line2,line3,line4]) 
        else:
            line1= f"{self.name} | level: {self.level}"
            line2= f"it is a {self.call_parent(text = True)}\n"                
            return self.center_string(strings= [line1,line2]) 

    #takes a list from childstats and gives calls the relevant stat's information
    def extract_child_stats(self):
        return_list = []
        for stat in self.childstats:
            return_list.append(f'{stat.name}: {stat.level}')
        return return_list 

    #calculates the value of a Main Stat based on its child stats
    def main_stat_calculation(self):
        child_stat_levels= []
        for stat in self.childstats:
            child_stat_levels.append(stat.level)

        return_statment= int(mfloor(statistics.fmean(child_stat_levels)))
        self.level = return_statment
        return return_statment


    ## here is the methods to call each part
    
    def call_childstats(self, lst_flag = False):
        if lst_flag is True:
            return self.childstats
        else:
            return_string= ", ".join(self.childstats)
            return return_string

    def call_parent(self, text = False):
        if text is False:
            return self.isparent
        else: 
            if self.isparent is True:
                return "Main Stat"
            else:
                return "Child Stat"







    ## here is the methods to change things

    def average_values(self):
        return statistics.mean(stat.level() for stat in self.childstats)
    
    def skill_effects(self,):
        if self.isparent is False:
            pass
        else:
            return False


