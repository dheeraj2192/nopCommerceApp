from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGeneration
import time


class Testcase_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logs=LogGeneration.loggen()

    def test_homePageTitle(self,setup):
        self.logs.info("*********** Testcase_001_Login ************")
        self.logs.info("*********** Verification of HomePage title started ************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title=self.driver.title


        if actual_title=="Your store. Login":
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle_Success.png") #. is to point current project directory
            self.driver.close()
            assert True
            self.logs.info("*********** Verification of HomePage title Finished and is matching ************")
        else:
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_homePageTitle_Failure.png")  # . is to point current project directory
            self.driver.close()
            assert False
            self.logs.info("*********** Verification of HomePage title Finished and is not matching ************")

    def test_login(self,setup):
        self.logs.info("*********** Verification of user login started ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        lp=LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        time.sleep(2)
        lp.clickLogin()
        actual_title=self.driver.title

        if actual_title=="Dashboard / nopCommerce administration":
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_login_Success.png")  # . is to point current project directory
            self.driver.close()
            assert True
            self.logs.info("*********** Verification of userlogin Finished and is able to login ************")
        else:
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_homePageTitle_Failure.png")  # . is to point current project directory
            self.driver.close()
            assert False
            self.logs.info("*********** Verification of userlogin Finished and is failing ************")


