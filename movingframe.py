import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
time.sleep(4)
driver.switch_to_frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to_default_content()

driver.switch_to_frame("packageFrame")
driver.find_element_by_link_text("Alert").click()

driver.switch_to_default_content()

driver.switch_to_frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
