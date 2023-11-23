from selenium import webdriver
import unittest

class TestSeleniumDevPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_page_title(self):
        self.driver.get("https://www.selenium.dev/")
        title = self.driver.title
        self.assertEqual(title, "Selenium")
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main