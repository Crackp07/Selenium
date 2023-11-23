from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestEnterAcc():
    driver = webdriver.Chrome()
    vars = {}
    driver.get("https://opencartforum.com/")
    driver.set_window_size(1536, 835)
    driver.find_element(By.ID, "elUserSignIn").click()
    driver.find_element(By.NAME, "auth").click()
    driver.find_element(By.NAME, "auth").send_keys("byushuk@gmail.com")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("34527259Very")
    driver.find_element(By.ID, "elSignIn_submit").click()
    element = driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > .ipsButton_veryLight")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    print("Succsess")
    driver.quit()