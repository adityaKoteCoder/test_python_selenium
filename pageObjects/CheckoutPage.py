from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkIn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")


    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getcheckIn(self):
        return self.driver.find_element(*CheckOutPage.checkIn)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage








