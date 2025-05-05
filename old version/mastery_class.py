number_of_masteries = []
import shutil
class Mastery:
    def __init__(self,
                name,
                minimum_level=0,
                maximum_level=1,
                requires_basic= False,
                multiplier=1,
                discription =""
                ):
        self.name = name
        self.maximumlevel = maximum_level
        self.minimumlevel = minimum_level
        self.requriesbasic = requires_basic
        self.multiplier = multiplier
        self.discription = discription
        number_of_masteries.append(self.name)
    def unpack_string(self, string=[]):
        unpacked_list= []
        for item in string:
            if type(item) is str:
                unpacked_list.append(item)
            elif type(item) is list:
                for line in item:
                    unpacked_list.append(line)
        return unpacked_list

    def center_string(self, strings=[]):
        unpacked_list= self.unpack_string(string=strings)
        return_string=''
        for item in unpacked_list:
            return_string += f'{item.center(shutil.get_terminal_size().columns)}'
        return return_string
    def __str__(self):
        return_string= '' 
        line1= f'{self.name}'
        line2= f'Discription:'
        line3= f'{self.center_string(self.discription)}'
        line4= ''
        line5= f'level range: {self.minimumlevel} - {self.maximumlevel}'
        line6= f'Basics requirement: {"Yes" if self.requriesbasic is True else "No"}'
        line7= f'power multiplier: {self.multiplier}'
        return_string += self.center_string(strings= [line1, line2, line3, 
                                                      line4, line5, line6])
        return return_string