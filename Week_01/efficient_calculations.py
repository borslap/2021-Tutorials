# -*- coding: utf-8 -*-
"""
@author: Alex Muirhead
"""

import numpy as np


def fact(n):
    """Calculate the value of n factorial.""" 
    # 4! = 4*3*2*1
    product = 1
    for i in range(1, n+1):
        product *= i
    return product


def exptaylor(n, x):
    """Taylor series expansion of e^x """
    output = np.zeros_like(x)
    for i in range(n):
        output += x**i / fact(i)
    return output

    # output = 
    #   x / 1
    # + (x)*x / (1*2)
    # + (x*x)*x / (1*2*3)
    
def better_exptaylor(n, x):
    """Better Taylor series expansion of e^x """
    term = 1
    output = term
    for i in range(1, n):
        term   *= x / i
        output += term
    return output
