from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://ok.ukrposhta.ua/")
driver.find_element(By.XPATH, "//*[@id='login-form']/form/div[4]/div/div/a[2]").click()
driver.find_element(By.NAME, 'login').send_keys('byushuk@gmail.com')
driver.find_element(By.NAME, 'reset-password')
window_handles = driver.window_handles

driver.switch_to.new_window('tab')
driver.get('https://mail.google.com/')
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('byushuk@gmail.com')
driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/div[3]").click()
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('234527259Cra')
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]').click
driver.find_element(By.XPATH, "//*[@id=':24;']").click()
driver.find_element(By.XPATH, "//*[@id=':ob']/div[2]/div[2]/table/tbody/tr/td/div[2]/div/div/div/div/div/div[2]/a/div").click()
driver.switch_to.new_window('tab')
driver.find_element(By.XPATH, "//*[@id='pass']").send_keys("newpassword")
driver.find_element(By.XPATH, "//*[@id='password-confirm']").send_keys("newpassword")
driver.find_element(By.XPATH, "//*[@id='reset-password']").click()