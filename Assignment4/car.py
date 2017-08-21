''' Drawing the car'''
from graphics import *
from wheel import *
class Car :
    def __init__(self,center1,radius1,center2, radius2,height):
        self.wheel_1 = Wheel(center1, 0.6*radius1, radius1)
        self.wheel_2 = Wheel(center2, 0.6*radius2, radius2)
        
        x1 = center1.getX()
        y1 = center1.getY()
        x2 = center2.getX()
        y2 = center2.getY()
        self.rect = Rectangle(Point(x1-height,y1),Point(x2+height,y2-height))
       
    def draw(self,win):
        self.wheel_1.draw(win)
        self.wheel_2.draw(win)
        self.rect.draw(win)
        

def main():
    new_win = GraphWin("A Car", 700, 300)
    car1 = Car(Point(50, 50), 15, Point(100,50), 15, 40)
    car1.draw(new_win)
    
    new_win.getMouse()
    new_win.close()

main()
