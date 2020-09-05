import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver


# from TestData.HomePageData import HomePageData
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        # log.info("Name:"+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getPword().send_keys(getData["password"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.getCheckBox2().click()
        # dropdown.select_by_value()
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text

        assert ("success" in message)
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self,request):
        return request.param