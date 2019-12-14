import time

from p3.decorators import *

def login(driver):
    driver.find_element_by_xpath("//input[@type='email']").send_keys("manisapattnaik506@gmail.com",Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@type='password']").send_keys("9937756506",Keys.ENTER)

@invoke_browser
def login_only(driver):
    login(driver)