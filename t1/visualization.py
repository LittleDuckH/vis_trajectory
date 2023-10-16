import numpy as np
import matplotlib.pyplot as plt
import math
GRAVITY = 9.78
k = 0.092
e = 2.71828

def Visualization(v, t_ls, angle):
    point = []
    for t in t_ls:
        vis_x = (1 / k) * math.log(k * v * math.cos(angle) * t + 1)
        vis_y = v * math.sin(angle) * t - 0.5 * GRAVITY * t * t
        point.append([vis_x, vis_y])
    return point

def hk_Visualization(v, t_ls, angle):
    point = []
    for t in t_ls:
        vis_x = v * math.cos(angle) * t
        vis_y = v * math.sin(angle) * t - 0.5 * GRAVITY * t * t
        point.append([vis_x, vis_y])
    return point

def vis_from_point(h, s, point, new_point, ori_point):
    x = [point_x[0] for point_x in point]
    y = [point_y[1] for point_y in point]
    new_x = [new_point_x[0] for new_point_x in new_point]
    new_y = [new_point_y[1] for new_point_y in new_point]
    ori_x = [ori_point_x[0] for ori_point_x in ori_point]
    ori_y = [ori_point_y[1] for ori_point_y in ori_point]
    
    # 创建一个散点图
    plt.plot(x, y, label='trajectory', color='blue', linestyle='--', linewidth=1)
    plt.plot(new_x, new_y, label='hk_iter_trajectory', color='pink', linestyle='--', linewidth=1)
    plt.plot(ori_x, ori_y, label='ori_iter_trajectory', color='cyan', linestyle='--', linewidth=1)

    # 设置x轴的属性
    plt.axhline(y=0, color='red', linestyle='-', linewidth=1, label='Horizontal Line at y=0')

    
    # 设置水平轴的属性
    plt.axhline(y=h, color='green', linestyle='--', linewidth=1, label='goal_y')
    # 设置垂直轴的属性
    plt.axvline(x=s, color='green', linestyle='--', linewidth=1, label='goal_x')

    # 添加标签和标题
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Sample Data Visualization')

    # 添加图例
    plt.legend()

    # 显示图形
    plt.show()
