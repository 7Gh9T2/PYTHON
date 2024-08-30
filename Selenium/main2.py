from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")


search_box = driver.find_element("name", "search")

search_box.send_keys("python")
search_box.send_keys(Keys.ENTER)


import time
time.sleep(30)


