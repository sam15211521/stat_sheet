class test():
    def __init__(self):
        self._ann = 8
    
    @property
    def ann(self):
        return self._ann
    
    @ann.setter
    def ann(self, value):
        self._ann = value

class quesistion(test):
    def __init__(self):
        super().__init__()
    
    @property
    def ann(self): 
        return self._ann
    
    @ann.setter
    def ann(self, value):
        if isinstance(value, int):
            self._ann = value
        else:
            return TypeError

dd = quesistion()

dd.ann = 9
print(dd.ann)
