import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
time.sleep(4)
element = driver.find_element_by_id("box6")
target = driver.find_element_by_id("box106")
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
time.sleep(10)
driver.close()
