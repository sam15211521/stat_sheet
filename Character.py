from stats import MajorStat, Stat ,Skill, CondensedMana, HiddenManaStat
import math

class Character():
    _dict_of_characters = {} 
    def __init__(self, name = '', race = '', body_mana_multiplier = 54433106):
        self._dict_of_kills = {}
        self._dict_of_skills = {}
        self._dict_of_major_stats = {}
        self._dict_of_stats = {}
        self._name = name
        self._race = race

        # the major stats
        self._health = MajorStat("Health")
        self._max_health = MajorStat("Max Health")
        self._max_mana = MajorStat("Max Mana")
        self._current_mana = MajorStat("Mana")
        self._level = MajorStat("Level")
        self._condensed_mana = CondensedMana("Condensed Mana")
        self._total_condensed_mana = MajorStat("Total Condensed Mana")

        self._hidden_mana_stat = HiddenManaStat("Base Mana Capacity", 
                                           mana_capacity_flag=True,)
        self.hidden_mana_stat.level = body_mana_multiplier
        
        self._stat_and_skills_effecting_mana = {}

        #regular stats
        
        #Strength
        self.strength = Stat(name = "Strength", isparent=True)
        self.physical_strength = Stat(name = "Physical Strength")
        self.magical_strength = Stat(name = "Mana Strength",
                                     mana_capacity_flag=True,
                                     mana_multiplier=1.5)
        self.strength.add_child_stat(self.physical_strength, 
                                     self.magical_strength)

        #Resistance
        self.resistance = Stat(name="Resistance", isparent=True)
        self.physical_resistance = Stat(name="Physical Resistance")
        self.magic_resistance = Stat(name="Mana Resistance",
                                     mana_capacity_flag=True)
        self.spiritual_resistance = Stat(name="Spiritual Resistance")
        self.resistance.add_child_stat(self.physical_resistance,
                                       self.magic_resistance,
                                       self.spiritual_resistance)
        
        #Regeneration
        self.regeneration = Stat(name="Regeneration", isparent=True)
        self.health_regen = Stat(name="Health Regeneration")
        self.mana_regen= Stat(name="Mana Regeneration",
                              mana_capacity_flag=True)
        self.regeneration.add_child_stat(self.health_regen,
                                         self.mana_regen)
        
        #Endurance
        self.endurance = Stat(name="Endurance", isparent=True)
        self.physical_endurance = Stat(name="Physical Endurance")
        self.magic_endurance = Stat(name="Magic_Endurance",
                                    mana_capacity_flag=True)
        self.endurance.add_child_stat(self.physical_endurance,
                                      self.magic_endurance)
        
        #Agility
        self.agility = Stat(name="Agility", isparent=True)
        self.speed = Stat(name="Speed")
        self.coordination = Stat(name="Coordination")
        self.agility.add_child_stat(self.speed, 
                                    self.coordination)
        
        #Energy potential
        self.energy_potential = Stat(name= "Energy Potential", 
                                     mana_capacity_flag=True,
                                     mana_multiplier=1.5)

        self.add_stat_to_mana_calc(
                                   self.magic_endurance,
                                   self.magic_resistance,
                                   self.magical_strength,
                                   self.mana_regen,
                                    )
        self.calculate_max_mana()
        self.current_mana.level = self.max_mana.level
        self.add_to_dict_stats_and_major_stats()
    
    def __str__(self):
        string = f"""
{self.name} | {self.level.name}: {self.level.level}| {self.condensed_mana.name}: {self.condensed_mana.level}
{self.health.name}: {self.health.level}/{self.max_health.level} | Mana: {self.current_mana.level}/{self.max_mana.level}
{self.resistance.name}: {self.resistance.level} | {self.strength.name}: {self.strength.level}
{self.regeneration.name}: {self.regeneration.level} | {self.endurance.name}: {self.endurance.level}
{self.energy_potential.name}: {self.energy_potential.level} | {self.agility.name}: {self.agility.level}
"""
        return string
   ##########################################################
   # here are all the propertie setters 
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dict_of_characters(self):
        return self._dict_of_characters
    @dict_of_characters.setter
    def dict_of_characters(self, dictionary):
        if isinstance(dictionary, dict):
            self._dict_of_kills = dictionary
        else: 
            print(f"dictionary of characters must be class <dict>")
    
    @property
    def dict_of_kills(self):
        return self._dict_of_kills
    @dict_of_kills.setter
    def dict_of_character(self, name):
        self._dict_of_kills = name
    @property
    def dict_of_stats(self):
        return self._dict_of_stats
    @dict_of_stats.setter
    def dict_of_stats(self, dict):
        self._dict_of_stats = dict
    
    @property
    def dict_of_major_stats(self):
        return self._dict_of_major_stats
    @dict_of_stats.setter
    def dict_of_major_stats(self, dict):
        self._dict_of_major_stats = dict


    @property
    def race(self):
        return self._race
    @race.setter
    def race(self, name):
        self._race = name
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, health):
        self._health = health
    
    @property
    def max_health(self):
        return self._max_health
    @max_health.setter
    def max_health(self, health):
        self._max_health = health

    @property
    def max_mana(self):
        return self._max_mana
    @max_mana.setter
    def max_mana(self, mana):
        self._max_mana = mana
    
    @property
    def current_mana(self):
        return self._current_mana
    @current_mana.setter
    def current_mana(self, mana):
        self._current_mana = mana

    @property
    def level(self):
        return self._level
    @level.setter
    def level(self, level):
        self._level = level

    @property
    def condensed_mana(self):
        return self._condensed_mana
    @condensed_mana.setter
    def condensed_mana(self, mana):
        self._condensed_mana = mana
    
    @property
    def total_condensed_mana(self):
        return self._total_condensed_mana
    @total_condensed_mana.setter
    def total_condensed_mana(self, mana):
        self._total_condensed_mana = mana
    @property
    def hidden_mana_stat(self):
        return self._hidden_mana_stat
    @hidden_mana_stat.setter
    def hidden_mana_stat(self, mana):
        self._hidden_mana_stat = mana

    @property
    def stat_and_skills_effecting_mana(self):
        return self._stat_and_skills_effecting_mana
    @stat_and_skills_effecting_mana.setter
    def stat_and_skills_effecting_mana(self, stat):
        self._stat_and_skills_effecting_mana = stat
    
    @property
    def dict_of_skills(self):
        return self._dict_of_skills
    @property
    def template(self):
        return self._template
    @template.setter
    def template(self, mana):
        self._template = mana
    
    ###########################################################
    #other misc methods
    
    def add_skill(self, skill):
        if isinstance(skill, Skill):
            self._dict_of_skills[skill.name] = skill
            if skill.affects_mana_capacity:
                self.add_skill_to_mana_calc(skill)
    
    def use_conensed_mana(self, amount):
        self.condensed_mana.level -= amount

    def add_condensed_mana(self, amount):
        self.condensed_mana.level += amount
    
    def kills_character(self, killed):
        if isinstance(killed, Character):
            dict_of_the_killed ={
                                "name": killed.name,
                                "race": killed.race,
                                "level": killed.level.level,
            }
    
    def add_skill_to_mana_calc(self, *args):
        for skill in args:
            if isinstance(skill, Skill):
                self.stat_and_skills_effecting_mana[skill.name] = skill
                self.calculate_max_mana()

    def add_stat_to_mana_calc(self, *args):
        for stat in args:
            if isinstance(stat, Stat):
                self.stat_and_skills_effecting_mana[stat.name] = stat
                self.calculate_max_mana()
        
        
    
    def calculate_max_mana(self):
        #max mana is based on first the body's iniate abilities
        #average is 2 
        #max mana based on the <hidden>, <magic_resistance>,
        #<magic_endurance>, <magic_regeneration>, <Energy Potential>
        #and misc skills that will add to the calculation. 
        #average mana capacity of a person is 100 Mp 100,000,000 p
        #a person with a mana deficiency has a capacity of 1 -5 Mp
        #ben is 5000 p
        #numbers got crazy with exponential so now lets try 
        # hiden * (stat_multiplier ** stat_multiplier.energy potential)
        # average person's hidden stat needs to multiply to this: 54433106
        stat_skill_multipliers = []
        
        for stat_skill in self.stat_and_skills_effecting_mana.values():
            stat_skill_multipliers.append(stat_skill.mana_capasity_multiplier)
        mana_multiplier = math.prod(stat_skill_multipliers)
        mana_capacity = (self.hidden_mana_stat.level * (mana_multiplier** self.energy_potential.mana_capasity_multiplier))
        if mana_capacity >1000000:
            mana_capacity/= 1000000
            self.max_mana.mana_unit = "Mp"
            self.current_mana.mana_unit = "Mp"
        elif mana_capacity <1000000 and mana_capacity >=20000:
            mana_capacity /= 1000
            self.max_mana.mana_unit ="kp"
            self.current_mana.mana_unit = "kp"
        elif mana_capacity < 20000:
            self.max_mana.mana_unit = "p"
            self.current_mana.mana_unit = "p"
        self.max_mana.level = math.floor(mana_capacity)

        #print(self.max_mana.level, self.max_mana.mana_unit)

        #self.max_mana.level = math.floor(mana_capacity)


        
        #print(stat_skill_multipliers)
        #print('hidden', self.hidden_mana_stat.level)
        #print("EP", self.energy_potential.mana_capasity_multiplier)
        #print('multiplicitive:',mana_multiplier)
        #print(f"mana capacity: {mana_capacity:,} {self.max_mana.mana_unit}")
    

    #stat should be the of the Stat class
    # level should only be an integer
    def add_to_dict_stats_and_major_stats(self, major_stat = False):
        if major_stat:
            if not bool(self._dict_of_major_stats):

                temp = [stat for stat in list(self.__dict__.values()) 
                        if isinstance(stat, Stat) | isinstance(stat, CondensedMana)]

                for stat in temp:
                    self._dict_of_major_stats[stat.name] = stat
            print(self._dict_of_major_stats)
        else:
            if not bool(self.dict_of_stats):

                temp = [stat for stat in list(self.__dict__.values()) 
                        if isinstance(stat, Stat) | isinstance(stat, CondensedMana)]

                for stat in temp:
                    self.dict_of_stats[stat.name] = stat

    def increase_stat_level(self, stat=None, level=1):
        quit_flag = False
        if not isinstance(stat, Stat) and not isinstance(stat, Skill):
            print( "Type Error: selected stat is not a type <Stat> or <Skill>.")
            print(f"is type {type(stat)}")
            quit_flag = True
        if not isinstance(level, int):
            print( "Type Error: level can only increase by integer values")
            quit_flag = True
        if quit_flag:
            return None
        if stat.name in self.dict_of_stats and not stat.isparent:
            stat.level += level
    
    def decrease_stat_level(self, stat=None, level=1):
        quit_flag = False
        if not isinstance(stat, Stat) and not isinstance(stat, Skill):
            print("Type Error: selected stat is not a type <Stat> or <Skill>.")
            print(f"is type {type(stat)}")
            quit_flag = True
        if not isinstance(level, int):
            print("Type Error: level can only increase by integer values")
            quit_flag = True
        if quit_flag:
            return None
        if stat.name in self.dict_of_stats and not stat.isparent:
            stat.level -= level

basicCharacter = Character('basicCharacter')
ben = Character("Ben",body_mana_multiplier=2722) #hiden stat = 15.327
monster = Character(name="Mana Condensate", race="Mana Condensate")
ben.add_skill(Skill(name='Mana Circulation',mana_capacity_flag=True))

ben.increase_stat_level(ben.physical_strength, 9)
ben.increase_stat_level(ben.magical_strength, 10)
ben.decrease_stat_level(ben.physical_strength, 4)
print()
#print(ben)
#print(ben.physical_strength)
#print(ben.magical_s
#print(ben.strength)