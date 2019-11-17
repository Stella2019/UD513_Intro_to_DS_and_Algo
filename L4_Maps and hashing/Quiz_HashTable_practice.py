"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        
        key = self.calculate_hash_value( string )
        
        if self.table[key] == None:
            self.table[key] = [ string ]
        else:
            self.table[key].append( string )
        
        pass
        return
    

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        
        key = self.calculate_hash_value( string )
        slot = self.table[ key ]
        if (None == slot) or (string not in slot):
            return -1
        else:
            return key    
        

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        
        # hash value = 100 * ASCII code of string[0] + ASCII code of string[1]
        
        hash_value = 100 * ord(string[0]) + ord(string[1])
        return hash_value
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print( hash_table.calculate_hash_value('UDACITY') )

# Test lookup edge case
# Should be -1
print( hash_table.lookup('UDACITY') )

# Test store
hash_table.store('UDACITY')
# Should be 8568
print( hash_table.lookup('UDACITY') )

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print( hash_table.lookup('UDACIOUS') )
