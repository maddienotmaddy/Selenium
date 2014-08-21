from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Basicpython(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ta2.vt-s.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_basicpython(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        print self.is_element_present(By.LINK_TEXT, "My Account")
        driver.find_element_by_link_text("Login").click()
        print driver.current_url
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("VTHGroupAdmin")
        driver.find_element_by_id("edit-pass").clear()
        driver.find_element_by_id("edit-pass").send_keys("VT$L0gin")
        driver.find_element_by_id("edit-submit").click()
        print driver.current_url
        print self.is_element_present(By.LINK_TEXT, "My Account")
        driver.get(self.base_url + "/")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
