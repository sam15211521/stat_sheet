from stat_classes import Skills 


#here is the default template
#default = Skills(name= '',
#                 basic= False,
#                 level= 0,
#                 total_mana_cost= 0,
#                 stat_multiplier= 0,
#                 tagged_stats= [],
#                 discription= (
#f"""_________________________
#discription goes here
#_________________________""",
#                             )
#                 )

energy_circulation = Skills(name= 'Energy Circulation',
                 basic= True,
                 level= 0,
                 stat_multiplier= 0.0003,
                 tagged_stats= ["Energy Potential", 
                                "Magic Resistance",
                                "Magic Strength"],
                                )
                    
energy_circulation.discription=["circulate mana throughout your body in an attept to harness it",
                                "[passive - improves Energy Potential, Magic Regeneration",
                                f"and Magic Strength by {energy_circulation.stat_multiplier*100}% ({energy_circulation.stat_multiplier}) per level]",
                                "_________________________",]

energy_conversion = Skills(name= 'Energy conversion',
                 basic= False,
                 level= 0,
                 stat_multiplier= 0.0003,
                 tagged_stats= ["Mana Condensation"],
)
energy_conversion.discription=["Give Energy a flavor or conept based on your understanding of the concept",
                              f"[passive - improves amount of mana condensation by {energy_conversion.stat_multiplier*100}% ({energy_conversion.stat_multiplier}) per level]",
                              "_________________________",]