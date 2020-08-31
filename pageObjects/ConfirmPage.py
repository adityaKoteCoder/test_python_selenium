from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    confirm = (By.CSS_SELECTOR, "")
    location = (By.ID, "country")

    def getlocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def clickConfirm(self,driver):
        return self.driver.find_elements(*ConfirmPage.confirm)