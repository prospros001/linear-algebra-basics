# 경사하강법(수치미분)
import os
import sys
from pathlib import Path
import numpy as np
try:
    sys.path.append('D:\deep-learning\PycharmProjects\linear-algebra-basics\lib')
    from common import mean_squarea_error, method_least_squares, gradient_descent_linear_regression
except ImportError:
    print('Library Module Can Not Found')

# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

# 경사하강법
result = gradient_descent_linear_regression(mean_squarea_error, np.array([0., 0.]), epoch=1000, data_training=(times, scores))

print(result)