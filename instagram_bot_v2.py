from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(8)
    def like_photo(self):
        driver = self.driver
        print(driver)
        while True:
            follow_count=0
            like_count = 0
            driver.get("https://www.instagram.com/explore/")
            time.sleep(4)
            for i in range(1,3):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)
            hrefs_in_view = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs_in_view]
            pic_hrefs = [elem for elem in pic_hrefs if 'com/p/' in elem]
            print("Total number of user to be Followed",len(pic_hrefs))
            for pic in pic_hrefs:
                driver.get(pic)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                try:
                    driver.find_element_by_xpath("//*[@aria-label='Like']").click()
                    like_count +=1
                    print("Liked : ",like_count)
                    time.sleep(2)
                except Exception as e:
                    time.sleep(2)
                try:
                    driver.find_element_by_xpath("//button[text()='Follow']").click()
                    follow_count +=1
                    print("Followed : ",follow_count)
                    time.sleep(18)
                except Exception as e:
                    time.sleep(18)
if __name__ == "__main__":

    username = "azhad.ghufran"
    password = "Dabkdi@126814"

    ig = InstagramBot(username, password)
    ig.login()
    ig.like_photo()
    ig.closeBrowser()
