from selenium import webdriver
from time import sleep
import const

class DailyCheckBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://dailycheck.cornell.edu')
        sleep(0.5)
        dailycheck_btn = self.driver.find_element_by_xpath('//*[@id="main-article"]/div[2]/div[1]/div/p/a')
        dailycheck_btn.click()
        sleep(0.5)
        cornelluser_btn = self.driver.find_element_by_xpath('//*[@id="main-article"]/p/a[1]')
        cornelluser_btn.click()
        sleep(0.5)
        netid_btn = self.driver.find_element_by_xpath('//*[@id="netid"]')
        netid_btn.click()
        netid_btn.send_keys(const.netid)       #net-id goes here
        sleep(0.5)
        pass_btn = self.driver.find_element_by_xpath('//*[@id="password"]')
        pass_btn.click()
        pass_btn.send_keys(const.password)    #password goes here
        sleep(0.5)
        login = self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/div[3]/div/input')
        login.click()
        sleep(0.5)
        self.driver.get('https://dailycheck.cornell.edu/daily-checkin')

    def fakeoptions(self):
        continue_btn = self.driver.find_element_by_xpath('//*[@id="continue"]')
        continue_btn.click()
        first = self.driver.find_element_by_xpath('//*[@id="positivetestever-no"]')
        first.click()
        sleep(0.5)
        second = self.driver.find_element_by_xpath('//*[@id="covidsymptoms-no"]')
        second.click()
        sleep(0.5)
        third = self.driver.find_element_by_xpath('//*[@id="contactsymptoms-no"]')
        third.click()
        sleep(0.5)
        fourth = self.driver.find_element_by_xpath('//*[@id="exposure-no"]')
        fourth.click()
        sleep(0.5)
        finish_btn = self.driver.find_element_by_xpath('//*[@id="submit"]')
        finish_btn.click()
        sleep(0.5)
        confirm_btn =  self.driver.find_element_by_xpath('//*[@id="submit"]')
        confirm_btn.click()




