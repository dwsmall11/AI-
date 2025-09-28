# 兼容python2和python3
from __future__ import print_function
print("love Python")
print("love pytorch")

# 导入pytorch和numpy包
import torch
import numpy as np

# 创建一个5行3列的未初始化矩阵
# x = torch.empty(5, 3)
# print(x)

#
y = torch.rand(5, 3)
print(y)