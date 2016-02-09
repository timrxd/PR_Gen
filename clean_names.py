# List of corrections to bracket names

def clean(name):

    # Xanadu
    if 'Mister Eric' in name:
        return 'Mister Eric'
    if 'dunnobro' in name.lower():
        return 'Dunnobro'
    if 'Logic' in name: # Dangerous
        return 'Logic'
    
    
    # GreyhoundSmash
    if 'Run.' == name:
        return 'Solar'
    #if 'Gorbaty' == name:
    #    return 'CheeseDeezNutz'
    if 'ChesseDeezNutz' == name:
        return 'CheeseDeezNutz'
    
    return name

#end
