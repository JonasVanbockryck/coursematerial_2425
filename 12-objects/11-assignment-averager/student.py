from statistics import mean
class Averager:
    # The constructor takes no parameters.
    def __init__(self):
        self.numlist = list()

    # A method add(value) adds value to the list of values.
    def add(self, value):
        self.numlist.append(value)
    
    # A method average() returns the average of all values that have been previously added.
    def average(self):
        return mean(self.numlist)
    
    # A method reset() that lets the object forget about all previously added values.
    def reset(self):
        list.clear(self.numlist)
