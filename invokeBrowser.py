import time

from selenium import webdriver
# Selenium checks your current Chrome version and downloads the proper driver
driver = webdriver.Chrome()
# Navigate to healthcare service
driver.get("https://katalon-demo-cura.herokuapp.com/")
time.sleep(2)
