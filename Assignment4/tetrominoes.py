from graphics import *
''' class- block : it conveters the points into pixels and displays the block of pixel 30
    it calls the super class 
'''

class Block(Rectangle):
    starting_num=0
    def __init__(self,points,color):
        # to convert the points into pixels
        x = points.getX()*30
        y = points.getY()*30
        
        '''calling super class '''
               
        #Rectangle.__init__(self,Point(Block.starting_num,y),Point(Block.starting_num+30,y))
        Rectangle.__init__(self,Point(x,y+30),Point(x+30,y))
        ''' another way to call super class constructor
        super(Block,self).__init__(self,Point(x+30,y),Point(x,y+30))
        '''
        # to fill the block
        Rectangle.setFill(self,color)

class Shape:
    def __init__(self,lst,color):
      #  print(lst[0])
       self.block1 = Block(lst[0],color)
       self.block2 = Block(lst[1],color)
       self.block3 = Block(lst[2],color)
       self.block4 = Block(lst[3],color)
    def draw(self,win):
        self.block1.draw(win)
        self.block2.draw(win)
        self.block3.draw(win)
        self.block4.draw(win)
        
class I_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x -2, center.y),
                  Point(center.x -1, center.y),
                  Point(center.x , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x-1,center.y),
                  Point(center.x,center.y),
                  Point(center.x+1,center.y),
                  Point(center.x+1,center.y+1)]
        Shape.__init__(self, coords, "orange")

class L_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x-1,center.y+1),
                  Point(center.x-1,center.y),
                  Point(center.x,center.y),
                  Point(center.x+1,center.y)]
        Shape.__init__(self, coords, "CornflowerBlue")

class O_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x-1,center.y+1),
                  Point(center.x-1,center.y),
                  Point(center.x,center.y),
                  Point(center.x,center.y+1)]
        Shape.__init__(self, coords, "red")

class S_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x-1,center.y+1),
                  Point(center.x,center.y),
                  Point(center.x,center.y+1),
                  Point(center.x+1,center.y)]
        Shape.__init__(self, coords, "green")

class T_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x-1,center.y),
                  Point(center.x,center.y),
                  Point(center.x,center.y+1),
                  Point(center.x+1,center.y)]
        Shape.__init__(self, coords, "yellow")

class Z_shape(Shape):
    def __init__(self,center):
        coords = [Point(center.x-1,center.y),
                  Point(center.x,center.y),
                  Point(center.x,center.y+1),
                  Point(center.x+1,center.y+1)]
        Shape.__init__(self, coords, "pink")
        
        
#main method
def main():
    
    win = GraphWin("Tetrominoes",900,150)
    # a list of shape classes
    tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
    x = 3
    for tetromino in tetrominoes:
        shape = tetromino(Point(x, 1))
        shape.draw(win)
        x += 4
        
    win.getMouse()
    win.close()

main()
