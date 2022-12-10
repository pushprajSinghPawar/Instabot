from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver=webdriver.Firefox()

def remove(string):
    return "".join(string.split())

def searchATag(tag):
    global driver
    page = driver.get('https://www.instagram.com/explore/tags/' + tag )
    time.sleep(6)
    return page 


def login():
    global driver
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(1)
    user=driver.find_element(By.NAME,"username")
    time.sleep(1)
    user.send_keys("health_and_life_over_and_under")
    passwd=driver.find_element(By.NAME,"password")
    passwd.send_keys("yyZpcuwkByz34VP")
    time.sleep(1)
    button=driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
    button.click()
    time.sleep(5)



login()
Domain_Hashtags=list('#health #healthyfood #bodygoals #bmi #diet #dietplan #bodybuilding #nutrition #healthknowledge #healthylifestyle #healthyliving #healthylivingtips #bodypositivity '.split('#'))

for ATag in Domain_Hashtags[1:]:
    page=searchATag(ATag)
time.sleep(100)
