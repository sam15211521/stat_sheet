from stats import MajorStat, Stat ,Skill, CondensedMana

class Character():
    _dict_of_characters = {} 
    def __init__(self, name = '', race = ''):
        self._dict_of_kills = {}
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
    
    def __str__(self):
        string = f"""
{self.name} | {self.level.name}: {self.level.level}| {self.condensed_mana.name}: {self.condensed_mana.level}
{self.health.name}: {self.health.level}/{self.max_health.level} | Mana: {self.current_mana.level}/{self.max_mana.level}
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
    def level(self, mana):
        self._level = mana

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
    def template(self):
        return self._template
    @template.setter
    def template(self, mana):
        self._template = mana
    
    def use_conensed_mana(self, amount):
        self.condensed_mana.level -= amount

    def add_condensed_mana(self, amount):
        self.condensed_mana.level += amount
    
    def kills_character(self, killed):
        if isinstance(killed, Character):

            self.dict_of_kills[killed.name] = killed
            pass
    


ben = Character("Ben")
monster = Character(name="Mana Condensate", race="Mana Condensate")
print(monster.__dict__)
print(ben)