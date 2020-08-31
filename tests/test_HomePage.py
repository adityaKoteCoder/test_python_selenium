import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver


# from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData[0])
        homepage.getemail().send_keys(getData[1])
        homepage.getPword().send_keys(getData[2])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData[3])

        homepage.getCheckBox2().click()
        # dropdown.select_by_value()
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text

        assert "success" in message


    @pytest.fixture(params=[("Aditya", "akstr17official@gmail.com", "1234", "Male"),("Striker", "akstr17obussiness@gmail.com", "1234", "Male"),("Toshaka", "akstr17gaming@gmail.com", "1234", "Female")])
    def getData(self,request):
        return request.param