from pytest import mark
from selenium.webdriver.common.by import By
from utility.TestBase import TestBase
from selenium.webdriver.chrome.webdriver import WebDriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@type='email']")
    password = (By.XPATH,"//input[@type='password']")
    login_button = (By.XPATH,"//button[@type='submit']")
    toast_error_msg = (By.XPATH,"//div[@class='Toastify__toast Toastify__toast--error']")

    def get_email(self):
        return self.driver.find_element(*LoginPage.email)
    
    def get_password(self):
        return self.driver.find_element(*LoginPage.password)
    
    def get_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_toast_error_msg(self):
        return self.driver.find_element(*LoginPage.toast_error_msg)