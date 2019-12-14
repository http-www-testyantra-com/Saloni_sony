import time

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver import ActionChains
from exception_handling.custon_exception import NameException as ne

def open_browser():
    global driver
    browser = input("enter browser")
    try:
        if browser == "Chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
    except Exception as e:
        print(e)
        raise ne
    finally:
        open_browser()
    # finally:
    #     print("open browser successfully")
    #     driver.get("https://flipkart.com")
    #     driver.maximize_window()

# def home_page():
#     try:
#         driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
#     except Exception as e:
#         print(e)
#     finally:
#         print("successfully clicked")
#
# def click():
#     try:
#         time.sleep(4)
#         driver.find_element_by_xpath("(//a[text()='VIEW ALL'])[1]").click()
#     except Exception as e:
#         print(e)
#         print("click intercepted")
#         driver.back()
#
#
# def move_to_element():
#     act = ActionChains(driver)
#     try:
#         elements = driver.find_element_by_xpath("//span[text()='Electronics']")
#         act.move_to_element(elements).perform()
#         time.sleep(3)
#         driver.find_element_by_xpath("(//a[text()='Mi'])[1]").click()
#     except Exception as e:
#         print(e)
#         print("done")
#
# def switch_alert():
#     try:
#         driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']")
#         alert = driver.switch_to_alert()
#         alert.dismiss()
#     except Exception as e:
#         print(e)
#         print("no such alert pop-up")
#
#
#




open_browser()
# home_page()
# time.sleep(5)
# click()
# time.sleep(5)
# move_to_element()
# switch_alert()