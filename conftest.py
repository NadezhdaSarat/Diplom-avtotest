import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    driver.implicitly_wait(50)
    yield driver
    driver.quit()
