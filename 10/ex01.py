# 최소제곱법 (Method of Least Squares) 테스트
from matplotlib import pyplot as plt
import numpy as np
import math

# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

def mls(x, y):
    mx = sum(x)/len(x)
    my = sum(y)/len(y)

    s1 = 0
    for i in range(len(x)):
        s1 += (x[i] - mx) * (y[i] - my)

    s2 = 0
    for i in range(len(x)):
        s2 += (x[i] - mx)**2

    mls_a = s1 / s2
    mls_b = my - (mx * mls_a)

    return mls_a, mls_b

a, b = mls(times, scores)
print(f'직선 y= {a}x + {b}')


# predict
scores_predict = [(a * t) + b for t in times]
print(scores_predict)

# 그래프
fig, splt = plt.subplots()
splt.scatter(times, scores)
splt.plot(times, scores_predict)


plt.show()