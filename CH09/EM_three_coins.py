# 三硬币模型（例9.1）
import numpy as np
from sympy import *

# 观测值
y = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1])

# 三个事件均服从0-1分布
# 参数初值
pi = 0.4
p = 0.6
q = 0.7

# Q函数中参数
pi_v = symbols('pi_v')
p_v = symbols('p_v')
q_v = symbols('q_v')

# 迭代步数
ite_num = 5

# 开始迭代
for ite_i in range(ite_num):
    Q = 0
    # E步 对隐含变量可能出现的各种情况求期望
    for j in range(len(y)):
        # 选择是硬币B的概率
        miu_B = (pi * (p ** y[j]) * ((1-p) ** (1 - y[j])))/((pi * (p ** y[j]) * ((1-p) ** (1 - y[j]))) + ((1 - pi) * (q ** y[j]) * ((1-q) ** (1 - y[j]))))
        # 选择是硬币C的概率
        miu_C = 1 - miu_B
        # 第j次实验Q函数
        Q_j = miu_B * log(pi_v * (p_v ** y[j]) * ((1-p_v) ** (1 - y[j]))) + miu_C * log((1 - pi_v) * (q_v ** y[j]) * ((1-q_v) ** (1 - y[j])))
        # 公式9.11
        Q = Q + Q_j
    # print(Q)
    # M步 找到使Q函数最大化的参数
    [(pi, p, q)] = solve([diff(Q, pi_v), diff(Q, p_v), diff(Q, q_v)], [pi_v, p_v, q_v])
    print('当前迭代次数:', ite_i + 1)
    print('迭代参数结果：pi =', pi, 'p =', p, 'q =', q)
