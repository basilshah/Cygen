from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def reserv(name, num, appointment_date,driver):
    reserve_app = driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[10]/a/span')
    reserve_app.click()
    time.sleep(2)
    # clicking reserve appoinment button
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
    time.sleep(5)
    print('Reservation was done successfully')
    tot = driver.find_elements_by_xpath('/html/body/div/div/div/div/div/div/div/div[2]/table/tbody')
    tot_num = len(tot)
    # finding the button
    for i in range(1, tot_num + 1):
        name_xpath = '/html/body/div/div/div/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[1]'
        nameee = driver.find_element_by_xpath(name_xpath)
        namee = nameee.text
        if namee == name:
            time.sleep(2)
            tick_xpath = '/html/body/div/div/div/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[6]/button'
            driver.find_element_by_xpath(tick_xpath).click()
    time.sleep(5)
    tot = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody')
    tot_num = len(tot)
    for i in range(1, tot_num + 1):
        name_xpath = '/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody[' + str(i) + ']/tr/td[2]'
        nameee = driver.find_element_by_xpath(name_xpath)
        namee = nameee.text

        if namee == name:
            confirm_xpath = '/html/body/div[2]/div[3]/div/div/div/div/div[2]/table/tbody[' + str(
                i) + ']/tr/td[4]/button'
            cli = driver.find_element_by_xpath(confirm_xpath)
            driver.execute_script("arguments[0].click();", cli)

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
    print('Reservation was confirmed')
    driver.__exit__()

# doc availability
def doc_avai(appointment_date, ti ,driver):
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
            print('Doc avalilablity slot was edited')
            exit()
    driver.save_screenshot("doc_availablity.png")
    print('not able to edit the slot please see the screenshot')