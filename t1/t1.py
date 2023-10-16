import math
from scipy.optimize import minimize
import numpy as np
from visualization import vis_from_point, hk_Visualization, Visualization
from ballisticsolution import hk_get_angle, get_angle, iteration_get_angle, hk_residual, residual
num1 = 6
num2 = 3
num3 = 5.196152422706632

PI = 3.1415926535
GRAVITY = 9.78
angle = 30
new_angle = math.radians(angle)
v = 16
v_x = v * math.cos(new_angle)
v_y = v * math.sin(new_angle)

s = num3
h = num2
k = 0.092

#################################################################
hk_t1_test, hk_z_actual_test, hk_dz_test = hk_get_angle(s, v, new_angle)
t1_test, z_actual_test, dz_test = get_angle(s, v, new_angle)

print(f"hk_t1_test = {hk_t1_test}, hk_z_actual_test = {hk_z_actual_test}, hk_dz_test = {hk_dz_test}")
print(f"t1_test = {t1_test}, z_actual_test = {z_actual_test}, dz_test = {dz_test}")

print("iter_angle = ", iteration_get_angle(s, h, v) * 180 / PI)


# 使用高斯-牛顿法进行参数拟合
init_params = [new_angle]
# result = minimize(residual, init_params[0], method='BFGS')
hk_result = minimize(lambda params: np.sum(hk_residual(params[0])**2), init_params, method='BFGS')
result = minimize(lambda params: np.sum(residual(params[0])**2), init_params, method='BFGS')

best_params = hk_result.x
min_value = hk_result.fun

# print("", hk_residual(new_angle))
print(f"best_params = {best_params * 180 / PI}")
print(f"min_value = {min_value}")
print(f"e = {hk_residual(best_params)}")

hk_t1_test, hk_z_actual_test, hk_dz_test = hk_get_angle(s, v, best_params)
print(f"hk_t1_test = {hk_t1_test}, hk_z_actual_test = {hk_z_actual_test}, hk_dz_test = {hk_dz_test}")
print(f"angel = {result.x * 180 / PI}")
################################################################

# 可视化
t_ls = []
for i in np.arange(0, 3, 0.01):
    t_ls.append(i)
vis_point = hk_Visualization(v, t_ls, new_angle)
vis_ori_point = Visualization(v, t_ls, result.x)
print("vis_ori_point = ", vis_ori_point)
new_vis_point = hk_Visualization(v, t_ls, best_params)
vis_from_point(h, s, vis_point, new_vis_point, vis_ori_point)