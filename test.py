class adkd():
    def __init__(self, name, level, race):
        self.name = name
        self.race = race
        self.level = level
entry = adkd("cat", 5, 'cat')                                      
#entry_structure = {entry.race: {'count': 1, 
#                                'characters': {'level': {entry.level:{entry.name: {'information'}}}}}}
                #the list       #the kind of enemy     #what level each was at # 
#{what race:{how many, character: {level:{level:{name{information}}}}}}
dic = {}

def adding(entry):
    global dic
    if isinstance(entry, adkd):
        if entry.race not in dic:
            dic[entry.race] = {"count": 1, entry.name: entry.__dict__}
        else:
            dic[entry.race]['count'] = dic[entry.race]['count'] + 1 
            dic[entry.race][entry.name] = entry.__dict__
    else:
        print('ERROR: entry must be of class <adkd>')
            
            
first = adkd("cat1", 5, 'cat')
first2 = adkd("cat2", 5, 'cat')
second = adkd("dog1", 2, 'dog')
second2 = adkd("dog2", 2, 'dog')
adding(first)
adding(first2)
adding(second)
adding(second2)
for key, value in dic.items():
    print(key, value) 