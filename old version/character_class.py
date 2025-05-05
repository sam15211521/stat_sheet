import shutil 
import inspect
from stat_classes import Stat, Skills, MajorStats


class Character: #any entitiy in the world

    def __init__(self, name= '', race= '',):
        self.list_of_kills = []

        self.name= name
        self.race= race
        # the major stats
        self.health= MajorStats(name= 'Health')
        self.mana= MajorStats(name= 'Mana')
        self.current_mana= MajorStats(name= 'Current Mana')
        self.level= MajorStats(name= 'Level')
        self.condensed_mana= MajorStats(name= 'Condensed Mana')
        self.total_condensed_mana= MajorStats(name="Total Condensed Mana")

        # the regular stats

        # strength
        self.physical_strength= Stat(name= 'Physical Strength')
        self.magical_strength= Stat(name= 'Magical Strength')
        self.strength= Stat(name= 'Strength')
        self.strength.childstats = [self.magical_strength, self.physical_strength] #add child classes here otherwise does not work
        self.strength.isparent= True #sets it at true after getting child stats otherwise it throws errors for stats.average in class
        self.physical_strength.parent_stat = self.strength
        self.magical_strength.parent_stat = self.strength
        
        # resistance
        self.physical_resistance= Stat(name= 'Physical Resistance')
        self.magic_resistance= Stat(name= 'Magic Resistance')
        self.spiritual_resistance= Stat(name= 'Spiritual Resistance')
        self.resistance= Stat(name='Resistance')
        self.resistance.childstats= [self.physical_resistance, self.spiritual_resistance, self.magic_resistance]
        self.resistance.isparent= True 
        self.physical_resistance.parent_stat = self.resistance
        self.spiritual_resistance.parent_stat = self.resistance
        self.magic_resistance.parent_stat = self.resistance

        # regeneration
        self.health_regeneration= Stat(name= 'Health Regeneration')
        self.mana_regenration= Stat(name= 'Mana Regeneration')
        self.regeneration= Stat(name= 'Regeneration')
        self.regeneration.childstats= [self.physical_resistance, self.magic_resistance]
        self.regeneration.isparent= True 
        self.health_regeneration.parent_stat= self.regeneration
        self.mana_regenration.parent_stat= self.regeneration
        

        # endurance
        self.physical_endurance= Stat(name= "Physical Endurance")
        self.mana_endurance= Stat(name= 'Mana Endurance')
        self.endurance= Stat(name= 'Endurance')
        self.endurance.childstats= [self.physical_endurance, self.mana_endurance]
        self.endurance.isparent= True
        self.physical_endurance.parent_stat= self.endurance
        self.mana_endurance.parent_stat= self.endurance

        # agility
        self.speed= Stat(name="Speed")
        self.coordination= Stat(name='Coordination')
        self.agility= Stat(name='agility')
        self.agility.childstats= [self.speed, self.coordination]
        self.agility.isparent= True

        # energy potential and mana condensation
        self.energy_potential= Stat(name= 'Energy Potential')
        self.mana_condensation= Stat(name= 'Mana Condensation')


        

# when defeating monster gain condensed mana adding it to total and current 
#condensed mana
    def gain_condensed_mana(self,           
                            monster=None,   
                            condensed_mana=0,):
        if isinstance(monster, Character) and condensed_mana == 0:
            self.condensed_mana.level += monster.level.level
            self.total_condensed_mana.level += monster.level.level
        else:
            print("false")
        return f'+{self.condensed_mana.level}' #returns string showing how much is used

    # subtracts condensed mana by amount
    def use_condensed_mana(self,            
                           amount):
        self.condensed_mana.level -= amount

    #increases the level of a stat 
    def increase_stat(self, amount, stat):                 
        if(not isinstance(stat, (MajorStats, Stat))):
            raise ValueError("must be instance of class MajorStat or Stat")
        elif stat.isparent is True:
            raise ValueError("Cannot be a Main Stat")
        else:
            stat.level += amount
            self.condensed_mana.level -= amount
    
    # records which characters are killed by Character
    def kills_character(self, killed):          
        self.list_of_kills.append((killed.name, killed.level.level, self.level.level))
        self.gain_condensed_mana(killed)
    
    #gives a string that tels exactly which enemies were killed with their level
    def extract_kills_name_level(self):
        lst = self.list_of_kills
        return_stirng = 'level | Enemy : Level'
        for kill in lst:
            return_stirng += f'\n lv.{kill[2]} | {kill[0]}: {kill[1]}'
        return return_stirng

    def get_kills(self):
        return_statment = self.extract_kills_name_level()
        return return_statment


