# 평균제곱오차 테스트

import os
import sys
from pathlib import Path
import numpy as np
try:
    sys.path.append('D:\deep-learning\PycharmProjects\linear-algebra-basics\lib')
    from common import mean_squarea_error, method_least_squares
except ImportError:
    print('Library Module Can Not Found')

# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

a, b = method_least_squares(times, scores)
print(f'직선 y= {a}x + {b}')

print(f'오차(평균제곱오차): {mean_squarea_error(np.array([a, b]), times, scores)}')