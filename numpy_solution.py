import numpy as np

a  = np.array([[1, 2], [3, 4]])  # 初始化一个非奇异矩阵(数组)
print(np.linalg.inv(a))  # 对应于MATLAB中 inv() 函数

# 矩阵对象可以通过 .I 更方便的求逆
A = np.matrix(a)
print(A.I)

def revert(a:np.array):
    """
    逆矩阵
    :param a: 输入矩阵
    :return: 逆矩阵
    """
    return a.I

def convert(a:np.array):
    """
    转置矩阵
    :param a: 输入矩阵
    :return: 转置矩阵
    """
    return a.T