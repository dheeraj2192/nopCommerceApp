import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import CustomerPage
from pageObjects.SearchCustomerPage import SearchCustomer

from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig
import time

class TestCase_005_SearchCustomerByName:
    app_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logs = LogGeneration.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logs.info("******* TestCase_005_SearchCustomerByName ********")
        self.logs.info("******* Start execution of SearchCustomerByName ********")
        self.driver = setup
        self.driver.get(self.app_url)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        self.logs.info("******* Login Successful ********")
        cp = CustomerPage(self.driver)
        cp.click_CustomerMenu()
        cp.click_CustomerSubMenu()
        self.logs.info("******* Click on Customers>Customer ********")

        sc = SearchCustomer(self.driver)
        sc.setFirstName("Victoria")
        sc.setLastName("Terces")
        sc.clickSearch()
        flg = sc.searchName("Victoria Terces")
        self.logs.info("******* search performed by name ********")
        time.sleep(3)

        print(flg)
        if flg.__eq__('True'):
            self.driver.close()
            assert True
            self.logs.info("****** Test Passed : Name found ********")
        else:
            self.driver.close()
            self.logs.info("****** Test Failed : Name not found ********")
            assert False


        self.logs.info("******* End execution of SearchCustomerByEmail ********")
        self.logs.info("******* End of TestCase_004_SearchCustomerByEmail ********")



