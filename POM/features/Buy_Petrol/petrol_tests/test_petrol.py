import sys
import os
import time
import pytest
import logging

from selenium.common import NoSuchElementException

from common.main_landing_page import MainLandingPage
from features.Buy_Petrol.petrol_components.no_petrol_accept_bs import NoPetrolAccept
from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage
from features.Buy_Petrol.petrol_pages.iocl_onboarding import IoclOnboardingPage
from features.Buy_Petrol.petrol_pages.petrol_voucher_payment import PetrolVoucherPayment

logger = logging.getLogger('test_petrol')

from appium.webdriver.common.appiumby import AppiumBy
from conftest import appium_driver
from POM.features.Buy_Petrol.petrol_fixtures import buy_petrol_home_pagee
from POM.features.Buy_Petrol.petrol_components import total_savings_bs
from POM.features.Buy_Petrol.petrol_fixtures import petrol_voucher_page_fixture
from features.Buy_Petrol.petrol_pages.business_email_sheet import BusinessEmailSheet


# Add POM directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)


"""--------------------------------------------SMOKE----------------------------------------------------"""

@pytest.mark.smoke
def test_buy_voucher(buy_petrol_home_pagee):
    """
    buy petrol home page > clicks buy petrol btn > choose a payment voucher >
    click on driver checkbox and enter driver number > clicks proceed to pay
    :param buy_petrol_home_pagee:
    :return:
    """
    home_page = buy_petrol_home_pagee
    assert home_page.wait_for_visibility(home_page.buy_petrol), "Petrol home page is not loaded"
    petrol_voucher = home_page.click_buy_petrol_button_home()
    assert petrol_voucher.wait_for_visibility(petrol_voucher.buy_petrol_voucher_text), "Petrol Payment voucher page is not loaded"
    assert petrol_voucher.wait_for_visibility(petrol_voucher.choose_payment_voucher), "Vouchers have not loaded yet"
    petrol_voucher.click_choose_payment_voucher()

    driver_num = 9315229016 #driver number to be entered
    if petrol_voucher.is_displayed(petrol_voucher.driver_number_input_field):
        logging.info("Driver checkbox is already true")
    else:
        logging.info("Driver checkbox is not true")
        petrol_voucher.click_driver_checkbox()

    petrol_voucher.clear_input(petrol_voucher.driver_number_input_field)
    logging.info("Clearing input field")
    petrol_voucher.enter_driver_number(driver_num)
    logging.info(f"entered driver number {driver_num}")
    assert petrol_voucher.get_text(petrol_voucher.driver_number_input_field) == str(driver_num), "Driver number is not entered correctly"
    petrol_voucher.click_proceed_to_pay()
    assert petrol_voucher.wait_for_visibility(petrol_voucher.processing_payment), "Payment processing page is not loaded"
    logging.info("Payment processing page is loaded")

@pytest.mark.smoke
def test_edit_email_id(buy_petrol_home_pagee):
    """
    petrol home page > click edit email btn > bs opens > enter and submit email > bs opens > clicks buy voucher CTA >
    on payment voucher page, enters voucher amount in the field and clicks proceed to pay
    :param buy_petrol_home_pagee:
    :return:
    """
    home_page = buy_petrol_home_pagee
    assert home_page.wait_for_visibility(home_page.buy_petrol), "Petrol home page is not loaded"
    email_bs = home_page.click_edit_business_email()
    assert email_bs.wait_for_visibility(email_bs.business_account), "Email BS did not opened"
    user_email = "shubhamkhaneja29@gmail.com" #entering email in the field
    email_bs.enter_email(user_email)
    assert email_bs.get_text(email_bs.email_input) == user_email, "Email is not entered correctly"
    email_bs.click_submit_email()
    assert email_bs.wait_for_visibility(email_bs.registered_text), "Email is not submitted correctly"
    petrol_voucher = email_bs.click_buy_voucher_cta()
    assert petrol_voucher.wait_for_visibility(petrol_voucher.buy_petrol_voucher_text), "User did not navigated to the petrol voucher page"
    logging.info("Navigated to the petrol voucher page")
    voucher_amount = 750
    logging.info(f"entered voucher amount is {voucher_amount}")
    petrol_voucher.enter_amount(voucher_amount)
    assert petrol_voucher.get_text(petrol_voucher.payment_input_field) == str(voucher_amount), "Amount is not entered correctly"
    petrol_voucher.click_proceed_to_pay()
    logging.info("Payment processing page is loaded")

@pytest.mark.smoke
def test_buy_voucher_tabs(buy_petrol_home_pagee):
    """
    petrol home page > click on my vouchers > scroll if required and click on voucher card buy now >
    landed on voucher page > click on proceed to pay
    :param buy_petrol_home_pagee:
    :return:
    """
    home_page = buy_petrol_home_pagee
    assert home_page.wait_for_visibility(home_page.buy_petrol), "Petrol home page is not loaded"
    my_vouchers = home_page.click_my_vouchers()
    assert my_vouchers.wait_for_visibility(my_vouchers.my_vouchers_heading_text), "My voucher page is not loaded"
    active_tab = my_vouchers.click_active_tab()
    if active_tab.is_displayed(active_tab.active_order_detail):
        active_tab.scroll_to_element(active_tab.recommended_voucher_comp.voucher_cards)
    petrol_voucher = active_tab.recommended_voucher_comp.click_voucher_buy_now(1)
    assert petrol_voucher.wait_for_visibility(petrol_voucher.buy_petrol_voucher_text), "User did not navigated to the petrol voucher page"
    petrol_voucher.click_proceed_to_pay()
    logging.info("Payment processing page is loaded")







