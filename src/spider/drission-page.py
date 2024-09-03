from DrissionPage import ChromiumPage
from DrissionPage import SessionPage
from DrissionPage import ChromiumOptions
from DrissionPage import WebPage

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
ChromiumOptions().set_browser_path(chrome_executable_file).save()


# 操控浏览器
def operate_chromium_page():
    # 创建浏览器控制对象
    page = ChromiumPage()

    # 访问参数中的地址
    page.get('https://gitee.com/login')

    # 查找元素，返回一个ChromiumElement对象 #:根据ID查找[其中ele方法已经内置了等待，如果元素未加载他会执行等待直到元素出现为止，默认超时时间10s]
    user_name_input = page.ele("#user_login")

    # 对元素输入文本
    user_name_input.input('18922420401')

    # 链式操作
    page.ele('#user_password').input('wmj18476723899')

    # 获取登录按钮，此次使用的@为按元素名查找
    page.ele('@value=登 录').click()


# 收发数据包
def seeding_and_receiving_data_packets():
    # 打开SessionPage
    page = SessionPage()

    # 遍历三页Gitee的开源项目页面
    for i in range(1, 4):
        # 打开开源项目页面，以循环状态为目标页
        page.get(f'https://gitee.com/explore/all?page={i}')
        # 从页面中获取所有项目名称标签
        links = page.eles('.title project-namespace-path')
        # 变例项目名称a标签
        for link in links:
            # 打印标签
            print(link)


# 模式切换：通常用于应付登录检查很严格的网站，可以用浏览器处理登录在转换模式用收发数据包的形式去采集数据
def switch_page_mode():
    page = WebPage()
    page.get('https://gitee.com/explore/all')

    page.change_mode()

    items = page.ele('.ui relaxed divided items explore-repo__list').eles('.item')
    for item in items:
        print(item('t:h3').text)
        print(item('.project-desc mb-1').text)
        print()


switch_page_mode()

