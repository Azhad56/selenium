import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(2)

entry = driver.find_element_by_name("q")
entry.send_keys("Azhad Ghufran")
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]").click()
time.sleep(2)
#Move backward
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
