class Counter:
    def __init__(self):
        # Internally, it keeps track of a count, i.e., an integer.
        # The constructor initializes this count to 0.
        self.__count = int(0)

    # You can retrieve the count using a readonly property named count.
    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        self.__count = value
    
    # A method increment() adds 1 to this count.
    def increment(self):
        self.count += 1
    
    # You can reset the count to 0 using a method reset().
    def reset(self):
        self.count = 0