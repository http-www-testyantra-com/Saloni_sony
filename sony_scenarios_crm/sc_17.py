import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# open the browser and maximizing window then entering the url
from vtiger.custom import Name_Exception


class Sc2(Name_Exception):

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

    def move_more(self,driver):
        try:
            more_element = driver.find_element_by_xpath("//a[text()='More']")
            act = ActionChains(driver)
            act.move_to_element(more_element).perform()
        except Exception as e:
            print(Name_Exception(e))
            self.move_more(driver)
    def sales_order(self,driver):
        driver.find_element_by_xpath("//a[@name='Invoice']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//img[@alt='Last Viewed']").click()
        time.sleep(5)
        driver.find_element_by_xpath("//td[@class='trackerList small']/descendant::a[text()='Vtiger Single User Pack']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[text()='Create Sales Order']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//img[@title='Select']").click()
        time.sleep(4)
        windows = driver.window_handles
        print(windows)
        driver.switch_to_window(windows[1])
        time.sleep(4)
        driver.find_element_by_xpath("//a[text()='vtiger - 1000 units']").click()

    def log_out(self, driver):
        try:
            administartor = driver.find_element_by_xpath("(//td[@class='small'])[2]")
            ActionChains(driver).move_to_element(administartor).perform()
            driver.find_element_by_xpath("//a[text()='Sign Out']").click()
        except Exception as e:
            print(Name_Exception(e))
            self.log_out(driver)
        driver.close()

obj = Sc2("msg")
driver = obj.open_browser()
obj.login(driver)
obj.move_more(driver)
obj.sales_order(driver)
obj.log_out(driver)