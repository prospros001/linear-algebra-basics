# 편미분(Partial Diffirentiation)
# y = x0**2 + x1**2
import os
import sys
from pathlib import Path

import numpy as np

try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import numerical_diff
except ImportError:
    print('Library Module Can Not Found')

def f(x0):
    return x0**2 + 4**2



def analytic_diff(x0):
    return 2 * x0


# (x0, x1) = (3, 4)
print(f'Numerical Partial Diffierentiation Value:{numerical_diff(f, 3)}')
print(f'Analytic Partial Diffierentiation Value:{analytic_diff(3)}')

# (x0, x1) = (1, 4)
print(f'Numerical Partial Diffierentiation Value:{numerical_diff(f, 1)}')
print(f'Analytic Partial Diffierentiation Value:{analytic_diff(1)}')

# (x0, x1) = (2, 4)
print(f'Numerical Partial Diffierentiation Value:{numerical_diff(f, 2)}')
print(f'Analytic Partial Diffierentiation Value:{analytic_diff(2)}')
