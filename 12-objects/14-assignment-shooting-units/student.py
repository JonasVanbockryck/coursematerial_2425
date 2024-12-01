class Unit:
    # It has three private fields: health, firepower and armor.
    # The constructor allows to initialize all three. 
    # It checks that all three are positive (>= 0), otherwise it throws a ValueError.
    def __init__(self, health, firepower, armor):
        if health >= 0 and firepower >= 0 and armor >= 0:
            self.__health = health
            self.__firepower = firepower
            self.__armor = armor
        else:
            raise ValueError("Values need to be positive you fucking moron.")
    
    # Readonly properties health, firepower and armor give public access to the unit's information.
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self,value):
        self.__health = value
    
    @property
    def firepower(self):
        return self.__firepower
    
    @firepower.setter
    def firepower(self,value):
        self.__firepower = value
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,value):
        self.__armor = value
    
    # A method shot_by(other) computes what happens if self is being shot by some other unit other. 
    # This method decreases self.health by the correct amount. 
    # SELF health lost= OTHER firepower− SELF armor
    # The health cannot go below 0.
    def shot_by(self, other):
        if isinstance(other, Unit):
            damage_taken = max((other.firepower - self.armor), 0)
            self.health -= damage_taken
            self.health = max(self.health, 0)

selff = Unit(0, 0, 5)
otherr = Unit(5, 50, 10)

selff.shot_by(otherr)