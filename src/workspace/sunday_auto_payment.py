import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from DrissionPage import Chromium

# erp获取付款链接接口
erp_ali_payment_api = 'http://192.168.98.21:39095/pss/api/purchase/alipayment/url'


# 右键浏览器桌面图标
# 选中目标添加 < --remote-debugging-port=9333>，添加完毕后大概长这样<"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=933>
# 然后双击浏览器运行，登录一个可账期付款阿里辉尔供应链子账
# 自动获取付款链接，进行账期付款 pyinstaller.exe -F -w .\sunday_auto_payment.py -i icon.png
def executor():
    # print('正在执行自动付款...')
    # response = requests.get(erp_ali_payment_api)
    # response_json = response.json()
    # url_dictionary = response_json['body']
    # if url_dictionary is None:
    #     print('未查询到需要付款的采购订单...')
    #     return
    #
    # urls_list = url_dictionary['urls']
    # if urls_list is None:
    #     print('未查询到需要付款的采购订单...')
    #     return

    urls_list = ['https://trade.1688.com/order/cashier.htm?orderId=4060397161064901415',]
    for url in urls_list:
        browser = Chromium(9333)
        current_tab = browser.latest_tab
        current_tab.get(url)
        browser.wait(2)
        div = current_tab.ele('@data-channel=account_period')
        div.click()
        browser.wait(2)
        button = current_tab.ele('@class=next-btn next-small next-btn-primary pay-btn')
        button.click()
        browser.wait(2)


# date触发器，用于指定时间触发，适用于只执行一次的任务 run_date可以是date类型，也可以时datetime类型或文本类型
def data_scheduler():
    scheduler = BlockingScheduler()
    cron_trigger = CronTrigger(day_of_week='sun', hour='8-23', minute='0-59', second='*/30')
    scheduler.add_job(executor, cron_trigger, max_instances=1)
    scheduler.start()


# data_scheduler()
executor()
