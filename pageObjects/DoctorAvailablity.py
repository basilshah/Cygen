
import time


class availablity:
    docAvailablity_xpath = '//*[@id="exampleAccordion"]/li[6]/a'
    docavailableCard_xpath = '//*[@id="Doctorreceptionisttable"]/tr[2]/td[10]/a'
    availableDate_xpath = '//*[@id="inputdate"]'
    slotes_xpath = '/html/body/div[1]/div/div/div[3]/input'

    def __init__(self,driver):
        self.driver = driver

    def cilickOnAvailablity(self):
        self.driver.find_element_by_xpath(self.docAvailablity_xpath).click()

    def clickOnDoc(self):
        self.driver.find_element_by_xpath(self.docavailableCard_xpath).click()

    def setDate(self,datee):
        self.driver.find_element_by_xpath(self.availableDate_xpath).send_keys(datee)

    def setSlote(self,ti):
        slots = self.driver.find_elements_by_xpath(self.slotes_xpath)
        for i in slots:
            time.sleep(1)
            tim = str(i.get_attribute('data-id'))
            cls = str(i.get_attribute('id'))
            if (ti == tim) and (cls == 'green'):
                i.click()
                time.sleep(3)
                self.driver.find_element_by_class_name("modal-body")
                self.driver.find_element_by_id('confirmblock').click()
                break






