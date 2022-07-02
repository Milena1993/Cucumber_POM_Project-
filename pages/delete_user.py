from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DeleteUser:
    delete_button = (By.XPATH,'//button[@ng-click="deleteCust(cust)"]')
    table = (By.CSS_SELECTOR,  '.table > tbody > tr')

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def delete_customer(self):
        self.driver.find_element(*DeleteUser.delete_button).click()

    def table_existing_check(self):
        try:
            self.driver.find_element(*DeleteUser.table)
        except NoSuchElementException:
            return False
        return True



