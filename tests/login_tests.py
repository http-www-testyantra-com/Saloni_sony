from selenium import webdriver
from pages.login_page import *

def invoke_browser(func):
    def inner(url):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        func(driver)
        driver.close()
    return inner

@invoke_browser
def login_test(self):
    driver = webdriver.Firefox()
    log = LoginPage(driver)
    log.enterEmail("manisapattnaik506@gmail.com")


login_test("http://www.gmail.com")