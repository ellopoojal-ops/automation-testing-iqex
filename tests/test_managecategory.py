import logging
from pages.managecategory import ManageCategory

def test_manage_category_flow(logged_in_driver):

    page = ManageCategory(logged_in_driver)

    page.open_side_menu()
    logging.info("Side menu opened")

    page.open_manage_category_module()
    logging.info("Manage Category Button Clicked")

    assert page.is_manage_category_module_opened()
    logging.info("Manage Category Module opened")

    page.open_create_category_form()
    logging.info("Create category form opened")

