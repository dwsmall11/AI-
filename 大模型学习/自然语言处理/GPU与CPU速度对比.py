import torch
import time

# CPU
start = time.time()
a = torch.ones(10000, 10000)
b = torch.ones(10000, 10000)   
c= torch.matmul(a, b)
end = time.time()
print("CPU计算时间：", end - start)

#GPU
# if torch.cuda.is_available():
#     start = time.time()
#     device = torch.device("cuda")
#     a = torch.rand(10000, 10000).to(device)
#     b = torch.rand(10000, 10000).to(device) 
#     c= torch.matmul(a, b)
#     end = time.time()
#     print("GPU计算时间：", end - start)     

if torch.cuda.is_available():
    start = time.time()
    a = torch.ones(10000, 10000).cuda()
    b = torch.ones(10000, 10000).cuda()   
    c= torch.matmul(a, b)
    end = time.time()
    print("GPU计算时间：", end - start)    