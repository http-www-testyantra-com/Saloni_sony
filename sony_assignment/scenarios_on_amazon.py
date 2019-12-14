import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://www.amazon.com")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//input[@class='a-button-input']").click()
drop_down = driver.find_element_by_xpath("//select[@id='searchDropdownBox']")
time.sleep(2)
drop_down.click()
sel = Select(drop_down)
sel.select_by_index(1)
