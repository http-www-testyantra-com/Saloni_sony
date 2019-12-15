import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# open the browser and maximizing window then entering the url
from vtiger.custom import Name_Exception


class Sc4(Name_Exception):

    def open_browser(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("http://localhost:8888/index.php?action=Login&module=Users")
        return driver

    def login(self, driver):
        try:
            driver.find_element_by_xpath("//input[@name='user_name']").send_keys("admin")
            driver.find_element_by_xpath("//input[@name='user_password']").send_keys("manager")
            driver.find_element_by_xpath("//input[@id='submitButton']").click()
        except Exception as e:
            print(Name_Exception(e))
            self.login(driver)
        print("logged in")

    def invoice(self, driver):
        try:
            more_element = driver.find_element_by_xpath("//a[text()='More']")
            act = ActionChains(driver)
            act.move_to_element(more_element).perform()
        except Exception as e:
            print(Name_Exception(e))
            self.invoice(driver)
    def submit(self,driver):
        driver.find_element_by_xpath("//a[@name='Invoice']").click()
        driver.find_element_by_xpath("//img[@alt='Last Viewed']").click()
        driver.find_element_by_xpath("//td[@class='trackerList small']/descendant::a[text()='Vtiger Single User Pack']").click()
        driver.find_element_by_xpath("//a[text()='Create Invoice']").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//input[@type='submit'])[1]").click()
        print(driver.switch_to_alert().text)

    def logout(self, driver):
        try:
            administartor = driver.find_element_by_xpath("(//td[@class='small'])[2]")
            ActionChains(driver).move_to_element(administartor).perform()
            driver.find_element_by_xpath("//a[text()='Sign Out']").click()
        except Exception as e:
            print(Name_Exception(e))
            self.logout(driver)

obj = Sc4("msg")
driver = obj.open_browser()
obj.login(driver)
obj.invoice(driver)
obj.submit(driver)
obj.logout(driver)