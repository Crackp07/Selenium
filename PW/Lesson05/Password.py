from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
# driver.get('https://www.work.ua/jobseeker/login/')
# driver.find_element(By.NAME, 'user_login').send_keys('byushuk@gmail.com')
# driver.find_element(By.XPATH, "//*[@id='lForm']/div[7]/button").click()
# WebDriverWait(driver, 30).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='lForm']/div[10]/a" )))
# driver.find_element(By.XPATH, "//*[@id='lForm']/div[10]/a" ).click()
# # -----------------------------------------------------------------------------------
# driver.switch_to.new_window('tab')
driver.get('https://mail.google.com/')
# driver.find_element(By.XPATH, "/html/body/header/div/div/div/a[2]")
driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys('byushuk@gmail.com')
driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))
driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input").send_keys('fdsfsadf')
driver.find_element(By.XPATH, "//*[@id=':24']").click()
driver.switch_to.window()

# driver.close()
