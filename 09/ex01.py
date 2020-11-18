
import os
import sys
from pathlib import Path
import numpy as np
try:
    sys.path.append('D:\deep-learning\PycharmProjects\linear-algebra-basics\lib')
    from common import method_least_squares
except ImportError:
    print('Library Module Can Not Found')


def f(x):
    return np.sum(x**2, axis=0)

method_least_squares(f, np.array([-3., 4.]), lr=0.1)
# gradient_descent(f, np.array([-3., 4.]), lr=100)
# gradient_descent(f, np.array([-3., 4.]), lr=0.001, epoch=10000)