
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By

class ReserveAppointment:
    reserveAppointmentTab_xpath = '//*[@id="exampleAccordion"]/li[10]/a/span'
    reserveButton_xpath ='//*[@id="root"]/div/div/div/div[1]/div[2]/a/span[1]'
    patientNameBox_xpath = '//*[@id="root"]/div/div/div/div/ul/li[1]/div/li/div[1]/div[2]/div/div/input'
    phnNum_xpath ='//*[@id="root"]/div/div/div/div/ul/li[1]/div/li/div[2]/div[2]/div/div/input'
    docSection_xpath ='//*[@id="root"]/div/div/div/div/ul/li[2]/div/div[1]/div/li/div/div[2]/div/select'
    appointmentDate_xapth ='//*[@id="root"]/div/div/div/div/ul/li[2]/div/div[2]/div/li/div/div[2]/div/div/input'
    timings_xpath = '//*[@id="root"]/div/div/div/div/ul/li[4]/div/li/div/div/div/div/div/button'
    sumbit_xpath = '//*[@id="root"]/div/div/div/div/ul/li[6]/button/span[1]'
    nametabe_xpath ='/html/body/div/div/div/div/div/div/div/div[2]/table/tbody'
    confirmTable_row_xpath = '/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody'
    bill_xpath ='//*[@id="group"]'
    generateButton_id = 'opdbutton'

    def __init__(self,driver):
        self.driver = driver

    def clickResrvationTab(self):
        self.driver.find_element_by_xpath(self.reserveAppointmentTab_xpath).click()

    def clickResrvationButton(self):
        self.driver.find_element_by_xpath(self.reserveButton_xpath).click()

    def setPatientName(self,name):
        self.driver.find_element_by_xpath(self.patientNameBox_xpath).send_keys(name)

    def setPhnNumber(self,number):
        self.driver.find_element_by_xpath(self.phnNum_xpath).send_keys(number)

    def setDoc(self):
        Select(self.driver.find_element_by_xpath(self.docSection_xpath)).select_by_index(2)

    def setDate(self,date):
        self.driver.find_element_by_xpath(self.appointmentDate_xapth).send_keys(date)

    def setTimeslote(self,tim_e):
        timeing = self.driver.find_elements_by_xpath(self.timings_xpath)
        for i in timeing:
            attb = i.get_attribute('value')
            if str(attb) >= tim_e:
                i.click()
                i.send_keys(Keys.ENTER)
                break

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.sumbit_xpath).click()

    def findName(self,name):
        tot = self.driver.find_elements_by_xpath(self.nametabe_xpath)
        for i in range(1, len(tot) + 1):
            name_xpath = '/html/body/div/div/div/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[1]'
            nameee = self.driver.find_element_by_xpath(name_xpath)
            namee = nameee.text
            if namee == name:
                time.sleep(2)
                tick_xpath = '/html/body/div/div/div/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[6]/button'
                element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,tick_xpath )))
                element.click()
                break
    def clickConfirmReserv(self,name):
        table_rows = self.driver.find_elements_by_xpath(self.confirmTable_row_xpath)
        for i in range(1, len(table_rows) + 1):
            time.sleep(1)
            name_xpath = '/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[2]'
            nameee = self.driver.find_element_by_xpath(name_xpath)
            namee = nameee.text

            if namee == name:
                confirm_xpath = '/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[4]/button'
                cli = self.driver.find_element_by_xpath(confirm_xpath)
                self.driver.execute_script("arguments[0].click();", cli)
                WebDriverWait(self.driver, 10).until(EC.alert_is_present())
                self.driver.switch_to.alert.accept()
                break

    def generateBill(self):
        self.driver.find_element_by_xpath(self.bill_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id(self.generateButton_id).click()


