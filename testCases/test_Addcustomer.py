import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import CustomerPage

from utilities.customLogger import LogGeneration
from utilities.readProperties import ReadConfig
import time
import string
import random


class TestCase_003_Addcustomer:
    appURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logs=LogGeneration.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self,setup):
        self.logs.info("******* Start TestCase_003_Addcustomer ********** ")
        self.driver = setup
        self.driver.get(self.appURL)
        self.driver.maximize_window()
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logs.info("****** Login Successful *******")
        cp = CustomerPage(self.driver)
        cp.click_CustomerMenu()
        cp.click_CustomerSubMenu()
        time.sleep(3)
        cp.click_Addcustomerbtn()
        time.sleep(3)
        self.logs.info("*** Add Customer Page *********")
        self.driver.save_screenshot(".\\Screenshots\\"+"test_NewCustomerRegistration_Success.png")
        email =random_generator() + "@gmail.com"
        cp.setBusinessEmail(email)
        cp.setPassword("test")
        cp.setFirstName("Sam")
        cp.setLastName("GUI")
        cp.selectGender('Male')
        cp.setDOB('2/21/1992')
        cp.setCompanyName("XYZ Industries")
        cp.selectTaxExempt()
        cp.setNewsLetter('Test store 2')
        time.sleep(2)
        cp.setCustomerRoles('Guests')
        cp.selectVendorManager('Not a vendor')
        cp.setAdminComment('test123')
        cp.clickSave()
        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\"+'test_SaveCustomer_Success.png')

        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
        if 'The new customer has been added successfully' in self.msg:
            self.logs.info("********* Customer added successfully **********")
            self.driver.close()
            assert True
        else:
            self.logs.info("****** Customer creation failed ********")
            self.driver.close()
            assert False

        self.logs.info("********** End of TestCase_003_Addcustomer *******")


def random_generator(size=8,chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))