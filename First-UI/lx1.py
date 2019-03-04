from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
try:
    driver.get("https://www.baidu.com")
    driver.switch_to_window(driver.current_window_handle)
    search_a=driver.find_elements_by_tag_name("a")
    print("共找到%d个结果"%len(search_a))
    for ele in search_a:
        print(ele.text)



finally:
    driver.quit()