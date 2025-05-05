from stat_classes import Stat 

# Strength objects
physical_strength = Stat(name = "Physical Strength",
                         isparent = False,
                         value = 0
                         ) 

magical_strength = Stat(name = "Magical Strength",
                       isparent = False,
                       value = 0
                       ) 
strength = Stat(name = "Strength", # parent stat
                isparent = True,
                childstats = [
                    physical_strength,
                    magical_strength] 
                )


# Resistance objects
physical_resistance = Stat(name = "Physical Resistance",
                         isparent = False,
                         value = 0
                         ) 
 
magical_resistance = Stat(name = "Magical Resistance",
                         isparent = False,
                         value = 0
                         ) 

spiritual_resistance = Stat(name = "Spiritual Resistance",
                         isparent = False,
                         value = 0
                         ) 

resistance = Stat(name = "Resistance", # parent stat
                isparent = True,
                childstats = [
                    physical_resistance,
                    magical_resistance] 
                )

# Regeneration Objects
health_Regeneration = Stat(name = "Health_Regeneration",
                         isparent = False,
                         value = 0
                         ) 


magic_Regeneration = Stat(name = "Magic Regeneration",
                         isparent = False,
                         value = 0
                         ) 


Regeneration = Stat(name = "Regeneration", # parent stat
                isparent = True,
                childstats = [
                    physical_resistance,
                    magical_resistance] 
                )


energy_potential = Stat(name = "Energy Potential", # parent stat
                        isparent = False,
                        value = 0
                        )


mana_condensation = Stat(name = "Mana Condensation", # parent stat
                         isparent= False,
                         value= 0,
                        )