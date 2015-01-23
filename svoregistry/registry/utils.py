def xstr(s):
    return '' if s is None else str(s)

def validate_vin(vin):
    pass
    #check that vin is 17 characters
    #or, if 9 characters, prepend 1FABP28T
    #1-8 should be 1FABP28T
    #9 should be a number or X
    #10 is model year: E=1984, F=1985, G=1986
    #11 is F
    #12-17 is unit number starting at 100001
    
    #reject if beginning isn't 1FABP28T
    #warn for other mistakes but accept value
    
    #return year (if valid) and char index of any values that may need correction