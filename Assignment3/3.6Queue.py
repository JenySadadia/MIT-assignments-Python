class stack(object):
    def __init__(self):
     self.vals = [] #initializing Queue set to null

    def push(self, e):   #method for pushing data into set
        if not e in self.vals:
            self.vals.append(e)

    def pop(self):    #pops value
        try:
            del self.vals[0]
        except IndexError as e:
            print("Sorry you cannot pop element because stack is empty....")

    def __str__(self):
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
stack = stack()
stack.push(5)
stack.push(6)
print(stack)
stack.pop()
print(stack)
stack.push(7)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)