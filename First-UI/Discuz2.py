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
# 进入默认版块
mo=driver.find_element_by_css_selector(".fl_tb h2 a")
mo.click()
driver.switch_to_window(driver.current_window_handle)
time.sleep(5)

# 删除
delect1=driver.find_element_by_name("moderate[]")
delect1.click()
delect2=driver.find_element_by_link_text("删除")
delect2.click()
sure=driver.find_element_by_css_selector(".tm_c button")
sure.click()

# 管理
guan=driver.find_element_by_link_text("管理中心")
guan.click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)

# # 管理登录
# guan_login=driver.find_element_by_css_selector(".loginform input")
# guan_login.send_keys("root")
# # 提交
# tijiao=driver.find_element_by_css_selector(".loginnofloat input")
# tijiao.click()
# 论坛
lun=driver.find_element_by_id("header_forum")
lun.click()
driver.switch_to_window(driver.current_window_handle)
time.sleep(5)

# 添加新版块
driver.switch_to_frame(0)
add=driver.find_element_by_css_selector(".lastboard a")
add.click()
# 提交创建
tj=driver.find_element_by_css_selector(".fixsel input")
tj.click()
# 管理员退出
time.sleep(6)
driver.close()
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
login_out=driver.find_element_by_link_text("退出")
login_out.click()
time.sleep(3)
# 用户登录
username=driver.find_element_by_name("username")
username.send_keys("wangwei")
pad=driver.find_element_by_name("password")
pad.send_keys("weishu0124")

login1=driver.find_element_by_css_selector(".fastlg_l button")
login1.click()
time.sleep(5)

# 刷新
s=driver.find_element_by_css_selector(".wp img")
s.click()
time.sleep(5)
# xin新版块
new_fa=driver.find_element_by_css_selector(".fl_row h2 a")
new_fa.click()

driver.switch_to_window(driver.current_window_handle)
time.sleep(5)

new_biao=driver.find_element_by_css_selector(".px")
new_biao.send_keys("lllllllllllllllllll")

new_n=driver.find_element_by_css_selector(".pt")
new_n.send_keys("2222222222222222222222")

# 发
new_fa=driver.find_element_by_css_selector(".bm_c button")
new_fa.click()

new_hui=driver.find_element_by_css_selector(".area textarea")
new_hui.send_keys("amkdnakdnk")

# 退出
logout1=driver.find_element_by_link_text("退出")
logout1.click()


