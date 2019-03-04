from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.qiushibaike.com/text/")
doc = driver.page_source

def zhua():
    zuozhe=driver.find_elements_by_css_selector(".col1 h2")
    zuowen=driver.find_elements_by_css_selector(".content")
    zan=driver.find_elements_by_css_selector(".stats-vote>i")
    writers=[]
    wen=[]
    smile=[]
    for i in zuozhe:
        writers.append(i.text)
    for j in zuowen:
        wen.append(j.text)
    for a in zan:
        smile.append(a.text)
    for i in range(0,len(writers)):
        print("作者:",writers[i])
        print("内容：",wen[i])
        print("好笑人数:",smile[i])
def next():
    xia=driver.find_element_by_css_selector(".next")
    xia.click()
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
# shu=driver.find_element_by_css_selector(".pagination span")
# print(shu.text)
# for i in range(1,13):
#     zhua()
#     next()

