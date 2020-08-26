import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://seleniumpractise.blogspot.com/2017/07/multiple-window-examples.html")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='post-body-6170641642826198246']/a[1]").click()
driver.find_element_by_xpath("//*[@id='post-body-6170641642826198246']/a[2]").click()
driver.find_element_by_xpath("//*[@id='post-body-6170641642826198246']/a[3]").click()
print(driver.current_window_handle)
handles = driver.window_handles
for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)
driver.close()
