# import numpy as np
# import pandas as pd
#
# s_data = pd.Series([1, 3, 5, 7, np.NaN, 9, 11])  # pandas中生产序列的函数，类似于我们平时说的数组
# print(s_data)

# import numpy as np
# import pandas as pd
#
# # 以20170220为基点向后生产时间点
# dates = pd.date_range('20170220', periods=6)
# # DataFrame生成函数，行索引为时间点，列索引为ABCD
# data = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(data)
# print(data.shape)
# print(data.values)

# import numpy as np
# import pandas as pd
#
# # 设计一个字典
# d_data = {'A': 1, 'B': pd.Timestamp('20170220'), 'C': range(4), 'D': np.arange(4)}
# print(d_data)
# # 使用字典生成一个DataFrame
# df_data = pd.DataFrame(d_data)
# print(df_data)
# # DataFrame中每一列的类型
# print(df_data.dtypes)
# # 打印A列
# print(df_data.A)
# # 打印B列
# print(df_data.B)
# # B列的类型
# print(type(df_data.B))

# import numpy as np
# import pandas as pd
#
# dates = pd.date_range('20170220', periods=6)
# data = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(data)
# # 输出data
# print(data.A)
# # 输出A列
# print(data['A'])
# # 输出3,4行
# print(data[2:4])
# # 输出3，4行
# print(data['20170222':'20170223'])
# # 输出3,4行
# print(data.loc['20170222':'20170223'])
# # 输出3,4行
# print(data.iloc[2:4])
# # 输出B, C两列
# print(data.loc[:, ['B', 'C']])


# import numpy as np
# import pandas as pd
#
# dates = pd.date_range('20170220', periods=6)
# data = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(data)
# # 输出A列中大于0的行
# print(data[data.A > 0])
# # 输出大于0的数据，小于等于0的用NaN补位
# print(data[data > 0])
# # 拷贝data
# data2 = data.copy()
# print(data2)
# tag = ['a'] * 2 + ['b'] * 2 + ['c'] * 2
# # 在data2中增加TAG列用tag赋值
# data2['TAG'] = tag
# print(data2)
# # 打印TAG列中为a,c的行
# print(data2[data2.TAG.isin(['a', 'c'])])

