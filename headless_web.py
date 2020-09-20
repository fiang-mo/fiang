from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import platform

# 无界面
print(platform.system())
if platform.system() == 'Windows':
    chrome_options = Options()
    # 设置当前窗口的宽度和高度
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    # Linux启动
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--no-sandbox') #解决DevToolsActivePort文件不存在报错问题
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu') # 禁用GPU硬件加速
    chrome_options.add_argument('--headless') # 无界面
    #启动浏览器
    driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.cnblogs.com/yoyoketang/")
time.sleep(5)
print(driver.title)
print(driver.page_source)
driver.quit()


