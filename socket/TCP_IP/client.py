# -*- coding: utf-8 -*-
# @Time    : 2018/7/26 16:26
# @Author  : Lsp

i = 1
while i <= 78:
#打印空格
    j = 1
    while j <= 78-i:
        print(' ', end="")
        j += 1
#打印"*"
    a = 1
    while a <= 2*i-1:
        print('*', end="")
        a += 1
    print('')
    i += 1