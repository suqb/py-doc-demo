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
    3. Settings 用于全局运行配置
3. 其它工具[位于DrissionPage.common中]
    1. Keys 键盘按键类
    2. Actions 动作链，在浏览器页面对象中已有内置
    3. By selenium一致的By类，便于项目迁移
    4. 其它
        1. wait_util 等待传入的方法结果为真
        2. make_session_ele 从html文本生成ChromiumElement对象
        3. configs_to_here 把配置文件复制到当前路径
        4. get_blob 获取指定的blob资源
        5. tree 用于打印页面对象或元素对象结构
        6. from_selenium 用于对接selenium代码
        7. from_playwright 用于对接playwright代码
4. 异常[位于DrissionPage.errors]
5. 衍生对象类型[Tab、Element等对象由Page对象生成，开发过程中需要类型判断时导入这些类型，位于DrissionPage.items]

"""

# 通过在浏览器输入[chrome://version] [edge://version]可获取浏览器可执行文件路径，DrissionPage会自动获取谷歌的可执行文件路径
# GoogleChrome可执行文件路径：C:\Program Files\Google\Chrome\Application\chrome.exe

# 手动选择浏览器可执行文件路径
chrome_executable_file = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
# ChromiumOptions().set_browser_path(chrome_executable_file).save()


# 导入浏览器
page = ChromiumPage()
page.get('https://gitee.com/login')

user_name_input = page.ele("#user_login")

user_name_input.input('')

page.ele('#user_password').input('')

page.ele('@value=登 录').chick()
