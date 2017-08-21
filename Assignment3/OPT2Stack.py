class Stack(object):

    def __init__(self):
     self.vals = [] #initializing Queue set to null

    def insert(self, e):   #method for inserting data into set
        if not e in self.vals:
            self.vals.append(e)

    def remove(self):    #removes value
        try:
            self.vals.pop()
        except IndexError as e:
            print("Sorry you cannot pop element because queue is empty....")

    def __str__(self):
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
queue = Stack()
queue.insert(5)
queue.insert(6)
print(queue)
queue.remove()
print(queue)
queue.insert(7)
queue.remove()
print(queue)
queue.remove()
print(queue)
queue.remove()
print(queue)