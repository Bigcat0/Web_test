from selenium import webdriver
import re


try:
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://home.baidu.com/contact.html")
    doc=driver.page_source
    emial=re .findall(r'[\w]+@[\w\.-]+',doc)
    for i in emial:
        print(i)
finally:
    driver.quit()
