import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def setup(request):
        driver = webdriver.Chrome()
        driver.get("https://demo.evershop.io/admin/login")
        driver.implicitly_wait(50)
        request.cls.driver = driver
        yield
        driver.close()