class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
    
    def is_empty(self):
        # this means it's empty
        if self.lower > self.upper:
            return True
        # this means its not
        else:
            return False
    
    def contains(self, value):
        if isinstance(value, Interval):
            if self.is_empty() == True or value.is_empty() == True:
                return False
            
            # we make a single set that contains every number within the interval of "self". 
            # aka, self.lower, self.upper and everything inbetween
            seen_self = set(range(self.lower, self.upper + 1))
            
           # we go through the range of value.then if anything within is found within the range, we return True
            for x in range(value.lower, value.upper + 1):
                if x in seen_self:
                    return True
            
            # if we can't find any overlap, return False.
            return False
    
    def old_hacky_contains(self, value):
        if isinstance(value, Interval):
            if self.is_empty() == True or value.is_empty() == True:
                return False
            
            # we have two blank sets. done because sets are fast.
            seen_self = set()
            seen_value = set()

            # every entry in "self" gets added to a set
            for x in range(self.lower, self.upper + 1):
                seen_self.add(x)
            
            # every entry in "value" gets added to a set
            for x in range(value.lower, value.upper + 1):
                # if an entry in this range was seen in "self", we just return true because it was contained in there.
                # otherwise, we continue on adding everything to the set
                if x in seen_self:
                    return True
                else:
                    seen_value.add(x)
                
            return False

    def overlaps_with(self, other):
        if self.contains(other) == True:
            return True
        else:
            return False