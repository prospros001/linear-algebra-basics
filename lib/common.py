import numpy as np


# 수치미분으로 기울기 구하기
def numerical_gradient(f, x):
    h = 1e-4
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


# 수치미분으로 기울기 구하기
def numerical_gradient_training(f, x, data_training):
    h = 1e-4
    gradient = np.zeros_like(x)

    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        h1 = f(x, *data_training)
        x[i] = tmp - h
        h2 = f(x, *data_training)
        gradient[i] = (h1 - h2) / (2 * h)

        x[i] = tmp

    return gradient


# 경사하강법 구현1
def gradient_descent(f, x, lr=0.01, epoch=100):
    for i in range(epoch):
        gradient = numerical_gradient(f, x)
        # 출력
        print(f'epoch={i+1}, gradient={gradient}, x={x}')
        x -= lr * gradient

    return x


# 경사하강법 구현2 - 선형회귀
def gradient_descent_linear_regression(f, x, lr=0.01, epoch=100, data_training=None):
    for i in range(epoch):
        gradient = numerical_gradient_training(f, x, data_training)
        # 출력
        print(f'epoch={i+1}, gradient={gradient}, x={x}')
        x -= lr * gradient

    return x


# 최소제곱법
# 여러 점에서 직선의 기울기 구하기
def method_least_squares(x, y):
    mx = sum(x)/len(x)
    my = sum(y)/len(y)

    # s1 = 0
    # for i in range(len(x)):
    #     s1 += (x[i] - mx) * (y[i] - my)
    s1 = sum([(i - mx)*(j - my) for i, j in zip(x, y)])

    # s2 = 0
    # for i in range(len(x)):
    #     s2 += (x[i] - mx)**2
    s2 = sum([(i-mx)**2 for i in x])

    mls_a = s1 / s2
    mls_b = my - (mx * mls_a)

    return mls_a, mls_b


# 평균제곱오차(MSE, Mean Squares Error)
def mean_squares_error(x, data_x, data_y):

    # s = 0
    # for i in range(len(data_x)):
    #     data_y_hat = x[0] * data_x[i] + x[1]
    #     s += ((data_y_hat - data_y[i]) ** 2)
    # e = s / len(data_x)

    data_y_hat = [x[0] * dx + x[1] for dx in data_x]
    e = np.mean([(dyh - dy)**2 for dyh, dy in zip(data_y_hat, data_y)])

    return e