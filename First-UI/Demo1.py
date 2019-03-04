from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
# driver=webdriver.Chrome("./chromedriver.exe")
# driver.get("https://www.baidu.com")

dir=os.path.dirname(__file__)
c_d_path=dir +"\chromedriver.exe"
driver = webdriver.Chrome(c_d_path)
# driver.get("https://www.yahoo.com")
driver.get("http://127.0.0.1/forum.php?mod=viewthread&tid=69&extra=page%3D1")
# assert "Yahoo" in driver.title

# el=driver.find_element_by_name("p")
# el.send_keys("seleniumhq"+Keys.ENTER)
# driver.quit()
a=driver.find_element_by_css_selector(".pcht tr:nth-child(2) td:nth-child(3)")
a.text

# dir=os.path.dirname(__file__)
# p= dir +"./geckodriver.exe"
# driver=webdriver.Firefox(executable_path=p)
# driver.get("https://www.yahoo.com")
# assert "Python" in driver.title


# dir=os.path.dirname(__file__)
# c_d_path=dir +"./IEDriverServer.exe"
# driver = webdriver.Ie(c_d_path)
# driver.get("https://www.bai.com")
# assert "Python" in driver.titledu












