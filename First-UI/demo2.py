from selenium import webdriver
import time
import os


dir=os.path.dirname(__file__)
p=dir+"\chromedriver.exe"
driver=webdriver.Chrome(p)
try:
    driver.implicitly_wait(5)
    driver.get("https://www.baidu.com")

    driver.switch_to_window(driver.current_window_handle)
    print("百度首页已打开",driver.title)
    search_input=driver.find_element_by_id("kw")
    search_input.send_keys("java")
    search_input.submit()
    nums=driver.find_element_by_class_name("nums")
    print("-------",nums.text)
    driver.switch_to_window(driver.current_window_handle)
    wait_time=10
    driver.execute_script("window.alert(\"{}, {}秒后关闭\")".format(nums.text.replace("\n", "$"), wait_time))
    time.sleep(wait_time)
finally:
    driver.quit()



