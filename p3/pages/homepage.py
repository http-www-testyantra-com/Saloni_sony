import time

from p3.decorators import *


def get_title(driver):
    etitle = "Gmail"
    atitle = driver.title
    print(atitle)
    assert atitle == etitle,print("not in same page")
    print("in same page")

@invoke_browser
def inbox(driver):
    total_inbox=driver.find_element_by_xpath("//div[@class='bsU']").text
    print(total_inbox)

@invoke_browser
def header_text(driver):
    headers=driver.find_elements_by_xpath("//tr[@class='zA zE']/descendant::td[@id=':2z']/descendant::span[@class='bqe']").text
    for i in headers:
        print(i.text)

@invoke_browser
def check_box_click(driver):
    driver.find_element_by_xpath("//span[@role='checkbox']").click()