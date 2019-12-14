import time

from p3.decorators import *

@invoke_browser
def logout(driver):
    driver = webdriver.Firefox()
    driver.find_element_by_xpath("//span[@class='gb_Ia gbii']").click()
    driver.find_element_by_xpath("//a[text()='Sign out']").click()