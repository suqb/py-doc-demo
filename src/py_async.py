import asyncio
import threading
import time


def print_numbers():
    for i in range(10):
        print(i)
        time.sleep(0.5)


def print_letters():
    for i in 'abcdefghijklmn':
        print(i)
        time.sleep(1)


# 通过构建多线程的方式进行异步编排
def async_by_thread():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('线程执行完毕')


# asyncio python3.4后出现的协程模块
@asyncio.coroutine
def io_operate_1():
    print('open io 1..............')
    yield from asyncio.sleep(2)
    print('close io 1..............')


@asyncio.coroutine
def io_operate_2():
    print('open io 2..............')
    yield from asyncio.sleep(2)
    print('close io 2..............')


tasks = [
    asyncio.ensure_future(io_operate_1()),
    asyncio.ensure_future(io_operate_2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
