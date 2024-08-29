from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

"""
DrissionPage的常见工具

1. 页面类[主要用于控制浏览器和收发数据包]
    1. ChromiumPage 控制浏览器
    2. SessionPage 收发数据包
    3. WebPage 兼职控制浏览器和收发数据包
2. 配置工具[设置浏览器参数，尽在启动浏览器时有用，接管已存在的浏览器时时不生效的]
    1. ChromiumOptions 设置浏览器启动参数
    2. SessionOptions 用于配置Session对象的启动参数与SessionPage或WebPage s模式

"""

# 通过在浏览器输入[chrome://version] [edge://version]可获取浏览器可执行文件路径，DrissionPage会自动获取谷歌的可执行文件路径
# GoogleChrome可执行文件路径：C:\Program Files\Google\Chrome\Application\chrome.exe

# 手动选择浏览器可执行文件路径
chrome_executable_file = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
ChromiumOptions().set_browser_path(chrome_executable_file).save()


# 导入浏览器
page = ChromiumPage()
page.get('http://DrissionPage.cn')
