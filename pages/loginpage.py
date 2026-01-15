from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[contains(text(), 'Login')]")
    DASHBOARD = (By.XPATH, "//span[contains(text(), 'Good morning')]")

    def enter_email(self, email):
        email_field = self.wait.until(EC.element_to_be_clickable(self.EMAIL))
        email_field.send_keys(Keys.CONTROL, "a")
        email_field.send_keys(Keys.BACKSPACE)
        email_field.send_keys(email)

    def enter_password(self, password):
        pass_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        pass_field.send_keys(Keys.CONTROL, "a")
        pass_field.send_keys(Keys.BACKSPACE)
        pass_field.send_keys(password)
    
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_email_validation_message(self):
        email_field = self.wait.until(EC.element_to_be_clickable(self.EMAIL))
        return email_field.get_attribute("validationMessage")

    def is_error_message_displayed(self, text):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{text}")]'))).is_displayed()

    def is_login_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD)).is_displayed()
