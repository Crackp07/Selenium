from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def read_auths_from_file(file_path):
    auths = []
    with open(file_path) as file:
        for line in file:
            auths.append(tuple(line.strip().split()))
    return auths

def auth_test(url, driver, auth_list):
    for auth in auth_list:
        try:
            driver.get(url)
            e_mail = 0
            try:
                e_mail = driver.find_element(By.XPATH, "//input[@type='email']")
            except:
                e_mail = driver.find_element(By.NAME,'email')
            password = driver.find_element(By.XPATH, "//input[@type='password']")

            e_mail.send_keys(auth[0])
            password.send_keys(auth[1])
            password.send_keys(Keys.ENTER)
            input("Press Enter to continue")
        except Exception as e:
            print(f"Error with auth: {auth}. Exception: {e}")
driver = webdriver.Chrome()
url = input("Enter the URL: ")
file_path = 'd:/QA32Celenium/PW/Lesson04/login_parol.txt'
auths = read_auths_from_file(file_path)


auth_test(url, driver, auths)

driver.close()
