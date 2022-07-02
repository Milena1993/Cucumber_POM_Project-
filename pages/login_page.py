from selenium.webdriver.common.by import By
import re


class LoginPage:
    button_manager_login_button = (By.XPATH,'//button[@ng-click="manager()"]')  
    add_customer_button =  (By.XPATH, '//button[@ng-click="addCust()"]')
    page_title = "XYZ Bank"
    
    def __init__(self, driver):
        super().__init__()
        self.driver = driver 
    
    def get_page_title(self):
        driver = self.driver
        get_title = driver.title
        return get_title

    def bank_manager_login(self):
        self.driver.find_element(*LoginPage.button_manager_login_button).click()
        self.driver.find_element(*LoginPage.add_customer_button).click()

