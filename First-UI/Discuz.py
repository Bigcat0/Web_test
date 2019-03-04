from selenium import webdriver
import time
driver=webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://127.0.0.1/forum.php")
driver.switch_to_window(driver.current_window_handle)
# 登录
username=driver.find_element_by_name("username")
username.send_keys("admin")
pad=driver.find_element_by_name("password")
pad.send_keys("root")
login=driver.find_element_by_css_selector(".fastlg_l button")
login.click()
time.sleep(5)
# 默认发帖
mo=driver.find_element_by_css_selector(".fl_tb h2 a")
mo.click()
driver.switch_to_window(driver.current_window_handle)
time.sleep(5)


# 标题
biao=driver.find_element_by_css_selector(".px")
biao.send_keys("啦啦啦")
# 内容
wen=driver.find_element_by_css_selector(".pt")
wen.send_keys("kslnfkslndfklsnkfdsnknfsdnfsndj")

# 发表
fa=driver.find_element_by_css_selector(".bm_c button")
fa.click()

# 回复
huifu=driver.find_element_by_css_selector(".pt")
huifu.send_keys("skdnfjksnfjksnjfnsfdjsnjf")
# 发表回复
fa=driver.find_element_by_css_selector(".plc button")
fa.click()
# 退出
logout=driver.find_element_by_link_text("退出")
logout.click()


