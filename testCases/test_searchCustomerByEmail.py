import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import CustomerPage
from pageObjects.SearchCustomerPage import SearchCustomer

from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig
import time

class TestCase_004_SearchCustomerByEmail:
    app_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logs = LogGeneration.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logs.info("******* TestCase_004_SearchCustomerByEmail ********")
        self.logs.info("******* Start execution of SearchCustomerByEmail ********")
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
        sc.setEmail("victoria_victoria@nopCommerce.com")
        sc.clickSearch()
        self.logs.info("******* search performed by email ********")
        time.sleep(3)
        flg = sc.searchEmail("victoria_victoria@nopCommerce.com")
        print(flg)
        if flg.__eq__('True'):
            self.driver.close()
            assert True
            self.logs.info("****** Test Passed : Email found ********")
        else:
            self.driver.close()
            self.logs.info("****** Test Failed : Email not found ********")
            assert False


        self.logs.info("******* End execution of SearchCustomerByEmail ********")
        self.logs.info("******* End of TestCase_004_SearchCustomerByEmail ********")



