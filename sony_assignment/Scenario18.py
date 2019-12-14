import time

import xlwt

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# open the browser and maximizing window then entering the url

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://bluestone.com")

# providing driver in action class means it will perform on that particular page and performing action class

act = ActionChains(driver)
coin = driver.find_element_by_xpath("//a[text()='Coins ']")
act.move_to_element(coin).perform()

# by using functional prgaraming persorming find element and clicking the element

click = lambda xpath,driver:driver.find_element_by_xpath(xpath).click()
click("(//span[text()='2 gram'])[1]",driver)


egram="2 gram 24 KT Gold Coin"
agram=driver.find_element_by_xpath("//h1[text()='2 gram 24 KT Gold Coin']").text

# comparing that it is equal or not by assert

assert egram==agram,print("it is not 2 gram")
print("it is 2gram")

#close browser

driver.close()