from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time



# 继承BasePage类
class HomePage(BasePage):
#     定位元素
    home_page_input_search_loc = (By.ID,'kw')
    home_page__button_search_loc=(By.ID,'su')

#输出搜索内容，并提交
    def search(self,content):
        self.sendkeys(content,*self.home_page_input_search_loc)
        time.sleep(5)
        self.click(*self.home_page__button_search_loc)
