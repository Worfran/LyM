#%%
from contextvars import Token
from typing import List
import nltk
import numpy
import Rules as RL

#path
file = 'C:/Users/frawo/Documents/Programacion/LyM/Data/Prueba0.py'
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
    for line in matrix:
        pass
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
    
    if RL.Isbinary: 
        None

    else:

def BinaryFR(S1: list):
    None

def NBinaryFR(S1: list):


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
    
    
# %%
