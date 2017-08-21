from math import sqrt
def ball_collide(b1=[],b2=[]):
    return (abs(sqrt((b2[0] - b1[0]) ** 2 + (b2[1] - b1[1]) ** 2)))
b1=[5,10,20]
b2=[5,60,20]
if ball_collide(b1,b2)>(b2[2]+b1[2]):
    print("Collide")
else:
    print("Not Collide")