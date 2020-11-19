# 수치미분(Numerical Diffirentiation) VS 해석미분(Analytic Diffirentiation) : ** 수치미분을 사용해라 **
import os
import sys
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import numerical_diff
except ImportError:
    print('Library Module Can Not Found')
from matplotlib import pyplot as plt


def f(x):
    return 20*(x-2)**2+500


def analytic_diff(x):
    return 40 * x - 80


print(f'Numerical Diffirentiation Value:{numerical_diff(f, 5)}')
print(f'Analytic Diffirentiation Value:{analytic_diff(5)}')
