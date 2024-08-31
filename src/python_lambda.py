# 在python中lambda函数通常以lambda关键字， 并且表达式只能时单一的表达式不能包含复杂的循环赋值的等，创建格式如下
# lambda args1, args2, ... : 表达式

def lambda_handler(func, context):
    print(func(context))


lambda_handler(lambda x: x ** 2, 5)
