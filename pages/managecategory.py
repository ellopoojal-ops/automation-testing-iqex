from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ManageCategory:
    def __init__(self, driver):
        self.driver = driver 
        self.wait = WebDriverWait(driver, 10)

    SIDEMENU_TOGGLE = (By.ID, "Icon_feather-arrow-right")
    MANAGE_CATEGORY_BTN = (By.XPATH, "//button[normalize-space()='Manage Category']")
    MODULE_HEADING = (By.XPATH, "//h2[normalize-space()='Manage Category']")
    CREATE_CATEGORY_BTN = (By.XPATH, "//button[normalize-space()='Create Category']")

    def open_side_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.SIDEMENU_TOGGLE)).click()
    
    def open_manage_category_module(self):
        self.wait.until(EC.element_to_be_clickable(self.MANAGE_CATEGORY_BTN)).click()
    
    def is_manage_category_module_opened(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MODULE_HEADING)).is_displayed()
    
    def open_create_category_form(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_CATEGORY_BTN)).click()
    
    

    
