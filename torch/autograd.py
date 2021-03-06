#!/bin/env python
#coding:utf-8

"""
autograd.Variable
    data
    grad
    creator: references a Function otherwise None
autograd.Function
"""

from __future__ import print_function
import torch
from torch.autograd import Variable

x = Variable(torch.ones(2,2), requires_grad=True)
print(x)

y = x + 2
print(y)
print(x.creator)
print(y.creator)

z = y * y * 3
out = z.mean()
print(z, out)

out.backward()
print(x.grad)
