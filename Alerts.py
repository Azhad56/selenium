import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
time.sleep(4)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
# driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
time.sleep(5)
driver.close()
