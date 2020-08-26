import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://account.codingblocks.com/signup")
time.sleep(4)
element = driver.find_element_by_xpath("//select[@name='gradYear']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
driver.close()
