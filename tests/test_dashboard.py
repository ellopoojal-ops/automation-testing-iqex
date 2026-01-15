import logging
from pages.loginpage import LoginPage
from pages.dashboard import DashboardPage

# def test_valid_login(driver):
#     page = LoginPage(driver)
#     page.login("ello.muskan07@gmail.com", "Admin@123")
#     assert page.is_toast_message_displayed("Login Successfully")

def test_dashboard_loaded(logged_in_driver):
    # login_page = LoginPage(driver)
    # login_page.login("superadmin@iqex.com", "Admin@123")
    # assert login_page.is_toast_message_displayed("Login Successfully")

    page = DashboardPage(logged_in_driver)
    username = page.get_username_text()
    assert username != ""

    assert page.is_element_visible(DashboardPage.DASHBOARD_HEADING)
    logging.info("Dashboard Heading is visible")
    assert page.is_element_visible(DashboardPage.GREETING_MSG)
    logging.info("Greetings message is visible")
    assert page.is_element_visible(DashboardPage.USER_LABEL)
    logging.info("User label is visible")


    assert page.is_element_visible(DashboardPage.TOTAL_ORG)
    logging.info("Total Organisations headiing is visible")
    assert page.is_element_visible(DashboardPage.ORG_COUNT)
    logging.info("Total Org count is visible")
    assert page.is_element_visible(DashboardPage.TOTAL_USERS)
    logging.info("Total Users headiing is visible")
    assert page.is_element_visible(DashboardPage.USERS_COUNT)
    logging.info("Total Users count is visible")