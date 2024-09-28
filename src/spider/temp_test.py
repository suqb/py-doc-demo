from DrissionPage import Chromium, ChromiumOptions

# 创建多个配置对象，每个指定不同的端口号和用户文件夹路径
co1 = ChromiumOptions().set_paths(local_port=9111, user_data_path=r'D:\data1')
# co2 = ChromiumOptions().set_paths(local_port=9222, user_data_path=r'D:\data2')

# 创建多个页面对象
tab1 = Chromium(addr_or_opts=co1).latest_tab
# tab2 = Chromium(addr_or_opts=co2).latest_tab

# 每个页面对象控制一个浏览器
tab1.get('https://DrissionPage.cn')
# tab2.get('https://www.baidu.com')