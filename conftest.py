from selenium import webdriver
import pytest
from pages.login_page import LoginPage
import os
import allure

_driver = None

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     '''获取每个用例状态的钩子函数'''
#     # 获取钩子方法的调用结果
#     outcome = yield
#     rep = outcome.get_result()
#     # 仅仅获取用例call执行结果是失败的情况，不包含 setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:  # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = "(%s)" %item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         #添加allure报告截图
#         with allure.step('添加失败截图...'):
#             allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

@pytest.fixture(scope="session")
def driver():
    global _driver
    if _driver == None:
        _driver = webdriver.Chrome()
    _driver.maximize_window()

    yield _driver

    _driver.quit()

@pytest.fixture(scope="session")
def login(driver, base_url):
    web = LoginPage(driver)
    web.login(base_url)
    return driver


