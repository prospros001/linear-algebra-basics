# 전치행렬

import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

a1 = a.T
print(a1)

a2 = np.transpose(a)
print(a2)

a3 = np.swapaxes(a, 0, 1)
print(a3)