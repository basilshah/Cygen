from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from registration import registration
from appointments import *
from reservation import *

#settingup webdriver
opt = Options()
opt.add_argument('start-maximized')
driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe', options=opt)
wait = WebDriverWait(driver, 20)

# loging into the site
driver.get("http://training.cygendiagnostics.com/")
driver.find_element_by_id("inputEmail").send_keys('saikiran@129')
driver.find_element_by_id("inputPassword").send_keys('saikiran1999')
driver.find_element_by_id("loginsubmit").click()
time.sleep(2)

# enter the details for the new registration
creds = {"first_name": "manu",
         "middle_name": "",
         "last_name": "babu",
         "add_line_1": "House no. 45 second floor, 5th cross",
         "add_line_2": "Banaswadi, Bangalore, KA 560043.",
         "city": "Bangalore",
         "country": "India",
         "zip_code": "123456",
         "state": "Kerala",
         "contact_no": "9955589129",
         "username": "manubabu",
         "proof_no": "12345678910",
         "dob": "27072000",
         "blood": "O+",
         "type": "LAB",
         "reson": "Fever"
         }

# appintment date for the OPD or reservation ---
appointment_date = 28102021

# UHID NO of patient
uhid_no = 'CHRL-00-00000076'

#name of patient
name = 'Darya N'

#name of patient for the LAB -- please add 2 space between first name and middle name, also 3 spaces between first name and last name.
name_lab = "Darya   N"
phn_number = '9059216061'
#time
ti = '09:20:00'



