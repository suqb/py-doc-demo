from DrissionPage import Chromium, ChromiumOptions
import os
import logging
import datetime


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


try:
    a = 3
    b = 0
    a/b
except Exception as e:
    logging.info("无法支付订单，请检查订单是否已取消", e)