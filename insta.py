import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(4)
username = driver.find_element_by_name("username")
username.clear()
username.send_keys("azhad.ghufran")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("Dabkdi@126814")
button = driver.find_element_by_xpath("//button[@type='submit']")
button.click()
time.sleep(10)
driver.close()
