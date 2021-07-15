from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
logging.basicConfig(filename='bot.log',format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%y/%m/%d %H:%M:%S', level=logging.INFO, filemode='w')

opt = Options()
opt.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe',options=opt)
wait = WebDriverWait(driver, 20)

#login
driver.get("http://training.cygendiagnostics.com/")
driver.find_element_by_id("inputEmail").send_keys('saikiran@129')
driver.find_element_by_id("inputPassword").send_keys('saikiran1999')
driver.find_element_by_id("loginsubmit").click()
logging.info('Logined successfully')
time.sleep(2)

#registation
def registration():
    driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[2]/a/span').click()
    time.sleep(2)
    driver.find_element_by_xpath(r'//div[@class="content-wrapper"]/div[1]/div[1]/div[1]/div[1]/div[1]/button').click()
    driver.find_element_by_id("patientfname").send_keys(creds["first_name"])
    driver.find_element_by_id("patientmname").send_keys(creds["middle_name"])
    driver.find_element_by_id("patientlname").send_keys(creds["last_name"])

    driver.find_element_by_id("patientstreetname").send_keys(creds["add_line_1"])
    driver.find_element_by_id("patientstreetname2").send_keys(creds["add_line_2"])
    driver.find_element_by_id("patientcity").send_keys(creds["city"])

    country = driver.find_element_by_id("country")
    Select(country).select_by_value(creds["country"])

    driver.find_element_by_id("patientzip").send_keys(creds["zip_code"])

    state = driver.find_element_by_id("state")
    Select(state).select_by_value(creds["state"])

    driver.find_element_by_id("patientcontactnumber").send_keys(creds["contact_no"])
    driver.find_element_by_id("username").send_keys(creds["username"])

    branch = driver.find_element_by_id("branchSelectionField")
    Select(branch).select_by_index(1)

    proof = driver.find_element_by_id("identityProofType")
    Select(proof).select_by_index(1)
    driver.find_element_by_id("idProofNumber").send_keys(creds["proof_no"])

    genter = driver.find_element_by_id("patientgender")
    Select(genter).select_by_index(1)

    driver.find_element_by_id("patientdob").send_keys(creds["dob"])

    blood_gp = driver.find_element_by_id("patientbloodgroup")
    Select(blood_gp).select_by_value(creds["blood"])

    pat_type = driver.find_element_by_id("patient_type")
    pat_type.location_once_scrolled_into_view
    Select(pat_type).select_by_value(creds["type"])
    driver.find_element_by_id("patientreason").send_keys(creds["reson"])
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[12]/div[11]/div/button[1]").click()
    time.sleep(2)
    driver.refresh()
    logging.info('Registration was successfull')


#booking appointment OPD
def opd(uhid_no,appointment_date):
    register_patient = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[2]/a/span')
    register_patient.click()
    time.sleep(2)
    ur = "//a[@href='/appointments/"+uhid_no+"/']"
    booking = driver.find_element_by_xpath(ur)
    booking.click()
    time.sleep(2)
    appoinment_type = driver.find_element_by_xpath('//*[@id="patienttype"]')
    Select(appoinment_type).select_by_index(2)
    doc = driver.find_element_by_xpath('//*[@id="doctorNameSpeciality"]')
    doc.click()
    time.sleep(2)
    doc.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
    driver.find_element_by_id('appointmentDate').send_keys(appointment_date)
    time.sleep(2)
    timeing = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/div/div/form/div[2]/input')
    for i in timeing:
        attb = i.get_attribute('value')
        click = i.get_attribute('class')
        if str(attb) >= '09:40' and str(click)=='clickMe':
            try:
                i.click()
                break
            except:
                pass
    time.sleep(2)
    driver.find_element_by_id('submitDoctorSpeciality').click()
    time.sleep(2)
    # billing OP
    try:

        driver.find_element_by_xpath('//*[@id="group"]').click()
        time.sleep(2)
    except:
        driver.save_screenshot("error.png")
        logging.info('Patient already have an appoinment')
        time.sleep(10)
        driver.__exit__()
        exit()
    pay_mode = driver.find_element_by_id('transaction_mode')
    Select(pay_mode).select_by_value('ff0001ab-af93-4477-b959-85a73bc91443')
    driver.find_element_by_xpath('//*[@id="opdbutton"]').click()
    time.sleep(2)
    driver.find_element_by_id('print').click()
    time.sleep(2)
    logging.info('OPD appointment booked successfully')


#booking appointment lab
def lab(uhid_no,name_lab):
    register_patient = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[2]/a/span')
    register_patient.click()
    time.sleep(2)
    ur = "//a[@href='/appointments/" + uhid_no + "/']"
    booking = driver.find_element_by_xpath(ur)
    booking.click()
    time.sleep(2)
    appoinment_type = driver.find_element_by_xpath('//*[@id="patienttype"]')
    Select(appoinment_type).select_by_index(3)
    time.sleep(2)
    doc = driver.find_element_by_xpath('//*[@id="doctorNameSpeciality"]')
    doc.click()
    doc.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
    submit = driver.find_element_by_xpath('//*[@id="submitDoctorSpeciality"]')
    submit.click()
    time.sleep(4)
    serch_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div[3]/div/input')))
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div[3]/div/input').send_keys(name_lab)
    time.sleep(2)
    buttons = driver.find_elements_by_xpath('//*[@class="MuiButtonBase-root MuiIconButton-root"][@tabindex="0"]')
    buttons[2].click()
    time.sleep(2)
    x = driver.find_element_by_xpath('//*[@id="demo-controlled-open-select"]')
    x.click()
    time.sleep(2)
    tests = driver.find_elements_by_xpath('//*[@type="checkbox"]')
    tests[1].click()
    tests[3].click()
    tests[5].click()
    tests[6].click()
    tests[7].click()
    tests[23].location_once_scrolled_into_view
    tests[23].click()
    tests[23].send_keys(Keys.ESCAPE)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/header/div/button[2]/span[1]').click()
    time.sleep(2)
    buttons = driver.find_elements_by_xpath(
        '//*[@class="MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary"]')
    buttons[2].click()
    time.sleep(2)
    discount = driver.find_element_by_id('discountAmount')
    discount.location_once_scrolled_into_view
    discount.send_keys('200')
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div/div/div[3]/div/div[3]/button').click()
    time.sleep(2)
    prin = driver.find_element_by_id('print')
    prin.location_once_scrolled_into_view
    prin.click()
    logging.info('LAB appointment booked successfully')


def diagno(uhid_no):
    register_patient = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[2]/a/span')
    register_patient.click()
    time.sleep(2)
    ur = "//a[@href='/appointments/" + uhid_no + "/']"
    booking = driver.find_element_by_xpath(ur)
    booking.click()
    time.sleep(2)
    appoinment_type = driver.find_element_by_xpath('//*[@id="patienttype"]')
    Select(appoinment_type).select_by_index(4)
    doc = driver.find_element_by_xpath('//*[@id="doctorNameSpeciality"]')
    doc.click()
    time.sleep(2)
    doc.send_keys(Keys.DOWN, Keys.RETURN)
    driver.find_element_by_id('submitDoctorSpeciality').click()
    time.sleep(2)
    logging.info('Diagnostic appointment booked successfully')






# reservation
def reserv(name ,num,appointment_date ):
    reserve_app = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[10]/a/span')
    reserve_app.click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/a/span[1]').click()
    time.sleep(2)
    name_box = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/ul/li[1]/div/li/div[1]/div[2]/div/div/input')
    name_box.send_keys(name)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/ul/li[1]/div/li/div[2]/div[2]/div/div/input').send_keys(num)
    doc = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/ul/li[2]/div/div[1]/div/li/div/div[2]/div/select')
    Select(doc).select_by_index(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/ul/li[2]/div/div[2]/div/li/div/div[2]/div/div/input').send_keys(appointment_date)
    time.sleep(2)
    timeing = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/ul/li[4]/div/li/div/div/div/div/div/button')
    for i in timeing:
        attb = i.get_attribute('value')
        if str(attb) >= '09:40:00':
            i.click()
            i.send_keys(Keys.ENTER)
            break
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/ul/li[6]/button/span[1]').click()
    time.sleep(2)
    logging.info('Reservation was done successfully')

#confirm reservation
def confi(name):
    reserve_app = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[10]/a/span')
    reserve_app.click()
    time.sleep(5)

    tot = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div/div/div[2]/table/tbody')
    tot_num = len(tot)
    for i in range(1,tot_num+1):
        name_xpath = '/html/body/div/div/div/div/div/div/div/div[2]/table/tbody['+str(i)+']/tr/td[1]'
        nameee = driver.find_element_by_xpath(name_xpath)
        namee = nameee.text
        if namee == name:
            time.sleep(2)
            tick_xpath ='/html/body/div/div/div/div/div/div/div/div[2]/table/tbody['+str(i)+']/tr/td[6]/button'
            driver.find_element_by_xpath(tick_xpath).click()
    time.sleep(5)
    tot = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody')
    tot_num = len(tot)
    print(tot_num)
    for i in range(1,tot_num+1):
        name_xpath = '/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody['+str(i)+']/tr/td[2]'
        nameee = driver.find_element_by_xpath(name_xpath)
        namee = nameee.text

        if namee == name:
            confirm_xpath ='/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody['+str(i)+']/tr/td[4]/button'
            cli = driver.find_element_by_xpath(confirm_xpath)
            driver.execute_script("arguments[0].click();",cli)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="group"]').click()
    time.sleep(2)
    pay_mode = driver.find_element_by_id('transaction_mode')
    Select(pay_mode).select_by_value('ff0001ab-af93-4477-b959-85a73bc91443')
    driver.find_element_by_xpath('//*[@id="opdbutton"]').click()
    time.sleep(2)
    driver.find_element_by_id('print').click()
    time.sleep(2)
    logging.info('Reservation was confirmed')



#doc availability
def doc_avai(appointment_date,ti):
    driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[6]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="Doctorreceptionisttable"]/tr[2]/td[10]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="inputdate"]').send_keys(appointment_date)
    time.sleep(7)
    slots = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[3]/input')
    for i in slots:
        time.sleep(1)
        tim = str(i.get_attribute('data-id'))
        cls = str(i.get_attribute('id'))
        if (ti == tim) and (cls == 'green'):
            i.click()
            time.sleep(2)
            driver.find_element_by_id('confirmblock').click()
            logging.info('Doc avalilablity slot was edited')
            exit()
    driver.save_screenshot("doc_availablity.png")
    logging.info('not able to edit the slot please see the screenshot')




creds = {"first_name":"badhshah",
         "middle_name":"",
         "last_name":"AB",
         "add_line_1":"House no. 45 second floor, 5th cross",
         "add_line_2":"Banaswadi, Bangalore, KA 560043.",
         "city":"Bangalore",
         "country":"India",
         "zip_code":"123456",
         "state":"Kerala",
         "contact_no":"9995989129",
         "username":"bad",
         "proof_no":"12345678910",
         "dob":"27072000",
         "blood":"O+",
         "type":"LAB",
         "reson":"Fever"
         }



#for searching the names in lab please add 2 space between first name and middle name, also 3 spaces between first name and last name.

appointment_date = 22092021
uhid_no ='CHRL-00-00000073'
name ='hafiz ashraf Shah'
name_lab ="hafiz  ashraf Shah"
num ='9995989127'
ti ='09:20:00'

