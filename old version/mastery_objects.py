from mastery_class import Mastery 
# these are the Mastery objects
basic = Mastery(name ="Basic",
               minimum_level= 0,
               maximum_level=100,
               requires_basic= False,
               multiplier= 1,
               discription= ["have a non-system amount of ability for that skill."],
               )
beginner = Mastery(name ="Beginner",
                   minimum_level= 1,
                   maximum_level= 100,
                   requires_basic= False, 
                   multiplier= 1.5,
                   discription= [
                'Skills boosted by mana, yet not capable of much strength.',
                'Learn more about the skill and level it up as well.',
                '(Cannot progress over 100 without the basics)',
                   ]
                    ) 
                      
intermediate = Mastery(name = "Intermediate",
                   minimum_level= 1, 
                   maximum_level= 109,
                   requires_basic= True, 
                   multiplier= 3,
                   discription= [
                       "You know the basics!", 
                        "And you even have some ability in it!", 
                        "Keep training and", 
                        "leveling the skill up with mana to make it shine"]
#'You know the basics! And you even have some ability in it!',
#'Keep Training and leveling the skill up with mana',
#'to make it shine!',
#                   ] 
)

expert = Mastery(name ="Expert",
                   minimum_level= 110,
                   maximum_level= 1000,
                   requires_basic= True,
                   multiplier= 6,
                   discription= ["You know how to use it!",
                                 "You just have to master it.",
                                 "strengthen its levels to unlock its power",
                                 "and practice your skill to mastery"],
                   )
master = Mastery(name = "Master",
                   minimum_level= 1001, 
                   maximum_level=10000,
                   requires_basic= True,
                   multiplier= 12,
                   discription=["Remember though I have nothing",
                                "left to to teach you,",
                                "never will you stop learning,", 
                                "growing"],
                   )