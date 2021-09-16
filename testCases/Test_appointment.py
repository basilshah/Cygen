import pytest
import time
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.Appointment import set_Appointment
from random import randint

class Test_003_appointment:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    name = "muhammed basil shah"
    doc_name ="suhas reddy yarrabothu Consultant Pathologist"
    doc_name_diagno = "Himavanth Reddy Depa Consultant Pathologist"

    @pytest.mark.regression
    def test_LabAppointment(self,setup):
        self.logger.info("******************Test_003_LAB Appointment******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(7)
        self.logger.info("******************Login successful******************")

        self.logger.info("******************Starting LAB Appointment******************")

        self.lp.searching(self.name)
        time.sleep(4)
        self.appointment = set_Appointment(self.driver)
        self.appointment.setAppointmentType("Lab")
        self.appointment.setDoctor(self.doc_name)
        time.sleep(2)
        self.appointment.setSubmit()
        self.logger.info("******************Searching for appointed patient******************")
        self.appointment.setLabSearchbox("muhammed  basil shah")
        time.sleep(4)
        self.appointment.setprescribeText()
        time.sleep(2)
        self.appointment.setprescribeTest()
        time.sleep(2)
        self.appointment.setselectTest()
        time.sleep(2)
        self.logger.info("******************Selecting LAB Tests******************")
        self.appointment.setBill()
        time.sleep(2)
        self.appointment.setMakePayment()
        self.logger.info("******************making Payments******************")
        self.logger.info("******************Test Passed******************")
        self.driver.close()
        self.logger.info("******* Ending LAB test **********")

    @pytest.mark.regression
    def test_OpdAppointment(self,setup):
        self.app_date = random_date()
        self.logger.info("******************Test_003_OPD Appointment******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(7)
        self.logger.info("******************Login successful******************")

        self.logger.info("******************Starting OPD Appointment******************")

        self.lp.searching(self.name)
        time.sleep(4)
        self.appointment = set_Appointment(self.driver)
        self.appointment.setAppointmentType("OPD")
        self.appointment.setDoctor(self.doc_name)
        time.sleep(5)
        self.appointment.setDate(self.app_date)
        time.sleep(5)
        self.appointment.setTimeSlote()
        self.appointment.setSubmit()
        self.logger.info("******************OPD registration Done******************")
        self.driver.close()
        self.logger.info("******************Test Passed******************")

    @pytest.mark.regression
    def test_Diagnostic(self,setup):
        self.logger.info("******************Test_003_Diagnostic Appointment******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(7)
        self.logger.info("******************Login successful******************")

        self.logger.info("******************Starting Diagnostic Appointment******************")

        self.lp.searching(self.name)
        time.sleep(4)
        self.appointment = set_Appointment(self.driver)
        self.appointment.setAppointmentType("Diagnostic")
        self.appointment.setDoctor('Himavanth Reddy Depa Consultant Pathologist')
        time.sleep(2)
        self.appointment.setSubmit()
        self.logger.info("******************OPD registration Done******************")
        self.driver.close()
        self.logger.info("******************Test Passed******************")

def random_date():
    x= []
    x.append(str(randint(10,30)))
    x.append(str(0))
    x.append(str(randint(1,9)))
    x.append(str(randint(2021,3000)))
    num = ''.join(x)
    return num















