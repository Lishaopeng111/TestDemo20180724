# -*- coding: utf-8 -*-
# @Time    : 2018/9/7 10:48
# @Author  : Lsp

a = [[1, 2], 3, 4]
print(a)
print(id(a[0][1]))
b = a.copy()
b[0][1] = 5
print(a)
print(b)
print(id(b[0][1]))
