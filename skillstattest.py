from stats import Skill, SkillStat, Stat
from Character import Character

bob = Character(name="Bob")
bob.add_condensed_mana(100)

print(bob)
print(bob._dict_of_stats_affecting_level)

skills = SkillStat(name="Stat Levels")
ab = Skill(name = "boo")
bc = Skill(name = "cat")
print('\n**((^()))\n')
bob.add_skill(ab)
bob.add_skill(bc)
print('\n*))&^%\n')
bob.use_con_mana_to_increase_stat_level(bob.physical_strength, 10)
bob.use_con_mana_to_increase_stat_level(bob.magical_strength, 10)
print('\n#@#', bob, '#@#\n')
bob.use_con_mana_to_increase_stat_level(ab, 12)

print(bob)
print('\n####\n')
print(bob.skills_level)
print()
print(bob)