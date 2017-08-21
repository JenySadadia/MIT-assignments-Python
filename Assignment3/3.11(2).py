class Clock:
    def __init__(self,time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
clock = Clock('5:30')
clock.print_time()
'''
(a) What does the code print out? If you aren't sure, create a Python file and run it.

asn: 5:30

(b) Is that what you expected? Why?

Yes, because we printed out the attribute self.time, not the local variable time.
'''