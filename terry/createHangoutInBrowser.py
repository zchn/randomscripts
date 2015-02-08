from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Raw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://plus.google.com/hangouts/_/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_raw(self):
        driver = self.driver
        f = open('urls.txt','w')
        while True:
            driver.get(self.base_url)
            time.sleep(30)
            print driver.current_url
            f.write(driver.current_url+'\n')
        f.close()
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
