import pytest
import time
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.ReserveAppointment import ReserveAppointment
from random import randint

class Test_004_Reservation:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    timing = "09:40:00"
    name = "Muhammed Basil Shah"
    number = "9876543210"
    nametabe_xpath = '/html/body/div/div/div/div/div/div/div/div[2]/table/tbody'

    @pytest.mark.regression
    def test_reservation(self,setup):
        self.app_date = random_date()
        self.logger.info("******************Test_004_Reservation ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(7)
        self.logger.info("******************Login successful******************")
        self.logger.info("******************String Reservation  ******************")
        self.res = ReserveAppointment(self.driver)
        self.res.clickResrvationTab()
        time.sleep(2)
        self.res.clickResrvationButton()
        self.res.setPatientName(self.name)
        self.res.setPhnNumber(self.number)
        self.res.setDoc()
        self.res.setDate(self.app_date)
        time.sleep(4)
        self.res.setTimeslote(self.timing)
        self.res.clickSubmit()
        self.logger.info("******************Reservation  successful******************")
        self.driver.close()

    @pytest.mark.regression
    def test_reservConfermation(self,setup):
        self.logger.info("******************Test_004_Reservation ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(7)
        self.logger.info("******************Login successfull******************")
        self.logger.info("******************Confirming Reservation******************")
        self.res = ReserveAppointment(self.driver)
        self.res.clickResrvationTab()
        time.sleep(2)
        self.res.findName(self.name)
        time.sleep(5)
        self.res.clickConfirmReserv(self.name)
        self.res.generateBill()
        self.logger.info("******************Confirming Reservation was Sucessfull******************")
        self.driver.close()

def random_date():
    x= []
    x.append(str(randint(10,30)))
    x.append(str(0))
    x.append(str(randint(1,9)))
    x.append(str(randint(2021,3000)))
    num = ''.join(x)
    return num
