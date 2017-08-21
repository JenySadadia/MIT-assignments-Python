class Clock:
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)
clock = Clock('5:30')
clock.print_time('10:30')
'''
(a) What does the code print out? If you aren't sure, create a Python file and run it.

10:30

(b) What does this tell you about giving parameters the same name as object attributes?

They are needlessly confusing. It is less confusing if you give parameters, local variables, 
and attributes different names.
'''