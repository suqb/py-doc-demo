import pandas as pd

# 可以代表行也可以代表列，作为行时name则为每行的序号， index作为表头， 最为列时index则代表每行的序号，name作为表头
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='s')

print(s)


index = ['姓名', '年龄', '性别', '手机号', '籍贯']
s1 = pd.Series(['zhangsan', 21, '男', '13004510401', '广东省'], index=index, name=None)
s2 = pd.Series(['zhangsan', 21, '男', '13004510401', '广东省'], index=index, name=None)
s3 = pd.Series(['zhangsan', 21, '男', '13004510401', '广东省'], index=index, name=None)

# series作为行时则接受list：[series1, series2, series3], series作为列时接受字典{'表头名称1'：series1, '表头名称2'：series2, '表头名称3'：series3}
df = pd.DataFrame([s1, s2, s3])

print(df)
