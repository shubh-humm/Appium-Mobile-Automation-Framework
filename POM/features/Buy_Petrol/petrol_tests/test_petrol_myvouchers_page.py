import logging
import sys
import os
import pytest
import time

from appium.webdriver.common.appiumby import AppiumBy

from common.main_landing_page import MainLandingPage
from conftest import appium_driver
from POM.common.base_page import BasePage
from POM.features.Buy_Petrol.petrol_fixtures import petrol_my_vouchers_page_fixture


# Add POM directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)

"""for active tabs"""
def test_unable_to_redeem(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    active_tab = my_vouchers.click_active_tab()
    not_redeemable = active_tab.click_unable_to_redeem_voucher()
    assert not_redeemable.wait_for_visibility(not_redeemable.issues_faced), "HnS BS did not appeared"
    logging.info("HnS Bs displayed")

def test_report_pp(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    active_tab = my_vouchers.click_active_tab()
    report_pp = active_tab.click_report_petrol_pump()
    assert report_pp.wait_for_visibility(report_pp.issues_faced), "HnS BS did not appeared"
    logging.info("Hns Bs displayed")

def test_nearby_pp(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    active_tab = my_vouchers.click_active_tab()
    find_nearby_pp = active_tab.click_find_nearby_petrol_pump()
    assert find_nearby_pp.wait_for_visibility(find_nearby_pp.nearby_iocl_pp), "Nearby IOCL pp page did not appeared"
    logging.info("Navigated to nearby IOCL pp page")

def test_know_more_active(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    active_tab = my_vouchers.click_active_tab()
    know_more = active_tab.click_know_more_active()
    assert know_more.wait_for_visibility(know_more.steps_to_use), "How to use page did not loaded"
    logging.info("Navigated to 'know more' page")

def test_active_qr_intab(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    active_tab = my_vouchers.click_active_tab()
    if active_tab.wait_for_visibility_optional(active_tab.active_qr_code):
        active_tab.click_view_qr()
        assert active_tab.wait_for_visibility(active_tab.voucher_code), "QR code page did not opened"
        active_tab.click_close_qr()
        assert active_tab.wait_for_visibility(active_tab.active_qr_code), "QR code page did not appeard"
    else:
        pytest.skip("There are no active vouchers for the user")

def test_view_all_iocl_pump(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    active_tab = my_vouchers.click_active_tab()
    if active_tab.wait_for_visibility_optional(active_tab.view_all):
        nearby_iocl = active_tab.click_active_view_iocl_pump()
        assert nearby_iocl.wait_for_visibility(nearby_iocl.nearby_iocl_pp), "Did not navigated to neraby iocl page"
        logging.info("navigated to iocl page")
    else:
        pytest.skip("There are no active vouchers for the user")

def test_active_order_detail(appium_driver):
    main_landing_page = MainLandingPage(appium_driver)
    petrol_home = main_landing_page.navigate_to_buy_petrol()
    my_vouchers = petrol_home.click_my_vouchers()
    assert my_vouchers.wait_for_visibility(my_vouchers.my_vouchers_heading_text), "My voucher page did not opened"
    active_tab = my_vouchers.click_active_tab()
    active_order = active_tab.click_active_order_detail()
    assert active_order.wait_for_visibility(active_order.voucher_generated), "Active order detail page did not opened"
    logging.info("Active order detail page has loaded successfully")

"""for used tab"""
def test_used_download_receipt(petrol_my_vouchers_page_fixture):
    my_vouchers = petrol_my_vouchers_page_fixture
    used_tab = my_vouchers.click_used_tab()
    if used_tab.is_displayed(used_tab.download_receipt):
        receipt_bs = used_tab.click_download_receipt()
        assert receipt_bs.wait_for_visibility(receipt_bs.fuel_voucher_receipt), "Used receipt bs did not appeared"
    else:
        pytest.skip("There are no used vouchers for this user")
        """download receipt flow"""

def test_used_expired_order_detail(appium_driver):
    main_landing_page = MainLandingPage(appium_driver)
    petrol_home = main_landing_page.navigate_to_buy_petrol()
    my_vouchers = petrol_home.click_my_vouchers()
    assert my_vouchers.wait_for_visibility(my_vouchers.my_vouchers_heading_text), "Page did not loaded"
    used_tab = my_vouchers.click_used_tab()
    used_order = used_tab.click_used_order_detail()
    assert used_order.wait_for_visibility(used_order.voucher_marked_used), "Page did not loaded"
    logging.info("Used order detail page has loaded successfully")

"""for expired tab"""
def test_expired_order_detail(appium_driver):
    main_landing_page = MainLandingPage(appium_driver)
    petol_home = main_landing_page.navigate_to_buy_petrol()
    my_vouchers = petol_home.click_my_vouchers()
    assert my_vouchers.wait_for_visibility(my_vouchers.my_vouchers_heading_text), "Page did not loaded"
    expired_tab = my_vouchers.click_expired_tab()
    assert expired_tab.wait_for_visibility(expired_tab.expired_order_detail), "Page did not loaded"
    expired_order = expired_tab.click_expired_order_detail()
    assert expired_order.wait_for_visibility(expired_order.refund_status), "Refund status could not loaded"
    expired_order.click_payment_details()
    assert expired_order.wait_for_visibility(expired_order.payment_details_summary_bs), "Payment details summary could not loaded"
    logging.info("Payment summary bs has loaded successfully")



