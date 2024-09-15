import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from DrissionPage import ChromiumPage

# erp获取付款链接接口
erp_ali_payment_api = 'http://192.168.98.21:39095/pss/api/purchase/getAliPaymentUrl'
erp_ali_payment_api_local = 'http://localhost:8080/bessky_pss_web/api/purchase/getAliPaymentUrl'


# 自动获取付款链接，进行账期付款
def executor():
    print('正在执行自动付款...')
    response = requests.get(erp_ali_payment_api_local)
    response_json = response.json()
    url_dictionary = response_json['body']
    if url_dictionary is None:
        print('未查询到需要付款的采购订单...')
        return

    urls_list = url_dictionary['urls']
    if urls_list is None:
        print('未查询到需要付款的采购订单...')
        return

    page = ChromiumPage()
    page.get("https://www.baidu.com")

    for url in urls_list:
        current_tab = page.new_tab(url)
        # 关闭当前页面
        # div = page.ele('div.channel-card[data-channel="account_period"]')
        # div.click()
        # button = page.ele('button.next-btn.next-small.next-btn-primary.pay-btn')
        # button.click()
        page.close_tabs(current_tab)


# date触发器，用于指定时间触发，适用于只执行一次的任务 run_date可以是date类型，也可以时datetime类型或文本类型
def data_scheduler():
    scheduler = BlockingScheduler()
    cron_trigger = CronTrigger(day_of_week='sun', hour='0-23', minute='0-59', second='*/12')
    scheduler.add_job(executor, cron_trigger)
    scheduler.start()


executor()

