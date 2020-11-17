# 항등 행렬
# 단위행렬의 다른 이름이다.

import numpy as np

m1 = np.identity(3)
print(m1)

v = np.arange(1, 10)
print(v)
m2 = v.reshape(3, 3)
print(m2)

# 단위행렬(항등행렬)과의 닷연산(@) 결과는 그대로 이다.
m3 = np.dot(m2, m1)
print(m3)

