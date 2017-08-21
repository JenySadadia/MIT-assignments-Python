'''
Assignment : 4.4
Purpose:    Designing your own inheritance
'''
class Shoe :
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
class Converse(Shoe):
    def __init__(self,tongueColor,lowHighTop):
        self.tongueColor = tongueColor
        self.brand =  'Converse'
        Shoe.__init__(self,self.tongueColor, self.brand)

class CombatBoot(Shoe):
    def __init__(self,color,brand):
        
        
