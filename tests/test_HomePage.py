import pytest
from selenium.webdriver.support.select import Select
from selenium import webdriver


from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        homepage = HomePage(self.driver)
        homepage.getName().send_keys("Rahul")
        homepage.getemail().send_keys("akstr17official@gmail.com")
        homepage.getPword().send_keys("akote")
        homepage.getCheckBox("exampleCheck1").click()
        sel = Select(homepage.getGender())
        sel.select_by_visible_text("Female")
        homepage.getCheckBox2().click()
        # dropdown.select_by_value()
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text

        assert "success" in message


