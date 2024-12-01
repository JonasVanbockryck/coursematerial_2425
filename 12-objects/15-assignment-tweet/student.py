# Create a class Tweet:
class Tweet:
    # It has two private fields: message and max_length.
    # Its constructor takes two parameters allowing you to initialize these fields.
    def __init__(self, message, max_length):
        self.__message = message
        self.__max_length = max_length
    
    # It has a public property message (get & set) which gives you access to the tweet's message. 
    @property
    def message(self):
        return self.__message
    
    # The setter must guard against oversized tweets: if the new value exceeds the maximum length, it gets truncated.
    @message.setter
    def message(self, value):
        self.message = value
        self.truncate_message()
    
    @property
    def max_length(self):
        return self.__max_length
    
    @max_length.setter
    def max_length(self, value):
        # max_length must at least be 1. If the user sets it to a lower value, raise a ValueError.
        if value < 1:
            raise ValueError("max_length must be at least 1")
        
        # if max_length is set to a new value, it has to make sure that the current message doesn't exceed it. 
        # If it does, the message gets truncated.
        if value > self.max_length:
            self.max_length = value
            self.truncate_message()
        else:
            self.max_length = value
    
    def truncate_message(self):
        length_local = len(self.message)

        if length_local > self.max_length:
            self.message = self.message[0:length_local+1]