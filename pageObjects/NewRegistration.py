
from selenium.webdriver.support.select import Select


class Registration:
    register_patient_xpath = '//*[@id="exampleAccordion"]/li[2]/a/span'
    register_buttton_xpath = r'//div[@class="content-wrapper"]/div[1]/div[1]/div[1]/div[1]/div[1]/button'
    firstname_id = "patientfname"
    middlename_id = "patientmname"
    lastname_id = "patientlname"
    address_line1_id = "patientstreetname"
    address_line2_id = "patientstreetname2"
    city_id = "patientcity"
    country_id = "country"
    pincode_id = "patientzip"
    state_id = "state"
    contactnumber_id = "patientcontactnumber"
    username_id = "username"
    branch_id = "branchSelectionField"
    prooftype_id = "identityProofType"
    proofnum_id = "idProofNumber"
    gender_id = "patientgender"
    dob_id = "patientdob"
    bloodgroup_id = "patientbloodgroup"
    patienttype_id = "patient_type"
    reason_for_registation_id = "patientreason"
    createbutton_xpath = "/html/body/div[12]/div[11]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnRegisterPatient(self):
        self.driver.find_element_by_xpath(self.register_patient_xpath).click()

    def clickOnRegisterButton(self):
        self.driver.find_element_by_xpath(self.register_buttton_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.firstname_id).send_keys(fname)

    def setMiddleName(self, mname):
        self.driver.find_element_by_id(self.middlename_id).send_keys(mname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.lastname_id).send_keys(lname)

    def setAdress1(self, adress1):
        self.driver.find_element_by_id(self.address_line1_id).send_keys(adress1)

    def setAdress2(self, adress2):
        self.driver.find_element_by_id(self.address_line2_id).send_keys(adress2)

    def setCity(self, city):
        self.driver.find_element_by_id(self.city_id).send_keys(city)

    def setCountry(self, country):
        drp = Select(self.driver.find_element_by_id(self.country_id))
        drp.select_by_value(country)

    def setPinCode(self, pincode):
        self.driver.find_element_by_id(self.pincode_id).send_keys(pincode)

    def setState(self, state):
        drp = Select(self.driver.find_element_by_id(self.state_id))
        drp.select_by_value(state)

    def setPhnNumber(self, phn_number):
        self.driver.find_element_by_id(self.contactnumber_id).send_keys(phn_number)

    def setUsername(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def setBranch(self):
        Select(self.driver.find_element_by_id(self.branch_id)).select_by_index(1)

    def setIdProof(self, idproof):
        Select(self.driver.find_element_by_id(self.prooftype_id)).select_by_value(idproof)

    def setIDnumber(self, idnumber):
        self.driver.find_element_by_id(self.proofnum_id).send_keys(idnumber)

    def setDOB(self, dob):
        self.driver.find_element_by_id(self.dob_id).send_keys(dob)

    def setBloodGroup(self, bloodgroup):
        Select(self.driver.find_element_by_id(self.bloodgroup_id)).select_by_value(bloodgroup)

    def setPatientType(self, patient_type):
        self.driver.execute_script("window.scrollBy(0,600)", "")
        pat_type = self.driver.find_element_by_id(self.patienttype_id)
        Select(pat_type).select_by_value(patient_type)

    def setReasonForRegistration(self, reason):
        self.driver.find_element_by_id(self.reason_for_registation_id).send_keys(reason)

    def setClickOnCreate(self):
        self.driver.find_element_by_xpath(self.createbutton_xpath).click()

    def isCreatebuttonvisible(self):
        try:
            if self.driver.find_element_by_id(self.createbutton_xpath).is_enabled():
                return True
        except:
            return False
