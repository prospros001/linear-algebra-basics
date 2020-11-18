# 기울기(gradient)
import sys
import numpy as np
try:
    sys.path.append('D:\deep-learning\PycharmProjects\linear-algebra-basics\lib')
    import common as cm
except ImportError:
    print('Library Module, Can Not Found')


def f(x):
    return np.sum(x**2, axis=0)


# 함수 테스트
# print(f(np.array([3., 4., 5.])))

gra1 = cm.numerical_gradient(f, np.array([3., 4.]))
gra2 = cm.numerical_gradient(f, np.array([0., 2.]))
gra3 = cm.numerical_gradient(f, np.array([3., 0.]))
print(gra1, gra2, gra3)