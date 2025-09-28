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
# y = torch.rand(5, 3)
# print(y)


#张量的加法
# x = torch.rand(5, 3)
# y = torch.rand(5, 3)
# print(x+y)
# print(torch.add(x, y))
# z= torch.empty(5,3)
# torch.add(x, y, out=z)
# print(z)

#张量的切片
# print(x[:, 1])

# print(x[:,0])


#张量的形状改变
# x = torch.randn(4, 4)
# y = x.view(-1,16)
# print(y)
# print(y[0,0].item())


# 切片操作 [0:-1] 的含义
# 切片操作 [0:-1] 是Python中用于从序列（如列表、字符串或元组）中提取子序列的一种方式。具体来说，切片操作 [0:-1] 的含义如下：
# 1. 起始索引（start index）：0 表示从序列的第一个元素开始（索引从0开始）。
# 2. 结束索引（end index）：-1 表示到序列的倒数第二个元素结束（不包括索引为-1的元素，即最后一个元素）。
# 因此，切片操作 [0:-1] 会返回从序列的第一个元素到倒数第二个元素的所有元素，形成一个新的子序列。
# 示例：
# my_list = [10, 20, 30, 40, 50]
# sub_list = my_list[0:-1]
# print(sub_list)  # 输出: [10, 20, 30, 40]
# 在这个例子中，sub_list 包含了 my_list 的前四个元素（索引0到3），而不包括最后一个元素（索引4）。
# 详细解释
# my_list = [10, 20, 30, 40, 50]
# sub_list = my_list[-4:-2]
# print(sub_list)


# torch to numpy
# a= torch.ones(5,5)
# print(a)

# b=a.numpy()

# a.add_(1)
# print(a)
# print("numpy\r\n", b)

# numpy to torch
# a= np.ones(10)
# print(a)

# b = torch.from_numpy(a)
# np.add(a, 1, out=a)

# print(b)

# x = torch.rand(9,9)
# if torch.cuda.is_available():
#     #将处理设备定义为GPU
#     device = torch.device("cude")
#     y=torch.ones_like(x, device=device)
#     #将x转移到gpu上
#     x = x.to(device)
#     z= x+y
#     print(z)
#     print(z.to("cpu", torch.double))

print(torch.__version__)
if torch.cuda.is_available():
    print("cuda is available")
else:
    print("cuda is not available")