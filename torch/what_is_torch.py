#!/bin/env python
#coding:utf-8

from __future__ import print_function

import torch
import numpy as np


x = torch.randn(5, 3)
print(x)
print(x.size())

y = torch.Tensor(5, 3)
print(y)
print(y.size())


print(x + y)

print(torch.add(x, y))

x = torch.ones(5)
y = x.numpy()
print(x)
print(y)
x.add_(1)
print(x)

x = np.ones(1)
y = torch.from_numpy(x)

"""
# move to cuda
if torch.cuda.is_avaiable():
    x = x.cuda()
    y = y.cuda()
"""
