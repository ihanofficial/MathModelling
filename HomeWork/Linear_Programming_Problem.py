import numpy as np
from scipy.optimize import linprog

# 目标函数系数（取负以将最大化问题转化为最小化问题）
c = np.array([-3, 1, 1])
# 不等式约束矩阵A和向量b
A = np.array([[1, -2, 1], [4, -1, -2]])
b = np.array([11, -3])
# 等式约束矩阵Aeq和向量beq
Aeq = np.array([[-2, 0, 1]])
beq = np.array([1])
# 变量边界
bounds = [(0, None), (0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=bounds)

if result.success:
    print("最优解：", result.x)
    print("目标函数最大值：", -result.fun)
else:
    print("求解失败")
