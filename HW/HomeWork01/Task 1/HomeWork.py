from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.selenium.dev/')
title = driver.title
print("Page Title:", title)
driver.quit
