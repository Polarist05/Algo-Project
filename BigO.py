import numpy as np
def Logn(x, a, b):
    return a * np.log2(x) + b

def Linear(x, a, b):
    return a * x + b

def NlogN(x, a, b):
    return a * x * np.log2(x) + b

def Square(x, a, b):
    return a * x*x  + b

def N2logN(x,a,b):
    return a*x*x*np.log2(x) + b

def Cube(x,a,b):
    return a*x*x*x + b
