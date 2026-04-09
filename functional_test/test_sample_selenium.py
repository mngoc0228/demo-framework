from PageObject.login_page import LoginPage
from pytest import mark
from selenium.webdriver.common.by import By
from utility.TestBase import TestBase
from selenium.webdriver.chrome.webdriver import WebDriver

class TestSampleSelenium(TestBase):
    @mark.login_test
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.get_email().send_keys("demo@evershop.io")
        login_page.get_password().send_keys("123456")
        login_page.get_button().click()
        # email = self.driver.find_element(By.XPATH,"//input[@type='email']")
        # email.send_keys("demo@evershop.io")
        # password = self.driver.find_element(By.XPATH,"//input[@type='password']")
        # password.send_keys("123456")
        # login_button = self.driver.find_element(By.XPATH,"//button[@type='submit']")

        dashboard_page = self.driver.find_element(By.XPATH,"//h1[contains(text(),'Dashboard')]")
        is_dashboard_available = dashboard_page.is_displayed()
        assert is_dashboard_available is True, "Dashboard page is not displayed"
