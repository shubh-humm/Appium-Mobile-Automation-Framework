import logging
import sys
import os
import time
import pytest
from selenium.webdriver.common.by import By

from POM.features.fastag.fastag_pages.fastag_home_page import FastagHomePage
from conftest import appium_driver
from POM.features.fastag.fastag_fixtures import fastag_home_pagee
from POM.features.fastag.fastag_fixtures import fastag_recharge_payment_page
from appium.webdriver.common.appiumby import AppiumBy
from POM.features.fastag.fastag_fixtures import other_services_buy_now
from POM.features.store.store_pages.fastag_product_store_page import FastagProductStorePage

# Add POM directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)


"""smoke fastag"""

@pytest.mark.smoke
def test_fastag_recharge_smoke(fastag_home_pagee):
    """this flow test recharge flow by entering VRN"""
    fastag_home = fastag_home_pagee
    fastag_home.go_to_recharge_input()
    recharge_vehicle = "HR12AV8196"
    fastag_home.recharge_new_vehicle(recharge_vehicle)
    assert fastag_home.get_text(fastag_home_pagee.recharge_input_field) == recharge_vehicle, "Vehicle number did not matched"
    fastag_recharge = fastag_home.go_to_recharge_now_button()
    assert fastag_recharge.wait_for_visibility(fastag_recharge.recharge_page), "Did not navigated to fastag recharge page"
    fastag_recharge.click_amount_two()
    fastag_recharge.wait_for_clickable(fastag_recharge.proceed_to_pay)
    fastag_recharge.click_pay_amount()
    """assert the pay now button worked"""

@pytest.mark.smoke
def test_buy_fastag_with_vrn_smoke(other_services_buy_now):
    """this flow buys fastag with VRN"""
    other_services_page = other_services_buy_now
    assert other_services_page.wait_for_visibility(other_services_page.no_vehicle_number_right_now), "Did not landed on other servies page"
    vehicle_num = "HR12AV8196"
    other_services_page.enter_vehicle_number(vehicle_num)
    assert other_services_page.get_text(other_services_page.vehicle_number_input) == vehicle_num, "Vehicle number did not matched"
    fastag_store = other_services_page.click_continue_button()
    assert fastag_store.wait_for_visibility(fastag_store.delivery_avail), "Did not navigated to store"

@pytest.mark.smoke
def test_buy_fastag_bank_smoke(other_services_buy_now):
    """this flow buys fastag with bank"""
    other_servies_page = other_services_buy_now
    assert other_servies_page.wait_for_visibility(other_servies_page.no_vehicle_number_right_now), "Did not landed on other servies page"
    no_vrn = other_servies_page.click_on_no_vehicle_number_rightnow()
    assert no_vrn.wait_for_visibility(no_vrn.no_fastag_button), "did not landed on current fastag bank page"
    choose_bank = no_vrn.click_fastag_bank()
    assert choose_bank.wait_for_visibility(choose_bank.delivery_avail), "Did not navigated to bank page"

@pytest.mark.smoke
def test_buy_fastag_no_fastag_smoke(other_services_buy_now):
    """this flow buys fastag without VRN"""
    other_services_page = other_services_buy_now
    assert other_services_page.wait_for_visibility(other_services_page.no_vehicle_number_right_now), "Did not landed on other servies page"
    no_vrn = other_services_page.click_on_no_vehicle_number_rightnow()
    assert no_vrn.wait_for_visibility(no_vrn.no_fastag_button), "did not landed on current fastag bank page"
    no_fastag = no_vrn.click_fastag_bank()
    assert no_fastag.wait_for_visibility(no_fastag.delivery_avail), "Did not navigated to bank page"

"""fastag home end to end flowsss"""
def test_refresh_balance_home_card(fastag_home_pagee):
    """this flow validates refresh button on the vehicle cards"""
    fastag_home = fastag_home_pagee
    if fastag_home.is_displayed(fastag_home.refresh_balance):
        fastag_home.click_refresh_balance()
        assert fastag_home.wait_for_visibility(fastag_home.currnt_balance_bottom_sheet), "Refreshed balance bottom sheet is not displayed"
    else:
        pytest.skip("Vehicle cards not found, check logged in user")

