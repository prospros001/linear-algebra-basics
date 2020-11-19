# 편미분(Partial Diffirentiation) : x0, x1에 대해 미분
import os
import sys
from pathlib import Path

import numpy as np

try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import numerical_partial_diff
except ImportError:
    print('Library Module Can Not Found')

def f(x):
    return x[0]**2 + x[1]**2

# (x0, x1) = (2, 4)
print(f'Numerical Partial Diffierentiation Value:{numerical_partial_diff(f, np.array([2., 4.]))}')

# (x0, x1) = (3, 1)
print(f'Numerical Partial Diffierentiation Value:{numerical_partial_diff(f, np.array([3., 1.]))}')

# (x0, x1) = (8, 2)
print(f'Numerical Partial Diffierentiation Value:{numerical_partial_diff(f, np.array([8., 2.]))}')




