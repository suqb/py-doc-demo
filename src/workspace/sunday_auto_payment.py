from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


# 自动获取付款链接，进行账期付款
def executor():
    print('正在执行自动付款')


# date触发器，用于指定时间触发，适用于只执行一次的任务 run_date可以是date类型，也可以时datetime类型或文本类型
def data_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(executor, 'date', run_date=datetime(2024, 9, 3, 9, 48, 30), args=['指定date任务触发'])
    scheduler.start()

