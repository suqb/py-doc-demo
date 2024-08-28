
# 带参数的装饰器 不带参数则不需要外层repeat函数 也不需要传递可变未命名参数（元组）与可变命名参数（字典）
def repeat(user_id):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(user_id + 'target method excluding...')
            func(*args, **kwargs)
            print(user_id + 'target method including...')
        return wrapper
    return my_decorator


@repeat(user_id=1024)
def update_user_password():
    print('update user password...')


update_user_password()