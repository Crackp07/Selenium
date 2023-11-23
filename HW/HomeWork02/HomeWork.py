# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHomeWork():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_homeWork(self):
        self.driver.get("https://www.mazda.com/")
        self.driver.set_window_size(1536, 835)
        self.driver.find_element(By.ID, "header-search").click()
        self.driver.find_element(By.ID, "header-search").send_keys("Mazda 2")
        self.driver.find_element(By.CSS_SELECTOR, ".button-search").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".result_txt > p").text == "Results for \\\"Mazda 2\\\" , 510 Results Found."
        assert self.driver.title == "MAZDA:Search Result"
        first_result = self.driver.find_element(By.CSS_SELECTOR, "#contents_2014 > div.result_detail_area > div:nth-child(1) > h3 > a)")
        print("First search result:", first_result.text)

  