def xstr(s):
    return '' if s is None else str(s)

def validate_vin(vin):
    vin = vin.upper()
    is_svo = True
    is_valid = True
    year = '19XX'
        
    #first 8 characters is what determines it is an svo
    if vin[0:8] != '1FABP28T':
        is_svo = False
        is_valid = False
    
    #9th character is a digit or X
    if is_valid:
        if vin[8] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']:
            is_valid = False
    
    #10th character determines year, but cannot differentiate between 1985 and 1985.5. default to 1985    
    if is_valid:
        if vin[9] == 'E':
            year = '1984'
        elif vin[9] == 'F':
            year = '1985'
        elif vin[9] == 'G':
            year = '1986'
        else:
            is_valid = False
        
    #11th character is F, which means it was built at the Dearborn assembly plant
    if is_valid:
        if vin[10] != 'F':
            is_valid = False
                
    #12-17 character is a unit number starting from 100001
    if is_valid:
        if vin[11:17].isdigit() == False:
            is_valid = False
        elif int(vin[11:17]) < 100001:
            is_valid = False

    return (is_svo, is_valid, year)
