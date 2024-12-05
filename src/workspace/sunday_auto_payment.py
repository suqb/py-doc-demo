import requests
import os
import logging
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from DrissionPage import Chromium

# ERP获取付款链接接口
erp_ali_payment_api = 'http://gzerpx.ser.ltd:39095/pss/api/purchase/alipayment/url'
# 获取当前日期
current_date = datetime.date.today().strftime('%Y-%m-%d')
# 获取当前文件路径
current_dir = os.path.dirname(os.path.realpath(__file__))
# 创建日志记录
log_path = os.path.join(current_dir, f'sunday_auto_payment-{current_date}.log')
# 日志配置
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    encoding='utf-8')
# 用于存储无法支付的订单 URL
failed_urls = set()


# pip install requests
# pip install DrissionPage
# pip install apscheduler
# pip install pyinstaller
# 指定浏览器运行端口：--remote-debugging-port=9333
# 打包当前脚本：pyinstaller.exe -F -w .\sunday_auto_payment.py -i icon.png
# 需要阿里巴巴账号已登录并且记住密码状态
def executor():

    # 调用ERP支付接口获取支付链接
    response = requests.get(erp_ali_payment_api)

    # 获取响应JSON
    response_json = response.json()

    # 打印响应信息
    logging.info(response_json)

    # 获取响应主题
    url_dictionary = response_json['body']
    if url_dictionary is None:
        logging.info("响应体为空，结束本次任务......")
        return

    # 获取响应URL列表
    urls_list = url_dictionary['urls']
    if urls_list is None:
        logging.info("响应体为空，结束本次任务......")
        return

    # 接管当前浏览器
    browser = Chromium(9333)

    # 获取最新的选项卡
    latest_tab = browser.latest_tab

    # 遍历链接单个付款
    for url in urls_list:

        logging.info("正在为......")

        # 如果 URL 已在失败集合中，跳过
        if url in failed_urls:
            logging.info("跳过无法支付的订单 URL: %s", url)
            continue

        # 打开付款链接
        latest_tab.get(url)
        browser.wait(2)

        try:
            # 校验当前是否已经登录
            if not latest_tab.url.startswith('https://trade.1688.com/order'):
                # 未登录则点击登录链接 [前提是浏览器曾经登录过当前电脑并且点击了自动填充密码]
                latest_tab.ele('@class=fm-button fm-submit password-login  button-low-light').click()
                browser.wait(2)
        except Exception as e:
            logging.info("无法登录指alibaba管理后台，请检查当前PC是否验证账号并设置记住密码： %s", str(e))

        try:
            # 获取账期支付DIV
            div = latest_tab.ele('@data-channel=account_period')
            # 选择账期支付
            div.click()
            browser.wait(2)

            # 获取支付按钮
            button = latest_tab.ele('@class=next-btn next-small next-btn-primary pay-btn')
            # 点击支付
            button.click()
            browser.wait(2)
        except Exception as e:
            failed_urls.add(url)
            logging.info("无法支付订单，请检查订单是否已取消: %s", str(e))


# corn触发器每周日八点到23点，每隔而是分钟执行一次，并发数为1，如果上次任务未执行完毕则废弃
def auto_payment_scheduler():
    # 创建调度器
    scheduler = BlockingScheduler()
    # 周日每隔20分钟执行一次
    cron_trigger = CronTrigger(day_of_week='sun', hour='8-23', minute='*/20')
    # 添加自动付款执行器
    scheduler.add_job(executor, cron_trigger, max_instances=1)
    # 启动调度器
    scheduler.start()


# 创建并启动调度器
if __name__ == '__main__':
    auto_payment_scheduler()

# 直接触发任务用于测试
# executor()
