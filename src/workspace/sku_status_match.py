import pandas as pd

match_sku_excel = r'C:/Users/wumingjie/Desktop/部分下架历史销量30以内90天销量0 清理下架.xlsx'

df = pd.read_excel(match_sku_excel, sheet_name='需匹配')
