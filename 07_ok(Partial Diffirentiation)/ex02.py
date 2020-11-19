# 편미분(Partial Diffirentiation)
import os
import sys
from pathlib import Path

import numpy as np

try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import numerical_diff
except ImportError:
    print('Library Module Can Not Found')

def f(x1):
    return 3.**2 + x1**2


def analytic_diff(x1):
    return 2 * x1


# (x0, x1) = (3, 4)
print(f'Numerical Partial Diffierentiation Value:{numerical_diff(f, 4.)}')


# (x0, x1) = (3, 1)
print(f'Numerical Partial Diffierentiation Value:{numerical_diff(f, 1.)}')


# (x0, x1) = (3, 2)
print(f'Numerical Partial Diffierentiation Value:{numerical_diff(f, 2.)}')
