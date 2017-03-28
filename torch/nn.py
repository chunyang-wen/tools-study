#!/bin/env python
#coding:utf-8

"""
Neural networks: torch.nn, 依赖于 autograd

nn.Module: layer description
forward(input): returns output
torch.optim: ways to update weights or parameters
"""

"""
Questions:
    what is a view ?
    what is batch dimension ?
"""

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input channel, 6 output channels, 5*5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1   = nn.Linear(16*5*5, 120) # an offline operation: y = Wx + b
        self.fc2   = nn.Linear(120, 84)
        self.fc3   = nn.Linear(84, 10)

    # override ?
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:] # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

net = Net()
print(net)

params = list(net.parameters())
print(len(params))
print(params[0].size())

# feed input: autograd.Variable
# Conv2d consumes 4-D Tensor: nSamples * nChannels * Height * Width
input = Variable(torch.randn(1, 1, 32 ,32))
output = net(input)
print(output)

# backward
net.zero_grad()
#output.backward(torch.randn(1, 10)) # 10 is output size
net.zero_grad()

# loss function
target = Variable(torch.range(1, 10))
criterion = nn.MSELoss()
loss = criterion(output, target)
print("Loss is: %s" % loss.data)
print(loss.creator)

# backward
net.zero_grad()
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)
loss.backward()
print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

# update the weights
learning_rate = 0.01
for f in net.paremeters():
    f.data.sub_(f.grad.data * learning_rate)

# use torch.optim to update weights
"""
import torch.optim as optim
# create your optimizer
optimizer = optim.SGD(net.parameters(), lr=0.01)
# in your training Loop:
optimizer.zero_grad()
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()
"""
