#%%
from contextvars import Token
from typing import List
import nltk
import numpy
import Rules as RL

#path
file = 'C:/Users/frawo/Documents/Programacion/LyM/Data/Prueba0.py'

variables={}

directions=[ 'north' , 'south' , 'east' ,  'west' , 'right' , ' left' , ' front' , 
    'back' ]

directionsC=[ 'north' , 'south' , 'east' ,  'west' ]
#%%


def Tokenizer(file: str):
    
    #opening the script
    script = open(file, 'r')

    #list of every line's token
    tokens=[]
    line = script.readline()
    while len(line) !=0:
        #Tokenizing one line
        Tl=nltk.word_tokenize(line)
        tokens.append(Tl)
        line=script.readline()
    return tokens

print(analyzer(file))
# %%

def Analyzer(Matrix: list):
    i=0
    R = True 
    while i < len(matrix) and R:
        line = Matrix[i]
        if (i == 0) and (Matrix[i][0] != 'PROG'):
            R = False
        elif not (RL.Isfunction(line[0])):
            if (line[0] == 'var') :
                R=VarR(line)
        elif (RL.Isfunction(line[0])):
            R = FUNCTIONR(line)
            

#%%

#rules

def VarR( S1: list ):
    R=True
    coma=False
    i = 1
    n=len(S1)
    while (i < n) and R  :

        #Extractin every token of a var Line
        token = S1[i] 

        #using retrictecwords; Not comma succecive; Not iniciating wiht ',' conditions
        if (coma and token == ',') or ((i == 1) and (token == ',')) or (i==n-1 and token != ';') or (not RL.Isterminal(token)):
            R = False
        
        else:
            variables[token]=None

        if token == ',':
            coma = True
    
    return R
        
def PROCR( S1: list ):
    R = True
    PO = False
    i = 1
    n = len(S1)
    while (i < n) and R:
        token = S1[i]

        if (not RL.Isfunction(token)) or (i == n-1 and token != ')' ) or ((token =='(') and PO) \
            or (i != n-1 and token == ')' ) :
            R=False
        
        if (token =='(') and (not PO) :
            PO = True
        
    if not PO :
        R= False

    return R

def FUNCTIONR(S1: list):
    WRs=[]
    R = None
    for word in S1:
        if (word != '(') and (word != ')'):
            WRs.append(word)

    if RL.Isbinary(WRs[0]):
        var1 = WRs[0]
        var2 = WRs[1]
        var3 = WRs[2]
        R = BinaryFR(var1, var2, var3)

    else:
        var1 = WRs[0]
        var2 = WRs[1]
        R = NBinaryFR(var1, var2)
    
    return R
        
def BinaryFR(var1, var2, var3):
    R = False

    if (var1 == 'canWalk') or (var1 == 'walk'):
        if var2 in directions:
            if (var3 in variables) or (type(var3) is int):
                R = True

    elif var1 == 'jumpTo':
        if ((var2 in variables) or (type(var2) is int)) and ((var3 in variables) or (type(var3) is int)):
            R = True

    elif var1 == 'isfacing':
        if var2 in directionsC: 
            if((var3 in variables) or (type(var3) is int)):
                R = True
    
    return R

def NBinaryFR(var1, var2):
    R = True
    if var1 == 'look':
       if var2 not in directionsC:
        R = False
    else:
        if (type(var2) != int) or (not var2 in variables) :
            R= False
    return R


def BODYPR( S1: list ):
    R = True
    PO = False
    i = 1
    n = len(S1)
    while (i < n) and R:
        token = S1[i]

        if (not RL.Isfunction(token)) or (i == n-1 and token != ')' ) or ((token =='(') and PO) \
            or (i != n-1 and token == ')' ) :
            R=False
        
        if (token =='(') and (not PO) :
            PO = True
        
    if not PO :
        R= False

    return R
    
def Expresion(var1, var2, var3,token):
    if token is ':=':
        variables[var1] = var2
    elif token is '+':
        variables[var1] = var2 + var3
    elif token is '-':
        variables[var1] = var2 - var3

# %%
