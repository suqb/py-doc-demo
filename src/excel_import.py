import csv

import pandas as pd

# 读取excel pd.read_excel('path')
# 读取excel 指定工作表 pd.read_excel('path', sheet_name='SheetName')
# 读取excel 指定表头行，默认第一行header=0，没有则指定为None pd.read_excel('path', header=None)
# 读取excel 设置表头 book.columns = ['姓名', '年龄', '性别'] book.set_index('姓名', inplace=True)
# 读取excel 不指定索引列会从除了表头开始默认0增加，可以指定pd.read_excel('path'， index_col='姓名') 那么索引会从'姓名'0开始算
# 读取excel 并指定数据类型 pd.read_excel(path, dtype={'姓名': str, '年龄': int, '性别': 'str'})
# 读取excel 并且跳过表头前面的空行 pd.read_excel(path, skiprows=1)
# book = pd.read_excel(path, sheet_name='alias', usecols=[1], header=None, names=['main_sku', 'alias_sku_join'])
# df = pd.read_excel(path, sheet_name='alias', usecols=[1], header=None)


def calc_intersection_sku():
    print('------------------')
    order_sku = read_order_sku()
    alias_sku = read_alias_sku()

    # print(list(set(order_sku).intersection(alias_sku)))
    print(list(set(order_sku) & set(alias_sku)))


def read_order_sku():
    platform_sku_excel = r'C:/Users/wumingjie/Desktop/出单的平台SKU.xlsx'

    df = pd.read_excel(platform_sku_excel, sheet_name='Result 1', header=0)

    order_platform_sku_list = df.iloc[:, 0].tolist()

    # return [sku for sku in order_platform_sku_list if sku is not None]
    return list(filter(lambda sku: sku is not None, order_platform_sku_list))


def read_alias_sku():
    alias_sku_excel = r'C:/Users/wumingjie/Desktop/别名映射.xlsx'

    df = pd.read_excel(alias_sku_excel, sheet_name='Result 1', header=0)

    alias_sku_list = df.iloc[:, 0].tolist()

    return [sku for sku in alias_sku_list if sku is not None and len(sku.strip()) != 0 and sku != 'null']


# calc_intersection_sku()


sku_list = ['HQJ90822573RD', 'WUJ240622001GY', 'LZP200521142WE', 'YHP230412013PP', 'LSI210707948RD', 'CXB230224002RD2', 'XYM71107904WH', 'LZX80813736', 'YHP230412013GN', 'CXB230224002BK', 'CXB230224002BU2', 'XYM71107904PK', 'YHP230412013WE', 'PCD240409006BG42', 'CXB230713011BGL', 'CXB230224002PK', 'LAE230417007', 'CXB230224002BU1', 'HCJ211122013BKS', 'CXB230713011BGXL', 'FJC211103811B', 'PCD220112281BW39', 'YHP230412013WH', 'HZH81122056PK', 'YHP230412013RD', 'YHP230412013BK', 'CXB230224002RD1', 'XUY80904801BKL2', 'LNP80328368XL', 'XUY80904801BKXL', 'HCJ211119017BUS']

sku_join = ''

for sku in sku_list:
    sku_join = sku_join + ',' + sku

print(sku_join)
print(len(sku_list))
