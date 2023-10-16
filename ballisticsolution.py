import math

h = 3
GRAVITY = 9.78
k = 0.092
s = 5.196152422706632
v = 16
PI = 3.1415926535

# 华科，可得到t，z_actual, dz
def hk_get_angle(s, v, angle):
    hk_t1 = s / (v * math.cos(angle))
    # hk_z_actual = v_y * hk_t1 - GRAVITY * hk_t1 * hk_t1 / 2
    hk_z_actual = s * math.tan(angle) - GRAVITY * math.pow(s / (v * math.cos(angle)), 2) / 2
    hk_dz = h - hk_z_actual
    return hk_t1, hk_z_actual, hk_dz

# 可得到t，z_actual, dz
def get_angle(s, v, angle):
    t1 = (float)((math.exp(k * s) - 1) / (k * v * math.cos(angle)))
    z_actual = (float)(v * math.sin(angle) * t1 - GRAVITY * t1 * t1 / 2)
    dz = h - z_actual
    return t1, z_actual, dz

# 迭代，优化角度
def iteration_get_angle(s, z, v):
    z_temp = z

    for i in range(100):
        angle_pitch = math.atan2(z_temp, s)
        z_actual = get_angle(s, v, angle_pitch)[1]
        dz = 0.3 *(z - z_actual)
        z_temp = z_temp + dz
        print(f"num = {i}, angle_pitch = {angle_pitch * 180 / PI}, dz = {dz}, z_temp = {z_temp}, z_actual = {z_actual}")
        if abs(dz) < 0.0000001:
            break

    print(f"angle = {angle_pitch * 180 / PI}")
    return angle_pitch

# 华科公式的高斯牛顿残差公式
def hk_residual(angle):
    # 计算误差 e 的平方和
    e = h - (s * math.tan(angle) - 0.5 * GRAVITY * (s / (v * math.cos(angle)))**2)
    # e = h - (s * math.tan(angle) - GRAVITY * math.pow(s / (v * math.cos(angle)), 2) / 2)
    return e

# 高斯牛顿残差公式
def residual(angle):
    t1 = (float)((math.exp(k * s) - 1) / (k * v * math.cos(angle)))
    z_actual = (float)(v * math.sin(angle) * t1 - GRAVITY * t1 * t1 / 2)
    dz = h - z_actual
    return dz
