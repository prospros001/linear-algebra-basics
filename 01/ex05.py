import numpy as np

m = np.array([[10, 20],
              [1, 2]])

'''
 1. 2차원 배열 즉, 행렬의 축 기준 연산(합)
 2. 축이 두개 이기때문에 축 지정 유무에 상관없이 결과가 같다.
'''
print(m)

s1 = np.sum(m)
print(s1, type(s1))

s2 = np.sum(m, axis=0)
print(s2, type(s2))

s3 = np.sum(m, axis=1)
print(s3, type(s3))
