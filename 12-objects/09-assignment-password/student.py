class Password:
    # Its constructor takes a string that represents a password.
    def __init__(self, wachtwoord):
        # It stores this password in a private field named password (adapt this name as needed).
        self.__password = wachtwoord
    
    # no getter, we can access this private field ourself, but no one else can.

    # Define a method verify(string) that checks if the given string is equal to the password.
    def verify(self, string):
        if string == self.__password:
            print ("true")
            return True
        else:
            print ("false")
            return False