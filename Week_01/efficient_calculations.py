# -*- coding: utf-8 -*-
"""
@author: Alex Muirhead
"""

import numpy as np


def fact(n):
    """Calculate the value of n factorial."""
    # n! = n*(n-1)*...*2*1
    product = 1
    for i in range(1, n+1):
        product *= i
    return product


def exptaylor(n, x):
    """Taylor series expansion of e^x

    NOTE:
        This will fail with x as a np.ndarray when
        n > 21, due to a quirk with division by
        large numbers (21! = 51090942171709440000).
        Just another reason to avoid this implemenation!
    """
    output = 0
    for i in range(n):
        output += x**i / fact(i)
    return output


def better_exptaylor(n, x):
    """
    Better Taylor series expansion of e^x

    term 0: 1
    term 1: x**1 / 1! == (term 0) * x
    term 2: x**2 / 2! == (term 1) * x / 2
    term 3: x**3 / 3! == (term 2) * x / 3
    """
    term = 1
    output = term
    for i in range(1, n):
        term   *= x / i
        output += term
    return output


def lntaylor(n, x):
    """
    Efficient Taylor series expansion of ln(x+1) at x=1

    term 0: -1 {not included}
    term 1:   (x-1)**1 / (2**1 * 1)
    term 2: - (x-1)**2 / (2**2 * 2)
    term 3:   (x-1)**3 / (2**3 * 3)
    term 4: - (x-1)**4 / (2**4 * 4)
    """
    term = -1
    output = np.log(2.)  # <- 0th term
    for i in range(1, n):
        term *= (1-x) / 2
        output += term / i
    return output
