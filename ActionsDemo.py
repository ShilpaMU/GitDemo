#This is pushed to git
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver import ActionChains

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.get("https://rahulshettyacademy.com/AutomationPractice/"))
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform() #right click
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()