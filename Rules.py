
Noterminal=[ 'PROG' , 'PROC' , 'GORP' , 'var' , '(' , ')' , 'walk' , 
    'jump' , 'jumpTo', 'veer' , 'look' , 'drop' , 'grab', 'get' ,
    'free' , 'pop' , 'walk' , 'if', 'else' , 'while' , 'do' , 
    'isfacing' , 'isValid' , 'canWalk' , 'not' , 'north' , 
    'south' ,  'east' , ' west' , 'right' , ' left' , ' front' , 
    'back' ] 

function=['walk' , 'jump' , 'jumpTo', 'veer' , 'look' , 'drop' ,
     'grab', 'get' , 'free' , 'pop' , 'walk' ]
    
def Isterminal(token):
    if token in Noterminal:
        return True 
    else:
        return False

def Isfunction(token):
    if token in function:
        return True 
    else:
        return False