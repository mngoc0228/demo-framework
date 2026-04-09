import pytest
from PageObject.login_page import LoginPage
from PageObject.home_page import HomePage
from pytest import mark
from selenium.webdriver.common.by import By
from utility.TestBase import TestBase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestSampleSelenium (TestBase):
    @pytest.mark.login_test
    @pytest.mark.smoke
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.get_email().send_keys("ademo@evershop.ioa")
        login_page.get_password().send_keys("123456a")
        login_page.get_button().click()
        error_msg = self.verify_visibility_of_element(login_page.get_toast_error_msg())
        is_toast_error_msg = login_page.get_toast_error_msg().is_displayed()
        assert  is_toast_error_msg is True, "Error msg is not displayed"