def test_refresh_recharge_card_home(fastag_home_pagee):
    """the flow here is to test 'Recharge' CTA, which appears on refresh balance BS, of the cards"""
    fastag_home = fastag_home_pagee
    if fastag_home.is_displayed(fastag_home.refresh_balance):
        fastag_home.click_refresh_balance()
        assert fastag_home.wait_for_visibility(fastag_home.currnt_balance_bottom_sheet), "Refresh balance bototm sheet is not displayed"
        logging.info("Refreshed balance BS opened")
        recharge_fastag = fastag_home.click_recharge_refreshed_vehicle_bs()
        assert recharge_fastag.wait_for_visibility(recharge_fastag.recharge_page), "User did not redirected to the recharge page"
        logging.info("Redirected to recharge page")
    else:
        pytest.skip("Vehicle cards not found, check logged in user")

def test_last_toll_debit(fastag_home_pagee):
    """here the ID for last toll debit is hardcoded, so would have to change it everytime, this flow validates we redirect to passbook page"""
    fastag_home = fastag_home_pagee
    if fastag_home.is_displayed(fastag_home.refresh_balance):
        passbook = fastag_home.click_last_toll_debit()
        assert passbook.wait_for_visibility(passbook.passbook_page), "last toll debit page has not loaded"
        logging.info("Fastag passbook page has opened")
    else:
        pytest.skip("Vehicle cards not found, check logged in user")

def test_last_toll_balance_check(fastag_home_pagee):
    """here the ID for last toll debit is hardcoded, so would have to chnage it everytime"""
    """this flow checks the fastag balance after landing on the passbook page"""
    fastag_home = fastag_home_pagee
    passbook = fastag_home.click_last_toll_debit()
    assert passbook.wait_for_visibility(passbook.passbook_page), "Last toll debit page has not loaded"
    assert passbook.wait_for_visibility(passbook.check_balance), "could not find check balance CTA"
    passbook.tap_check_balance()
    passbook.wait_for_visibility(passbook.refresh_bottom_sheet_button), "Balance bottom sheet did not apperad"
    passbook.tap_refresh_balance()
    passbook.close_balance_bottom_sheet()
    assert passbook.wait_for_invisibility(passbook.refresh_bottom_sheet_button), "Balance bottom has not closed"

def test_recharge_card_cta(fastag_home_pagee):
    """this flow test recharge CTA which is present on the vehicle cards"""
    fastag_home = fastag_home_pagee
    if fastag_home.is_displayed(fastag_home.card_rechargs):
        fastag_pasbook = fastag_home.click_on_recharge_card()
        assert fastag_pasbook.wait_for_visibility(fastag_pasbook.recharge_page), "recharge page has not loaded"
    else:
        pytest.skip("Vehicle cards not found, check logged in user")

def test_tag_closed_fastag_closed_card(fastag_home_pagee):
    """this flow test tag closed CTA which is present on the vehicle cards"""
    fastag_home = fastag_home_pagee
    if fastag_home.is_displayed(fastag_home.tag_closed):
        tag_closed = fastag_home.click_why_is_tag_closed()
        assert tag_closed.wait_for_visibility(tag_closed.tag_closed_heading), "Tag closed page has not loaded"
    else:
        pytest.skip("Vehicle cards not found where the tags are closed, check logged in user")

def test_buy_new_fastag_closed_card(fastag_home_pagee):
    """this flow test 'buy new ' CTA which is present on the vehicle cards"""
    fastag_home = fastag_home_pagee
    new_fastag = fastag_home.click_buy_new_fastag()
    assert new_fastag.wait_for_visibility(new_fastag.no_vehicle_number_right_now), "'Buy new fastag' did not redirected to buy fastag ( other services page ) "

