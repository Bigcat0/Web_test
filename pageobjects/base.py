from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time
import os.path


logger=Logger(logger="BasePage").getlog()


class BasePage(object):




    def __init__(self,driver):
        self.driver=driver

    #
    def back(self):
    #浏览器后退按钮

        self.driver.back()
        # logger.info("浏览器后退")
    def forward(self):
        """
        浏览器前进按钮
        """
        self.driver.forward()
        # logger.info("浏览器前进")
    def open_url(self,url):
        """
        打开URL站点
        :param url:
        :return:
        """
        self.driver.get(url)
        logger.info("da打开站点")

    def quit_broser(self):
        """
        关闭停止浏览器服务
        :return:
        """
        self.driver.quit()



    # 保存图片
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name=file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("保存图片 : /screenshots")
        except Exception as e:
            pass
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s"%e)
    # 输入
    def sendkeys(self,text,*loc):
        el = self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容"+text)
        except Exception as e:
            print("未输入内容",e)
            logger.error("Faileed to type in input box with %s"%e)
            # self.get_windows_img()


    # 关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭页面")
        except Exception as e:
            logger.error("没有关闭%s"%e)
            pass

    #找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素-->"%loc)
        except:
            pass
            logger.error("%s页面未能找到%s 元素"%(self,loc))


    # 清除文本框
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除%s"%el)
        except Exception as e:
            logger.error("未清除%s"%e)
    # 点击元素
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("已点击")                      #添加el.text有问题
        except Exception as e:
            logger.error("未点击%s" %e)
    def text(self,*loc):
        el = self.find_element(*loc)
        try:
            print(el.text)
            logger.info("以获取")
        except Exception as e:
            logger.error("未获取%s" %e)