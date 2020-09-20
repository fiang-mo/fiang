from common.base import Base
import allure

class ArticleclassifyPage(Base):
    '''文章分类页面'''

    # 文章分类按钮（复数）
    loc_1 = ("xpath",'//a[@href="/xadmin/hello/articleclassify/"]')
    # 添加文章分类
    loc_2 = ("xpath", '//*[@id="content-block"]/div[1]/div[2]/div/a')
    # 输入框
    loc_3 = ("id", "id_n")
    # 保存
    loc_4 = ("xpath", '//*[@id="articleclassify_form"]/div[2]/button')
    # 获取保存成功的文本信息
    loc_5 = ("xpath", '//*[@id="content-block"]/div[2]')

    @allure.step("点击页面左侧的文章分类按钮")
    def click_articleclassify(self):
        '''点击左侧文章分类'''
        self.click(self.loc_1)

    @allure.step("点击添加文章分类按钮")
    def click_add_articleclassify(self):
        '''点击添加文章分类'''
        self.click(self.loc_2)

    @allure.step("输入内容")
    def input_articleclassify(self, text=''):
        '''输入内容'''
        self.send(self.loc_3, text)

    @allure.step("点击保存按钮")
    def save_articleclassify(self):
        '''点保存按钮'''
        self.click(self.loc_4)

    @allure.step("判断是否添加成功，返回True / False ")
    def is_add_success(self, expect=""):
        '''判断是否添加成功，返回True / False '''
        get_result = self.get_text(self.loc_5)
        print("保存成功后，获取到页面的信息：%s" %get_result)
        return expect in get_result

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    #先登录
    from pages.login_page import LoginPage
    web = LoginPage(driver)
    web.login()

    #添加文章分类
    article = ArticleclassifyPage(driver)
    article.click_articleclassify()
    article.click_add_articleclassify()
    article.input_articleclassify("文学")
    article.save_articleclassify()

    #断言
    result = article.is_add_success(expect="添加成功")
    driver.quit()
    assert result
