from selenium.webdriver.support.select import Select
import time

def registration(creds,driver):
    # clicking the register button
    driver.find_element_by_xpath('//*[@id="exampleAccordion"]/li[2]/a/span').click()
    time.sleep(2)
    #filling the details
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
    driver.__exit__()

