from selenium import webdriver
driver=webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    driver.switch_to_window(driver.current_window_handle)
    search_text=driver.find_element_by_partial_link_text("关于百度")
    search_text.click()

    search_text2=driver.find_element_by_partial_link_text("联系我们")
    search_text2.click()
    for handle in driver.window_handles:                                       ###点击进行=下一步
        driver.switch_to_window(handle)
    nums = driver.find_elements_by_class_name("mail-content-text")
    for i in nums:
        if "@" in i.text:
            print(i.text)
finally:
    driver.quit()