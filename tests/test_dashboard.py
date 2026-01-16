import logging
from pages.dashboard import DashboardPage

def test_dashboard_loaded(logged_in_driver):
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
    logging.info("Total Organisations heading is visible")
    assert page.is_element_visible(DashboardPage.ORG_COUNT)
    logging.info("Total Org count is visible")
    assert page.is_element_visible(DashboardPage.TOTAL_USERS)
    logging.info("Total Users heading is visible")
    assert page.is_element_visible(DashboardPage.USERS_COUNT)
    logging.info("Total Users count is visible")

    assert page.is_profile_elements_visible(DashboardPage.MY_PROFILE)
    logging.info("My account button is visible")

    assert page.is_profile_elements_visible(DashboardPage.LOGOUT_BTN)
    logging.info("Logout button is visible")