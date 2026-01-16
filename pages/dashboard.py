from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    DASHBOARD_HEADING = (By.XPATH, "//p[normalize-space()='Dashboard']")
    # GREETING_MSG = (By.XPATH, "//span[contains(text(),'Good morning') or "
    #                     "contains(text(),'Good afternoon') or "
    #                     "contains(text(),'Good evening')]")
    GREETING_MSG = (By.XPATH, "//span[contains(text(),'Good')]")
    USER_LABEL = (By.XPATH, "//div[contains(@class,'ant-dropdown-trigger')]//span")
    TOTAL_ORG = (By.XPATH, "//p[normalize-space()='Total Organizations']")
    TOTAL_USERS = (By.XPATH, "//p[normalize-space()='Total Users']")
    ORG_COUNT = (By.XPATH, "//p[normalize-space()='Total Organizations']"
        "/ancestor::div[contains(@class,'border')]"
        "//p[@class='text-2xl self-center leading-none font-bold']")
    USERS_COUNT = (By.XPATH, "//p[normalize-space()='Total Users']"
        "/ancestor::div[contains(@class,'border')]"
        "//p[@class='text-2xl self-center leading-none font-bold']")
    
    MY_PROFILE = (By.XPATH, "//ul[@role='menu']//li[@role='menuitem']//span[normalize-space()='My Account']")
    LOGOUT_BTN = (By.XPATH, "//ul[@role='menu']//li[@role='menuitem']//span[normalize-space()='Logout']")


    def get_username_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.USER_LABEL)).text

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        

    def is_profile_elements_visible(self, locator):
        self.wait.until(EC.element_to_be_clickable(self.USER_LABEL)).click()
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()