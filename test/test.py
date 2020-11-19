from inspect import signature
import os
import sys
import numpy as np


def numerical_gradient(f, x, data_training=None):
    h = 1e-4
    dx = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]
        x[i] = tmp + h
        h1 = f(x) if len(signature(f).parameters) == 1 else f(x, data_training)
        x[i] = tmp - h
        h2 = f(x) if len(signature(f).parameters) == 1 else f(x, data_training)

        dx[i] = (h1 - h2) / (2 * h)

        x[i] = tmp
    return dx


def gradient_descent(f, x, lr=0.01, epoch=100, data_training=None):
    for i in range(epoch):
        gradient = numerical_gradient(f, x, data_training)

        print(f'epoch = {i + 1}, gradient = {gradient}, x = {x}')
        x += lr * gradient
    return x


def mean_squares_error(x, data_training):
    data_x, data_y = data_training

    s = 0
    for i in range(len(data_x)):
        data_y_hat = x[0] + data_x[i] + x[1]
        s += ((data_y_hat - data_y[i]) ** 2)
    e = s / len(data_x)
    return e


# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

# 경사하강법
result = gradient_descent(mean_squares_error, np.array([0., 0.]), epoch=5000, data_training=(times, scores))
print(f'직선 y = {result[0]}x + {result[1]}')

# 평균제곱오차
print(f'오차(평균제곱오차) : {mean_squares_error(np.array(result), (times, scores))}')
