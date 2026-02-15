import logging

import pytest
from common.main_landing_page import MainLandingPage
from conftest import appium_driver
from POM.features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage

@pytest.fixture
def buy_petrol_home_pagee(appium_driver):
    # navigate to buy petrol home page
    landing_page = MainLandingPage(appium_driver)
    logging.info("Landed on Main Landing Page")
    page = landing_page.navigate_to_buy_petrol()
    page.nearby_accepting_bs.click_close_bs()
    logging.info("Navigating to Petrol Home Page")
    yield page


@pytest.fixture
def petrol_voucher_page_fixture(appium_driver):
    # logging.info("Navigating to petrol voucher page")
    landing_page = MainLandingPage(appium_driver)
    logging.info("Landed on Main Landing Page")
    petrol_home = landing_page.navigate_to_buy_petrol()
    logging.info("Landed on Petrol Home Page")
    petrol_home.nearby_accepting_bs.click_close_bs()
    voucher_page = petrol_home.click_buy_petrol_button_home()
    logging.info("Navigating to Petrol Voucher Page")

    yield voucher_page


@pytest.fixture
def petrol_my_vouchers_page_fixture(appium_driver):
    landing_page = MainLandingPage(appium_driver)
    logging.info("Landed on Main Landing Page")
    petrol_home = landing_page.navigate_to_buy_petrol()
    logging.info("Landed on Petrol Home Page")
    petrol_home.nearby_accepting_bs.click_close_bs()
    my_vouchers_page = petrol_home.click_my_vouchers()
    logging.info("Navigating to My Vouchers Page")

    yield my_vouchers_page


@pytest.fixture
def petrol_pump_reporting_fixture(appium_driver):
    landing_page = MainLandingPage(appium_driver)
    logging.info("Landed on Main Landing Page")
    petrol_home = landing_page.navigate_to_buy_petrol()
    logging.info("Landed on Petrol Home Page")
    petrol_home.nearby_accepting_bs.click_close_bs()
    hns_btn = petrol_home.click_hns()
    logging.info("Opened Hns Bottom Sheet")
    reporting_pp = hns_btn.click_petrol_not_accepting()
    reporting_pp.click_report_pp()
    logging.info("Clicked to report petrol pump")
    no_pump = reporting_pp.click_couldnt_find_pp()
    no_pump.wait_for_visibility(no_pump.add_pump_details)
    logging.info("Landed on Pump form submission page")

    yield no_pump