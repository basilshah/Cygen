from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def appointment_selection(uhid_no,type_of_appointment,driver):
    if type_of_appointment == "OPD" :
        indx = 2
    elif type_of_appointment == "LAB":
        indx = 3
    elif type_of_appointment == "diagno":
        indx = 4
    register_patient = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[2]/a/span')
    register_patient.click()
    time.sleep(2)

    # finding the book_appointment button
    ur = "//a[@href='/appointments/" + uhid_no + "/']"
    booking = driver.find_element_by_xpath(ur)
    booking.click()
    time.sleep(2)

    # selecting appoinmnet type as OPD or LAB or Other
    appoinment_type = driver.find_element_by_xpath('//*[@id="patienttype"]')
    Select(appoinment_type).select_by_index(indx)
    time.sleep(2)

# booking appointment OPD
def opd(uhid_no, appointment_date,driver):

    appointment_selection(uhid_no,'OPD',driver)
    #selecting the doctor
    doc = driver.find_element_by_xpath('//*[@id="doctorNameSpeciality"]')
    doc.click()
    time.sleep(2)
    doc.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
    driver.find_element_by_id('appointmentDate').send_keys(appointment_date)
    time.sleep(2)
    # finding all the time slots
    timeing = driver.find_elements_by_xpath('/html/body/div[1]/div/div/div/div/div/form/div[2]/input')

    # checking each time slot for the availablity
    for i in timeing:
        attb = i.get_attribute('value')
        click = i.get_attribute('class')
        if str(attb) >= '09:40' and str(click) == 'clickMe':
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
        print('Patient already have an appoinment')
        time.sleep(10)
        driver.__exit__()
        exit()
    pay_mode = driver.find_element_by_id('transaction_mode')
    # selecting the cash option
    Select(pay_mode).select_by_value('ff0001ab-af93-4477-b959-85a73bc91443')
    driver.find_element_by_xpath('//*[@id="opdbutton"]').click()
    time.sleep(2)
    driver.find_element_by_id('print').click()
    time.sleep(2)

# LAB
def lab(uhid_no, name_lab,driver):
    appointment_selection(uhid_no, 'LAB',driver)
    doc = driver.find_element_by_xpath('//*[@id="doctorNameSpeciality"]')
    doc.click()
    doc.send_keys(Keys.DOWN, Keys.DOWN, Keys.RETURN)
    submit = driver.find_element_by_xpath('//*[@id="submitDoctorSpeciality"]')
    submit.click()
    time.sleep(4)
    #waiting for the search box to load
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
    # selecting the options
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
    time.sleep(2)
    prin.location_once_scrolled_into_view
    prin.click()


def diagno(uhid_no,driver):
    appointment_selection(uhid_no, 'diagno', driver)
    doc = driver.find_element_by_xpath('//*[@id="doctorNameSpeciality"]')
    doc.click()
    time.sleep(2)
    doc.send_keys(Keys.DOWN, Keys.RETURN)
    driver.find_element_by_id('submitDoctorSpeciality').click()
    time.sleep(2)
    print('Diagnostic appointment booked successfully')

def reserv(name, num, appointment_date,driver):
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
    doc = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/ul/li[2]/div/div[1]/div/li/div/div[2]/div/select')
    Select(doc).select_by_index(2)
    driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div/ul/li[2]/div/div[2]/div/li/div/div[2]/div/div/input').send_keys(
        appointment_date)
    time.sleep(2)
    timeing = driver.find_elements_by_xpath(
        '//*[@id="root"]/div/div/div/div/ul/li[4]/div/li/div/div/div/div/div/button')
    for i in timeing:
        attb = i.get_attribute('value')
        if str(attb) >= '09:40:00':
            i.click()
            i.send_keys(Keys.ENTER)
            break
    driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/ul/li[6]/button/span[1]').click()
    time.sleep(2)
    print('Reservation was done successfully')
