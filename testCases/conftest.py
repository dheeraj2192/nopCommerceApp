import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.ie.service import Service


@pytest.fixture()
def setup(browser):
    if browser=="ie":
        s = Service('D:\\DHEERAJ\\SeleniumJAVAProject\\Drivers\\iedriver\\IEDriverServer.exe')
        driver = webdriver.Ie(service=s)

    elif browser=="edge":
        s = Service('D:\\DHEERAJ\\SeleniumJAVAProject\\Drivers\\edgedriver\\msedgedriver.exe')
        driver = webdriver.Edge(service=s)

    else:
        s = Service('D:\\DHEERAJ\\SeleniumJAVAProject\\Drivers\\chromedriver\\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
    return driver


def pytest_addoption(parser): # this will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): # this will return the browser value to setup method
    return request.config.getoption("--browser")

############################pytest HTML report####################

#It is hook for adding Environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name']='customer'
    config._metadata['Tester']='Dheeraj'

#It is hook for delete/modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

