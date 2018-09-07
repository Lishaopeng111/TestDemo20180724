# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 17:47
# @Author  : Lsp

import pandas as pd

index = pd.Index(data=['tom', 'bob', 'mary', 'james'], name='name')
data = {'age': [18, 30, 25, 40],
        'city': ['beijing', 'shanghai', 'guangzhou', 'shenzhen']
        }

user_info = pd.DataFrame(data=data, index=index)
user_info['sex'] = 'male'
user_info.pop('sex')
user_info.assign(age_add_one=user_info['age'] + 1)
print(user_info)
