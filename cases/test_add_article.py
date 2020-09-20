from selenium import webdriver
from pages.articleclassify_page import ArticleclassifyPage
import pytest
import allure

@allure.feature("添加文章分类")
class Testarticle():

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-6-2.html")
    @allure.title("输入中文，编辑成功")
    def test_add_article_1(self, login):
        driver = login
        #添加文章分类
        article = ArticleclassifyPage(driver)
        with allure.step("step1:点击页面左侧列表中的文章分类"):
            article.click_articleclassify()
        with allure.step("step2:点击添加文章分类按钮"):
            article.click_add_articleclassify()
        with allure.step("step3:输入框输入"):
            article.input_articleclassify("文学")
        with allure.step("step4:点击保存按钮"):
            article.save_articleclassify()
        with allure.step("step5:获取实际结果"):
            result = article.is_add_success(expect="添加成功")
        #断言
        assert result

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-3-1.html")
    @allure.title("输入英文，编辑成功")
    def test_add_article_2(self, login):
        driver = login
        #添加文章分类
        article = ArticleclassifyPage(driver)
        with allure.step("step1:点击页面左侧列表中的文章分类"):
            article.click_articleclassify()
        with allure.step("step2:点击添加文章分类按钮"):
            article.click_add_articleclassify()
        with allure.step("step3:输入框输入"):
            article.input_articleclassify("art")
        with allure.step("step4:点击保存按钮"):
            article.save_articleclassify()
        with allure.step("step5:获取实际结果"):
            result = article.is_add_success(expect="添加成功")
        #断言
        assert result

    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-3-1.html")
    @allure.title("重复的分类")
    def test_add_article_3(self, login):
        driver = login
        #添加文章分类
        article = ArticleclassifyPage(driver)
        article.click_articleclassify()
        article.click_add_articleclassify()
        article.input_articleclassify("艺术")
        article.save_articleclassify()
        result = article.is_add_success(expect="添加成功")

        #添加重复的分类-预期结果：可以重复
        article.click_add_articleclassify()
        article.input_articleclassify("艺术")
        article.save_articleclassify()
        #断言
        assert not result


