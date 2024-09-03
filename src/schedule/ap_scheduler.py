# https://www.cnblogs.com/zjyao/p/17666797.html

import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def job(args):
    print(args)


# 最基本的调度器
def base_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', seconds=10, args=['触发任务。。。。。。'])
    scheduler.start()


# date触发器，用于指定时间触发，适用于只执行一次的任务 run_date可以是date类型，也可以时datetime类型或文本类型
def data_scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'date', run_date=datetime(2024, 9, 3, 9, 48, 30), args=['指定date任务触发'])
    scheduler.start()


# cron触发器:范围之间用横杠隔开的字符串，时间从0开始，每隔5分钟就写*/5字符串
# day_of_week: mon, tue, wed, thu, fri, sat, sun
def cron_scheduler():
    scheduler = BlockingScheduler()
    cron_trigger = CronTrigger(day_of_week='tue', hour='0-23', minute='0-59', second='*/12')
    scheduler.add_job(job, cron_trigger, args=['cron任务触发......'])
    scheduler.start()


cron_scheduler()
