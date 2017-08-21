from graphics import *
import time

class DigitalClock:
    def __init__(self,hour,minute,sec):
        self.hour = hour%12
        self.min = minute%60
        self.sec = sec%60
       # self.time = "Time"
        self.ampm = 'am'
        if hour > 12:
            self.ampm = 'pm'                   
        #print(self.hour,self.min, self.sec)
        self.rect = Rectangle(Point(0,0),Point(200,100))
    def draw(self,win,d):
        self.rect.draw(win)
        self.rect.setFill('blue')
        self.time = Text( Point( 100, 50 ), d)
        self.time.draw(win)
        
    def __str__(self):
       timestr = " "+str(self.hour)+':'+str(self.min)+':'+str(self.sec)+' '+self.ampm
       return str(timestr)
    
#def main()
        
win = GraphWin("Digital Clock",300,300)
d = DigitalClock(15,30,23)
d.draw(win,d)

        

    
'''

purpose: display time in HH:MM::SS: am/pm
# create the graphics window
new_win = GraphWin("Digital Clock", 300, 300)
# create a text objects centered at (100, 100)
msg1 = Text( Point( 100, 100 ), "Hello, world!" )
#time = time.ctime()
msg2 = Text( Point( 100, 200 ), time.strftime("%I:%M:%S %p"))
msg1.draw( new_win )
msg2.draw( new_win )
# process events
'''
