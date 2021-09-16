import pytest
import string
import time
import random
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.NewRegistration import Registration


class Test_002_NewReg:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_newRegistration(self,setup):
        self.creds = {"first_name": "manu",
         "middle_name": "",
         "last_name": "babu",
         "add_line_1": "House no. 45 second floor, 5th cross",
         "add_line_2": "Banaswadi, Bangalore, KA 560043.",
         "city": "Bangalore",
         "country": "India",
         "zip_code": "123456",
         "state": "Kerala",
         "contact_no": "9955589129",
         "proof_no": "12345678910",
         "dob": "27072000",
         "blood": "O+",
         "type": "LAB",
         "reson": "Fever"
         }
        self.logger.info("******************Test_003_NewRegistration******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(4)
        self.logger.info("******************Login successful******************")


        self.logger.info("******************Starting Registration******************")

        self.new_reg = Registration(self.driver)
        self.new_reg.clickOnRegisterPatient()
        time.sleep(4)

        self.new_reg.clickOnRegisterButton()
        time.sleep(4)

        self.logger.info("******************Entering the details******************")

        self.user_name = random_generator()
        self.fname = random_generator()
        self.lname = random_generator()
        self.new_reg.setFirstName(self.fname)
        self.new_reg.setMiddleName(self.creds["middle_name"])
        self.new_reg.setLastName(self.lname)
        self.new_reg.setAdress1(self.creds["add_line_1"])
        self.new_reg.setAdress2(self.creds["add_line_2"])
        self.new_reg.setCity(self.creds["city"])
        self.new_reg.setCountry(self.creds["country"])
        self.new_reg.setPinCode(self.creds["zip_code"])
        self.new_reg.setState(self.creds["state"])
        self.new_reg.setPhnNumber(self.creds["contact_no"])
        self.new_reg.setUsername(self.user_name)
        self.new_reg.setBranch()
        self.new_reg.setIdProof("adhaar")
        self.new_reg.setIDnumber(self.creds["proof_no"])
        self.new_reg.setDOB(self.creds["dob"])
        self.new_reg.setBloodGroup(self.creds["blood"])
        self.new_reg.setPatientType(self.creds["type"])
        self.new_reg.setReasonForRegistration(self.creds["reson"])
        self.new_reg.setClickOnCreate()
        time.sleep(5)

        self.logger.info("************* Saving customer info **********")

        self.logger.info("************* Validating **********")
        if self.new_reg.isCreatebuttonvisible() :
            self.logger.error("********* Test Failed ************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            assert False
        else:
            assert True
            self.logger.error("*********  Test Passed ************")

        self.driver.close()
        self.logger.info("******* Ending Registration test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





