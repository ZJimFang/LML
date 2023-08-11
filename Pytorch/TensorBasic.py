import torch
import numpy as np

"""
create tensor (Pytorch only know tensor)
"""
# x = torch.rand(4, 4)
# y = torch.rand(4, 4)
# x = torch.zeros(2, 2)
# x = torch.ones(2, 2, dtype=torch.float16)
# x = torch.tensor([2.4, 0.1])

"""
calculate, if doing in-place calculation need add _
"""
# x = torch.rand(4, 4)
# y = torch.rand(4, 4)
# y.add_(x)
# y.sub_(x)
# y.mul_(x)
# z = torch.add(x, y)
# z = torch.sub(x, y)
# z = torch.mul(x, y)
# print(x)

"""
get tensor value
"""
# x = torch.rand(3, 5)
# print(x)
# print(x[:, 0])
# print(x[1, :])
# print(x[1, 1].item())  # get actual value

"""
tensor operate
"""
# x = torch.rand(4, 4)
# y = torch.rand(4, 4)
# y = x.view(16)
# y = x.view(-1, 8)  # auto*8
# print(y.size())

"""
torch -> numpy
"""
# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b, type(b))
# a.add_(1) # if we run in CPU then a and b will run in the same memory place
# print(a)
# print(b)

"""
numpy -> torch
"""
# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)
# a += 1  # if we run in CPU then a and b will run in the same memory place
# print(a)
# print(b)

"""
run in GP（MAC need to use in the other way）
Torch -> tensor -> GPU
Numpy -> array -> CPU
"""
# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     x = torch.ones(5, device=device)
#     y = torch.ones(5)
#     y = y.to(device)
#     z = x+y
#     # z.numpy()  # would be error, numpy can't be used in GPU
#     z = z.to("cpu")
