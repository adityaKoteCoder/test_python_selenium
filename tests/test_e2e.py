import time

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        # log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItem()
        # log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            # log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
        #1
        checkIns = CheckOutPage.getcheckIn(self)
        checkIns.click()

        #2
        confirmPage = CheckOutPage.checkOutItems(self)

        # log.info("Entering country name as ind")
        locationin = ConfirmPage.getlocation(self)
        locationin.send_keys("ind")
        # self.driver.find_element_by_id("country").send_keys("ind")
        time.sleep(7)
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        # log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)

