# 경사하강법(수치미분)
import os
import sys
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import mean_squares_error, gradient_descent
except ImportError:
    print('Library Module Can Not Found')
import numpy as np


# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

# 경사하강법
result = gradient_descent(mean_squares_error, np.array([0., 0.]), epoch=5000, data_training=(times, scores))
print(f'직선 y = {result[0]}x + {result[1]}')

# 평균제곱오차
print(f'오차(평균제곱오차):{mean_squares_error(np.array(result), (times, scores))}')
