"""

Author:
    Ilias Bilionis

Date:
    7/25/2013

Revised by @Chuan Lu, 2018-02-08
"""


__all__ = ['lancz']


import numpy as np
from ._orthpol import *


def lancz(x, w, n):
    """The Lanczos procedure for constructing the recurcive formula
    for orthogonal polynomials.

    Wrapper from ORTHPOL.
    """
    if x.dtype == 'float32':
        func = slancz
    else:
        func = dlancz
    alpha, beta, ierr = func(n, x, w)
    assert ierr == 0
    return alpha, beta


if __name__ == '__main__':
    x = np.linspace(0., 1, 100)
    w = np.ones(100)
    print(x, w)
    alpha, beta = lancz(x, w, 10)
    print(alpha)
    print(beta)
