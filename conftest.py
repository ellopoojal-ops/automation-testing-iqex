import pytest, logging
from selenium import webdriver
from pages.loginpage import LoginPage

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stg.iqex.co.uk/login")
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login("superadmin@iqex.com", "Admin@123")
    assert login_page.is_toast_message_displayed("Login Successfully")
    return driver

