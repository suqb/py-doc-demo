# 数字
class DataNumber:
    num = 100
    flag = True
    decimal = 3.14
    complex = complex(1 + 1)


# 字符串
class DataString:
    str_1 = 'firstname'
    str_2 = 'lastname'

    # 字符串拼接
    fullname = str_1 + ' ' + str_2

    # 字符串重复
    repeat_str = str_1 * 3

    # 字符串转小写
    str_1.lower()

    # 字符串转大写
    str_1.upper()

    # 首字母大写
    str_2.capitalize()

    # 去除两端空白
    str_1.strip()

    # 替换子串
    str_1.replace('name', '名称')

    # 拆分字符串
    str_1.split('t')

    # 查找字符串位置
    str_1.find('t')

    # 是否已某字符串开头
    str_1.startswith("fist")

    # 是否已某字符串结尾
    str_1.endswith("name")


# 列表
class DataList:
    list = [1, 2, 3]

    # 在指定位置插入元素
    list.insert(3, 5)

    # 在末尾添加元素
    list.append(4)

    # 移除指定元素
    list.remove(5)

    # 移除末尾元素
    list.pop()

    # 移除指定位置的元素
    list.pop(2)

    # 获取指定位置的元素
    fist_element = list[0]

    # 获取最后一个元素
    last_element = list[-1]

    # 获取子列表
    sub_list = list[1:3]

    # 排序
    list.sort()

    # 反转
    list.reverse()

    # 获取列表长度
    len(list)


# 字典
class DataDictionary:
    dictionary = {'username': 'Zhangsan', 'password': '123456', 'email': '2907829008@qq.com'}

    # 访问值
    username = dictionary['username']
    dictionary.get('password')

    # 添加或修改值
    dictionary['name'] = 'suqb'
    dictionary['age'] = 28

    # 移除键值对
    del dictionary['password']
    dictionary.pop('age')

    # 获取所有键
    keys = dictionary.keys()

    # 获取所有值
    values = dictionary.values()

    # 获取所有键值对
    items = dictionary.items()


# 元组
class DataTuple:
    my_tuple = (1, 2, 3)

    # 访问
    fist = my_tuple[0]
    last = my_tuple[-1]

    # 解包
    f, l, s = my_tuple


# 集合
class DataSet:
    unique_set = {1, 2, 3}
    other_set = {3, 4, 5}

    # 添加元素
    unique_set.add(4)

    # 移除元素
    unique_set.remove(4)

    # 移除元素，当元素不存在时不报错
    unique_set.discard(4)

    # 求并集
    union = unique_set.union(other_set)

    # 求交集
    intersection = unique_set.intersection(other_set)

    # 求差集
    difference = unique_set.difference(other_set)




