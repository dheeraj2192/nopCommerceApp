from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CustomerPage:

    menuItm_customers_xpath = "(//p[contains(text(),'Customers')])[1]"
    submenuItm_customers_xpath = "(//p[contains(text(),'Customers')])[2]"
    btn_addnewCust_xpath = "//a[@class='btn btn-primary']/i"

    txtbox_email_id = "Email"
    txtbox_password_id = "Password"
    txtbox_firstname_id = 'FirstName'
    txtbox_lastname_id = 'LastName'
    rdbtn_gendermale_id='Gender_Male'
    rdbtn_genderfemale_id = 'Gender_Female'
    txtbox_dob_id = 'DateOfBirth'
    txtbox_company_id = 'Company'
    chkbox_taxexempt_id = 'IsTaxExempt'
    lstbox_newsletter_xpath = "//input[@class='k-input k-readonly']"
    lstboxopt_urstorename_xpath = "//li[@class='k-item'][contains(text(),'Your store name')]"
    lstboxopt_teststore2_xpath = "//li[@class='k-item'][contains(text(),'Test store 2')]"
    lstbox_custrole_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    lstboxopt_registered_xpath = "//li[contains(text(),'Registered')]"
    lstboxopt_administrator_xpath = "//li[contains(text(),'Administrators')]"
    lstboxopt_forummoderator_xpath = "//li[contains(text(),'Forum Moderators')]"
    lstboxopt_vendors_xpath = "//li[contains(text(),'Vendors')]"
    lstboxopt_guests_xpath = "//li[contains(text(),'Guests')]"
    lstboxopt_registereddel_xpath = "(//div[@class='k-multiselect-wrap k-floatwrap']//span)[7]"
    drpdown_mgrvendor_id = 'VendorId'
    txtbox_admincomment_id = 'AdminComment'
    btn_save_xpath = "(//div[@class='content-header clearfix']//button)[1]"

    def __init__(self,driver):
        self.driver = driver

    def click_CustomerMenu(self):
        self.driver.find_element(By.XPATH,self.menuItm_customers_xpath).click()

    def click_CustomerSubMenu(self):
        self.driver.find_element(By.XPATH,self.submenuItm_customers_xpath).click()

    def click_Addcustomerbtn(self):
        self.driver.find_element(By.XPATH,self.btn_addnewCust_xpath).click()

    def setBusinessEmail(self,email):
        self.driver.find_element(By.ID,self.txtbox_email_id).clear()
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txtbox_password_id).clear()
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.ID,self.txtbox_firstname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_firstname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtbox_lastname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_lastname_id).send_keys(lastname)

    def selectGender(self, gender):
        if gender == 'male':
            self.driver.find_element(By.ID, self.rdbtn_gendermale_id).click()
        elif gender == 'female':
            self.driver.find_element(By.ID, self.rdbtn_genderfemale_id).click()
        else:
            self.driver.find_element(By.ID, self.rdbtn_gendermale_id).click()

    def setDOB(self, dob):
        self.driver.find_element(By.ID, self.txtbox_dob_id).clear()
        self.driver.find_element(By.ID, self.txtbox_dob_id).send_keys(dob)

    def setCompanyName(self, companyname):
        self.driver.find_element(By.ID, self.txtbox_company_id).clear()
        self.driver.find_element(By.ID, self.txtbox_company_id).send_keys(companyname)

    def selectTaxExempt(self):
        self.driver.find_element(By.ID, self.chkbox_taxexempt_id).click()

    def setNewsLetter(self, newsletter):
        self.driver.find_element(By.XPATH, self.lstbox_newsletter_xpath).click()
        if newsletter == 'Your store name':
            value = self.driver.find_element(By.XPATH,self.lstboxopt_urstorename_xpath)
            self.driver.execute_script("arguments[0].click();",value)
        elif newsletter == 'Test store 2':
            value = self.driver.find_element(By.XPATH, self.lstboxopt_teststore2_xpath)
            self.driver.execute_script("arguments[0].click();", value)
        else:
            value = self.driver.find_element(By.XPATH, self.lstboxopt_urstorename_xpath)
            self.driver.execute_script("arguments[0].click();", value)

    def setCustomerRoles(self, customerrole):

        if customerrole == 'Guests':
            self.driver.find_element(By.XPATH,self.lstboxopt_registereddel_xpath).click()
            self.driver.find_element(By.XPATH, self.lstbox_custrole_xpath).click()
            value = self.driver.find_element(By.XPATH,self.lstboxopt_guests_xpath)
            self.driver.execute_script("arguments[0].click();",value)
        elif customerrole == 'Administrators':
            self.driver.find_element(By.XPATH, self.lstbox_custrole_xpath).click()
            value = self.driver.find_element(By.XPATH, self.lstboxopt_administrator_xpath)
            self.driver.execute_script("arguments[0].click();", value)
        elif customerrole == 'Forum Moderators':
            self.driver.find_element(By.XPATH, self.lstbox_custrole_xpath).click()
            value = self.driver.find_element(By.XPATH, self.lstboxopt_forummoderator_xpath)
            self.driver.execute_script("arguments[0].click();", value)
        elif customerrole == 'Vendors':
            self.driver.find_element(By.XPATH, self.lstbox_custrole_xpath).click()
            value = self.driver.find_element(By.XPATH, self.lstboxopt_vendors_xpath)
            self.driver.execute_script("arguments[0].click();", value)
        else:
            self.driver.find_element(By.XPATH, self.lstboxopt_registereddel_xpath).click()
            self.driver.find_element(By.XPATH, self.lstbox_custrole_xpath).click()
            self.driver.find_element(By.XPATH, self.lstboxopt_registered_xpath).click()

    def selectVendorManager(self,vendormgr):
        element=self.driver.find_element(By.ID, self.drpdown_mgrvendor_id)
        drpdown=Select(element)
        drpdown.select_by_visible_text(vendormgr)

    def setAdminComment(self,comment):
        self.driver.find_element(By.ID,self.txtbox_admincomment_id).send_keys(comment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()
