import pandas as pd

path = r'../index.xlsx'

# 读取excel pd.read_excel('path')
# 读取excel 指定工作表 pd.read_excel('path', sheet_name='SheetName')
# 读取excel 指定表头行，默认第一行header=0，没有则指定为None pd.read_excel('path', header=None)
# 读取excel 设置表头 book.columns = ['姓名', '年龄', '性别'] book.set_index('姓名', inplace=True)
# 读取excel 不指定索引列会从除了表头开始默认0增加，可以指定pd.read_excel('path'， index_col='姓名') 那么索引会从'姓名'0开始算
# 读取excel 并指定数据类型 pd.read_excel(path, dtype={'姓名': str, '年龄': int, '性别': 'str'})
# 读取excel 并且跳过表头前面的空行 pd.read_excel(path, skiprows=1)
book = pd.read_excel(path, usecols=1)
print(book)

