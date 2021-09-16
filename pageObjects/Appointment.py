from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class set_Appointment:
    appointment_type_id = 'patienttype'
    doctor_id = 'doctorNameSpeciality'
    appointment_date_id = "appointmentDate"
    uhid_number = None
    submitbutton_id = "submitDoctorSpeciality"
    timing_xpath = '/html/body/div[1]/div/div/div/div/div/form/div[2]/input'
    view_details_xpath = '//*[@id="group"]'
    generatebill_id = "opdbutton"
    lab_searchbox_xpath = '//*[@id="root"]/div/div/div[2]/div/div[1]/div[3]/div/input'
    prescribeButon_xpath = '//*[@class="MuiButtonBase-root MuiIconButton-root"][@tabindex="0"]'
    prescribetest_xpath = '//*[@id="demo-controlled-open-select"]'
    testName_xpath = '//*[@type="checkbox"]'
    savebottun_xpath = "/html/body/div[3]/div[3]/div/header/div/button[2]/span[1]"
    lab_billbutton_xpath = '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[8]/a'
    lab_pyment_xpath ='//*[@id="root"]/div/div/div[3]/div[2]/div/div/div[3]/div/div[3]/button/span[1]'

    def __init__(self,driver):
        self.driver = driver



    def setAppointmentType(self,appointment_type):
        Select(self.driver.find_element_by_id(self.appointment_type_id)).select_by_visible_text(appointment_type)

    def setDoctor(self,doc_name):
        Select(self.driver.find_element_by_id(self.doctor_id)).select_by_visible_text(doc_name)

    def setDate(self,appointment_date):
        self.driver.find_element_by_id(self.appointment_date_id).send_keys(appointment_date)

    def setTimeSlote(self):
        timeing = self.driver.find_elements_by_xpath(self.timing_xpath)
        for i in timeing:
            attb = i.get_attribute('value')
            click = i.get_attribute('class')
            if str(attb) >= "09:40" and str(click) == 'clickMe':
                try:
                    i.click()
                    break
                except:
                    pass
        time.sleep(2)

    def setSubmit(self):
        self.driver.find_element_by_id(self.submitbutton_id).click()

    def setViewDetails(self):
        self.driver.find_element_by_xpath(self.view_details_xpath).click()

    def setGenerateBil(self):
        self.driver.find_element_by_id(self.generatebill_id).click()

    def setLabSearchbox(self,name):
        serch_box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,self.lab_searchbox_xpath )))
        serch_box.send_keys(name)

    def setprescribeText(self):
        buttons = self.driver.find_elements_by_xpath(self.prescribeButon_xpath)
        buttons[2].click()

    def setprescribeTest(self):
        self.driver.find_element_by_xpath(self.prescribetest_xpath).click()

    def setselectTest(self):
        tests = self.driver.find_elements_by_xpath(self.testName_xpath)
        time.sleep(4)

        for i in range(10):
            tests[i].click()

        tests[1].send_keys(Keys.ESCAPE)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.savebottun_xpath).click()

    def setBill(self):
        self.driver.find_element_by_xpath(self.lab_billbutton_xpath).click()

    def setMakePayment(self):
        self.driver.find_element_by_xpath(self.lab_pyment_xpath).click()



















