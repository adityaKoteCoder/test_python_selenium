import pytest
from selenium import webdriver
import time
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\\ADITYA\Selenium\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\ADITYA\Selenium\geckodriver.exe")

    elif browser_name == "ie":
        driver = webdriver.Ie(executable_path="E:\\ADITYA\Selenium\IEDriverServer.exe")

    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

