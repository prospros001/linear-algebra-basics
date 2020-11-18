# 기울기(gradient)

import numpy as np

def f(x):
    return np.sum(x**2, axis=0)

def numerical_gradient(f, x):
    h = 1.0e-4
    gradient = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        h1 = f(x)

        x[i] = tmp - h
        h2 = f(x)

        gradient[i] = (h1 - h2) / (2 * h)
        x[i] = tmp

    return gradient


# 함수 테스트
# print(f(np.array([3., 4., 5.])))

gra1 = numerical_gradient(f, np.array([3., 4.]))
gra2 = numerical_gradient(f, np.array([0., 2.]))
gra3 = numerical_gradient(f, np.array([3., 0.]))
print(gra1, gra2, gra3)