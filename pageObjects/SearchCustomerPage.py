from selenium.webdriver.common.by import By


class SearchCustomer:
    txtbox_email_id = 'SearchEmail'
    txtbox_fname_id = 'SearchFirstName'
    txtbox_lname_id = 'SearchLastName'
    btn_search_id = 'search-customers'
    tbl_searchresult_xpath = "//table[@id='customers-grid']"
    tbl_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    tbl_columns_xpath = "//table[@id='customers-grid']/tbody/tr[1]/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID,self.txtbox_email_id).clear()
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, self.txtbox_fname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_fname_id).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, self.txtbox_lname_id).clear()
        self.driver.find_element(By.ID, self.txtbox_lname_id).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element(By.ID,self.btn_search_id).click()

    def getRowCount(self):
        return len(self.driver.find_elements(By.XPATH, self.tbl_rows_xpath))

    def searchEmail(self,email):
        flag = False
        table = self.driver.find_element(By.XPATH,self.tbl_searchresult_xpath)
        for r in range(1, self.getRowCount()+1):
            emailresult = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+r.__str__()+"]/td[2]").text
            if emailresult == email:
                flag = True
                break
        return flag

    def searchName(self, name):
        rows = len(self.driver.find_elements(By.XPATH, self.tbl_rows_xpath))
        # cols = len(self.driver.find_element(By.XPATH,self.tbl_columns_xpath))
        flag = False
        for r in range(1, rows + 1):

            nameresult = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+r.__str__()+"]/td[3]").text
            if nameresult == name:
                flag = True
        return flag


