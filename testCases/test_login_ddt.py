from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
from utilities import XLUtils
import time

import pytest

class Testcase_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logs=LogGeneration.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logs.info("*********** Starting execution Testcase_002_DDT_Login ************")
        self.logs.info("*********** Verification of user login started ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp=LoginPage(self.driver)
        rows=XLUtils.rowCount(self.path,"Sheet1")
        loginStatus=[]

        for r in range(2,rows+1):
            self.username=XLUtils.readExcel(self.path,"Sheet1",r,1)
            self.password=XLUtils.readExcel(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readExcel(self.path,"Sheet1",r,3)

            lp.setUserName(self.username)
            lp.setPassword(self.password)
            time.sleep(2)
            lp.clickLogin()
            actual_title=self.driver.title

            if actual_title == "Dashboard / nopCommerce administration":
                if self.exp == 'Pass':
                    self.logs.info("************** Test Passed *****************")
                    loginStatus.append("Pass")
                    lp.clickLogout()
                elif self.exp == "Fail":
                    self.logs.info("************** Test Failed *****************")
                    loginStatus.append("Fail")
                    lp.clickLogout()
            elif actual_title != "Dashboard / nopCommerce administration":
                if self.exp == 'Fail':
                    self.logs.info("************** Test Passed *****************")
                    loginStatus.append("Pass")

                elif self.exp == 'Pass':
                    self.logs.info("************** Test Failed *****************")
                    loginStatus.append("Fail")

        self.driver.close()

        if "Fail" not in loginStatus:
            self.logs.info("************** Testcase_002_DDT_Login -  Passed *****************")

            assert True
        else:
            self.logs.info("************** Testcase_002_DDT_Login -  Fail *****************")

            assert False

        self.logs.info("************** End of Testcase_002_DDT_Login *****************")







