# y = -logx

from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return -np.log(-x)

data_x = np.arange(-2, 2, 0.01)
data_y = f(data_x)

fig, splt = plt.subplots()
plt.axvline(x=0, color='r')
plt.axhline(y=0, color='r')


plt.show()