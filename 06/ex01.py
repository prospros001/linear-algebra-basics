# 수치미분 (Numerical Diffirention)
# 이차함수 y = 20(x-2)^2 +500

import numpy as np

def f(x):
    return  20*(x-2)**2+500


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x)) / h

print(f'Diffirention Value:{numerical_diff(f, 5)}')
print(f'Diffirention Value:{numerical_diff(f, 6)}')