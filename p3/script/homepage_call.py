from p3.pages.homepage import *
from p3.pages.login import *

@invoke_browser
def mail_test(driver):
    login("http://www.gmail.com")
    get_title("http://www.gmail.com")

