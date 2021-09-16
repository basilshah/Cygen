import pytest
import time
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.DoctorAvailablity import availablity
from random import randint

class Test_005_DocAvailablity:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    ti = '16:00:00'

    @pytest.mark.regression
    def test_availablity(self,setup):
        self.datee = random_date()
        self.logger.info("******************Test_004_Reservation ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(7)
        self.logger.info("******************Login successful******************")
        self.logger.info("******************setting slote******************")
        self.avai = availablity(self.driver)
        self.avai.cilickOnAvailablity()
        self.avai.clickOnDoc()
        time.sleep(3)
        self.avai.setDate(self.datee)
        time.sleep(3)
        self.avai.setSlote(self.ti)
        self.logger.info("******************slot successful******************")
        self.driver.close()

def random_date():
    x= []
    x.append(str(randint(10,30)))
    x.append(str(0))
    x.append(str(randint(1,9)))
    x.append(str(randint(2021,3000)))
    num = ''.join(x)
    return num