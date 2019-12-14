from base.common import *

class LoginPage(Selenium_Driver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email_field = "email"
    _password_field = "password"

    def enterEmail(self, email):
        return self.getElement("xpath").sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def login(self, email="", password=""):
        # self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
