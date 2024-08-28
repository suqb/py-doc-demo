import pandas as pd
import yaml

with open('../config.yml', 'r', encoding='utf-8') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

is_row = data['setting']['is_row']

index = {1: '姓名', 2: '年龄', 3: '性别'}
people = [['小秦', '18', '女'], ['小张', '23', '男'], ['小李', '19', '女']]

temp_list = []
temp_dictionary = {}

k = 1
index_keys = index.keys()
index_values = index.values()
for person in people:
    if is_row:
        temp_list.append(pd.Series(person, index=index_values, name=k))
        k += 1
    else:
        j = 0
        for col_name in index_values:
            if col_name in temp_dictionary.keys():
                temp_dictionary[col_name].append(person[j])
            else:
                temp_dictionary[col_name] = [person[j]]
            j += 1
del k

col_dictionary = {}
if not is_row:
    for key in temp_dictionary.keys():
        col_dictionary[key] = pd.Series(temp_dictionary[key], index=index_values, name=key)

# 指定series为行
df = pd.DataFrame(temp_list) if is_row else pd.DataFrame(col_dictionary)

df.to_excel('F:/workspace/python/doc_demo/index.xlsx', index=False)
