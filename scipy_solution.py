import scipy.spatial as spt
import numpy as np

def find_point_in_circle(point):
    """
    找到圆内的点
    :param point: 输入点
    :return: 圆内的点的index
    """
    ckt = spt.cKDTree(point)  # 用C写的查找类，执行速度更快
    find_point = point[16]  # 原点
    index = ckt.query_ball_point(x=find_point, r=20)  # 返回最近邻点在数组中的index(极其优雅的写法)
    return index

def find_point_with_given_distence(point):
    """
    
    """
    ckt = spt.cKDTree(point)  # 用C写的查找类，执行速度更快
    ckt.query_ball_tree()