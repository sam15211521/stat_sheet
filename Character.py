from stats import MajorStat, Stat ,Skill, CondensedMana

class Character():
    _dict_of_characters = {} 
    def __init__(self, name = '', race = '', body_mana_multiplier = 1):
        self._dict_of_kills = {}
        self._dict_of_skills = {}
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

        self._hidden_mana_stat = MajorStat("Base Mana capacity", 
                                           mana_capacity_flag=True,
                                           mana_multiplier=body_mana_multiplier)
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
                                     mana_capacity_flag=True)

        self.add_stat_to_mana_calc(self.hidden_mana_stat, 
                                   self.magic_endurance,
                                   self.magic_resistance,
                                   self.magical_strength,
                                   self.mana_regen,
                                   self.energy_potential,
                                    )
    
    def __str__(self):
        string = f"""
{self.name} | {self.level.name}: {self.level.level}| {self.condensed_mana.name}: {self.condensed_mana.level}
{self.health.name}: {self.health.level}/{self.max_health.level} | Mana: {self.current_mana.level}/{self.max_mana.level}
{self.resistance.name}: {self.resistance.level} | {self.strength.name}: {self.strength.level}
{self.regeneration.name}: {self.regeneration.level} | {self.endurance.name}: {self.endurance.level}
{self.energy_potential.name}: {self.energy_potential.level} | {self.agility.name}: {self.agility.level}
"""
        return string
    
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
    def template(self):
        return self._template
    @template.setter
    def template(self, mana):
        self._template = mana
    
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
    def add_stat_to_mana_calc(self, *args):
        for stat in args:
            if isinstance(stat, Stat):
                self.stat_and_skills_effecting_mana[stat.name] = stat
        
        
    
    def calculate_max_mana(self):
        #max mana is based on first the body's iniate abilities
        #average is 2 
        initial = self.hidden_mana_stat
        #max mana based on the <hidden>, <magic_resistance>,
        #<magic_endurance>, <magic_regeneration>, <Energy Potential>
        #and misc skills that will add to the calculation. 
        #need to make a dict of the stats and skills that effect it
        stat_multipliers = []
        skill_multipliers = []
        for name, stat_skill in self.stat_and_skills_effecting_mana.items():
            if isinstance(stat_skill, Stat):
                print(name)

                pass
            
            elif isinstance(stat_skill, Skill):
                print(name)
                pass



    


ben = Character("Ben")
monster = Character(name="Mana Condensate", race="Mana Condensate")
print(ben.stat_and_skills_effecting_mana.keys())
ben.add_skill(Skill(name='Mana Circulation',mana_capacity_flag=True))
print(ben.stat_and_skills_effecting_mana.keys())


#ben.calculate_max_mana()