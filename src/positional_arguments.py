def positional_arguments(*args):
    print(type(args))
    print(args)


def keyword_arguments(**kwargs):
    print(type(kwargs))
    print(kwargs)


positional_arguments(1, 2, 3, 4)
keyword_arguments(name='zhangsna', email='2907829008@qq.com')
