from selenium import webdriver
import time
driver=webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(1)
driver.execute_script("window.alert('这是一个弹出框')")
time.sleep(2)
driver.switch_to.alert.accept()