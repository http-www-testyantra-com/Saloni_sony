import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from datetime import datetime

# Current date time in local system
c_date = datetime.date(datetime.now())
c_date1 = str(c_date)
# open the browser and maximizing window then entering the url

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://yatra.com")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']").click()
time.sleep(2)
driver.find_element_by_xpath("(//p[@class='ac_cityname'])[3]").click()
time.sleep(2)
driver.find_element_by_xpath("(//p[@class='ac_cityname'])[5]").click()
driver.find_element_by_xpath("//input[@id='BE_flight_origin_date']").click()

driver.find_element_by_xpath("//td[@id="+''+c_date1+''+"]").click()
