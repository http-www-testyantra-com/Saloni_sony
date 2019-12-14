import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys


def invoke_browser(func):
    def inner(url):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        driver=func(driver)

    return inner

