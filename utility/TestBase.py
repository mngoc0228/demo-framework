import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait 

@pytest.mark.usefixtures("setup")
class TestBase:
    def verify_visibility_of_element(self,web_element):
        wait = WebDriverWait(self.driver, timeout=15)
        wait.until(expected_conditions.visibility_of(web_element))
