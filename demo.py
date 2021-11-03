#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:lei
@file:demo.py
@time:2021/11/03
@邮箱：leigang431@163.com
"""
import numpy as np
import torch
from matplotlib import pyplot as plt
# % matplotlib online

def verify():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # Assuming that we are on a CUDA machine, this should print a CUDA device:
    print(device)


def task1():
    c = np.ones((3, 3))
    d = torch.from_numpy(c)
    print(c)
    print(d)

# task1()

def task2():
    x = torch.linspace(0, 100, 10001)
    noise = torch.randn(1)
    #  y = 10x+1
    y_true = 10 * x + 1 + noise
    # 通过模型计算y_predict
    w = torch.rand([1, 1], requires_grad=True)
    b = torch.tensor(1, requires_grad=True, dtype=torch.float32)
    # 设置学习率
    learing_rate = 1e-6
    # 通过循环，反向传播，更新参数
    for i in range(800):
        # 计算loss
        y_pred = w * x + b
        loss = (y_pred - y_true).pow(2).mean()
        if w.grad is not None:
            w.grad.data.zero_()
        if b.grad is not None:
            b.grad.data.zero_()
        loss.backward()  # 反向传播
        with torch.no_grad():
            w.data = w.data - learing_rate * w.grad.data
            b.data = b.data - learing_rate * b.grad.data
            w.grad=None
            b.grad=None
        if i % 50 == 0:
            print("w, b, loss", w.item(), b.item(), loss.item())

    print(f'Result: y = {w.item()} x + {b.item()}')
    # plt.figure(figsize=(20, 8))
    # plt.scatter(x, y_true, c='r')
    # y_pred = w * x + b
    # plt.plot(x.numpy().reshape(-1), y_pred.detach().numpy().reshape(-1))
    # plt.show()

def task3():
    # 使用numpy定义全连接层
    class Liner():
        def __init__(self, in_features, out_features, bias=0):
            self.in_features = in_features
            self.out_features = out_features
            self.weight = np.zeros((in_features, out_features))
            self.bias = np.zeros((in_features, out_features))

        def forward(self, x):
            return np.dot(x, self.weight.T) + self.bias

    # 使用pytorch的全连接层
    m = torch.nn.Linear(20, 30)
    input = torch.randn(128, 20)
    output = m(input)
    print(output.size())


def task4():
    # https://pytorch.org/docs/stable/nn.html#non-linear-activations-weighted-sum-nonlinearity
    # https://pytorch.org/docs/stable/generated/torch.nn.ELU.html#torch.nn.ELU
    m = torch.nn.ELU()
    input = torch.randn(2)
    output = m(input)
    print(output)


def main():
    # verify()
    # task1()
    # task2()
    # task3()
    task4()

if __name__ == '__main__':
    main()
