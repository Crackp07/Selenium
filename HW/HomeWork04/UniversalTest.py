from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class AuthTester:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self, username, password):
        try:
            self.driver.get(self.url)
            username_field = self.driver.find_element(By.XPATH, "//input[@type='email']")
            password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")

            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.ENTER)
            return True  
        except Exception as e:
            print(f"Error during login. Exception: {e}")
            return False  

driver = webdriver.Chrome()
url = input("Enter the URL: ")
username = input("Enter your username: ")
password = input("Enter your password: ")

tester = AuthTester(driver, url)

if tester.login(username, password):
    print("Login successful!")
else:
    print("Login failed!")

driver.quit()