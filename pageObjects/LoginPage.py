from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    search_box_id = "myInput"
    table_xpath = '//*[@id="patienttableInReceptionistregistration"]/tr[@style="display: table-row;"]/td[1]'
    textbox_username_id ="inputEmail"
    textbox_password_id ="inputPassword"
    button_login_id = "loginsubmit"
    button_logout_xpath = '//*[@id="mainNav"]/div/ul[3]/li/a'

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(30)


    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def ClickLogout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

    def searching(self,name):
        serch_box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, self.search_box_id)))
        serch_box.send_keys(name)
        uhid_number = self.driver.find_element_by_xpath(self.table_xpath).text
        url = "//a[@href='/appointments/" + uhid_number + "/']"
        self.driver.find_element_by_xpath(url).click()