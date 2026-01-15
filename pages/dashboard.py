from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    DASHBOARD_HEADING = (By.XPATH, "//*[contains(text(), 'Dashboard')]")
    GREETING_MSG = (By.XPATH, "//span[contains(text(),'Good morning') or "
                        "contains(text(),'Good afternoon') or "
                        "contains(text(),'Good evening')]")
    USER_LABEL = (By.XPATH, "//span[normalize-space()='Super Admin']")

    
    def is_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()
