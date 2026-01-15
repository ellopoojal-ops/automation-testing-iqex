import pytest, logging
from pages.loginpage import LoginPage

@pytest.mark.smoke
def test_empty_email(driver):
    page = LoginPage(driver)
    page.click_login()
    assert page.get_email_validation_message() == "Please fill in this field."
    logging.info("Empty email error message is visible")


@pytest.mark.regression
def test_invalid_email(driver):
    page = LoginPage(driver)
    page.login("super@ad.com", "Admin@123")
    assert page.is_toast_message_displayed("Email doesn't exists")
    logging.info("Invalid email error message is visible")


@pytest.mark.regression
def test_invalid_password(driver):
    page = LoginPage(driver)
    page.login("ello.muskan07@gmail.com", "admin@12")
    assert page.is_toast_message_displayed("Wrong password!")
    logging.info("Invalid password message is visible")


@pytest.mark.smoke
def test_valid_login(driver):
    page = LoginPage(driver)
    page.login("ello.muskan07@gmail.com", "Admin@123")
    assert page.is_toast_message_displayed("Login Successfully")
    logging.info("Login successfully")
