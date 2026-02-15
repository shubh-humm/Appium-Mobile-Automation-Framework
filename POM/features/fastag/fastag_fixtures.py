import pytest
import logging
from common.main_landing_page import MainLandingPage
from conftest import appium_driver

@pytest.fixture
def fastag_home_pagee(appium_driver):

    #navigate to fastag home page
    landing_page = MainLandingPage(appium_driver)
    logging.info("Navigated on Main Landing page")
    page = landing_page.navigate_to_fastag()

    yield page

@pytest.fixture
def other_services_buy_now(fastag_home_pagee):
    #fastag_home_page > other services ( buy now )
    page = fastag_home_pagee.go_to_buynow_fastag_page()
    yield page


@pytest.fixture
def fastag_recharge_payment_page(appium_driver):
    landing_page = MainLandingPage(appium_driver)
    logging.info("Landed on main landind page")
    fastag_home = landing_page.navigate_to_fastag()
    logging.info("Landed on fastag home page")
    fastag_home.go_to_recharge_input()
    vehicle_num = "HR12AV8196"
    fastag_home.recharge_new_vehicle(vehicle_num)
    recharge_page = fastag_home.go_to_recharge_now_button()
    recharge_page.wait_for_visibility(recharge_page.recharge_page)
    logging.info("Navigating to recharge payment page")

    yield recharge_page



