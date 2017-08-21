class Clock:
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)
boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
'''

(a) What does the code print out? If you aren't sure, create a Python file and run it.

10:30

(b) Why does it print what it does? (Are boston_clock and paris_clock different objects?
Why or why not?)

boston_clock and paris_clock are two names for the same object. This is called "aliasing."

'''