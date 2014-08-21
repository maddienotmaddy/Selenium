# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#import actionChains so we can simulate mouse overs
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CreateEditDeleteDept2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://ta2.vt-s.net/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_edit_delete_dept2(self):
        driver = self.driver
        driver.get(self.base_url + "/home")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("edit-name").clear()
        driver.find_element_by_id("edit-name").send_keys("VTHSiteAdmin")
        driver.find_element_by_id("edit-pass").clear()
        driver.find_element_by_id("edit-pass").send_keys("VT$L0gin")
        driver.find_element_by_id("edit-submit").click()
        # ERROR: Caught exception [ERROR: Unsupported command [mouseOver | link=Content | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [mouseOver | link=Add content | ]]
        #create a new ActionChains object for performing mouse clicks
        actions = ActionChains(driver)

        #tell it to move the mouse over the Content admin link
        actions.move_to_element(driver.find_element_by_link_text("Content"))
        actions.perform() #actually perform the action

        #now that the menu cascades we can look for the Add Content link
        actions.move_to_element(driver.find_element_by_link_text("Add content"))
        actions.perform() #perform the action

        #now the final cascade with the Department/Board link should be clickable
        driver.find_element_by_link_text("Department/Board Home Page").click()
        driver.find_element_by_id("edit-title").clear()
        driver.find_element_by_id("edit-title").send_keys("This is a test department")
        driver.find_element_by_xpath("//form[@id='department-node-form']/div/div[3]/ul/li[2]/a/strong").click()
        driver.find_element_by_id("edit-field-is-dept-und").click()
        driver.find_element_by_css_selector("li.vertical-tab-button.Address > a > span.summary").click()
        driver.find_element_by_id("edit-field-address-und-0-name").clear()
        driver.find_element_by_id("edit-field-address-und-0-name").send_keys("Town Hall")
        driver.find_element_by_id("edit-field-address-und-0-street").clear()
        driver.find_element_by_id("edit-field-address-und-0-street").send_keys("123 Main Street")
        driver.find_element_by_id("edit-field-address-und-0-city").clear()
        driver.find_element_by_id("edit-field-address-und-0-city").send_keys("OurTown")
        driver.find_element_by_id("edit-field-address-und-0-province").clear()
        driver.find_element_by_id("edit-field-address-und-0-province").send_keys("Massachusetts")
        driver.find_element_by_id("edit-field-address-und-0-postal-code").clear()
        driver.find_element_by_id("edit-field-address-und-0-postal-code").send_keys("01754")
        driver.find_element_by_xpath("//form[@id='department-node-form']/div/div[3]/ul/li[4]/a/strong").click()
        driver.find_element_by_xpath("//form[@id='department-node-form']/div/div[3]/ul/li[10]/a/span").click()
        driver.find_element_by_id("edit-multiple-node-menu-enabled").click()
        driver.find_element_by_id("edit-multiple-node-menu-add-link-link-title").click()
        driver.find_element_by_id("edit-multiple-node-menu-add-link-link-title").clear()
        driver.find_element_by_id("edit-multiple-node-menu-add-link-link-title").send_keys("Selenium Department")
        driver.find_element_by_id("edit-submit--2").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Edit')])[3]").click()
        driver.find_element_by_id("edit-field-subtitle-und-0-value").clear()
        driver.find_element_by_id("edit-field-subtitle-und-0-value").send_keys("changing subtitle")
        driver.find_element_by_id("edit-submit--2").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Edit')])[3]").click()
        driver.find_element_by_id("edit-delete--2").click()
        driver.find_element_by_id("edit-submit").click()
        
    
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
