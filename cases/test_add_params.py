from selenium import webdriver
from pages.articleclassify_page import ArticleclassifyPage
import pytest
import allure
from setting import basepath
import os
from common.read_yaml import read_yaml_data

# 测试数据
# test_data = [("中文", True),("English", True),("123456", True)]

yamlpath = os.path.join(basepath, "testdatas", "test_cases.yml")
print("读取到yaml文件地址：%s" %yamlpath)
d = read_yaml_data(yamlpath)
test_data = d.get('test_add_params', [])
print("测试数据：%s" %test_data)

@allure.feature("添加文章分类")
class Testarticle():
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    # @allure.title("输入中文，编辑成功")
    @pytest.mark.parametrize("test_input, expected, title", test_data)
    def test_add_article_1(self, login, test_input, expected, title):
        driver = login
        #添加文章分类
        allure.dynamic.title("dynamic动态添加："+title)
        article = ArticleclassifyPage(driver)
        with allure.step("step1:点击页面左侧列表中的文章分类"):
            article.click_articleclassify()
        with allure.step("step2:点击添加文章分类按钮"):
            article.click_add_articleclassify()
        with allure.step("step3:输入框输入"):
            article.input_articleclassify(test_input)
        with allure.step("step4:点击保存按钮"):
            article.save_articleclassify()
        with allure.step("step5:获取实际结果"):
            result = article.is_add_success(expect="添加成功")
        #断言
        assert result == expected, "断言失败，原因："


