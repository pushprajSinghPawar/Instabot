from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
driver=webdriver.Firefox()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(1)
user=driver.find_element(By.NAME,"username")
user.send_keys("health_and_life_over_and_under")
passwd=driver.find_element(By.NAME,"password")
passwd.send_keys("yyZpcuwkByz34VP")


time.sleep(1)
button=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
button.click()
time.sleep(100)