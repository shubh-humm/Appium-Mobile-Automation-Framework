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



#
# def test_other_services(other_services_buy_now):
#     other_services_page = other_services_buy_now
#     print("Redirected to other services page")
#
#     assert other_services_page.is_displayed(other_services_page.continue_button), "Buy now page is not loaded"
#     other_services_page.click_continue_button()
#     print("Clicking on continue without any input")
#     assert other_services_page.is_displayed(other_services_page.no_vrn_incorrect_vrn), "Error message is not displayed"
#     other_services_page.enter_vehicle_number("HR12AV8196")
#     print("Entered VRN")
#     other_services_page.driver.hide_keyboard()
#
#     fastag_product = other_services_page.click_continue_button()
#     assert fastag_product.is_displayed(fastag_product.add_to_cart_icon), "fastag product page is not loaded"
#     fastag_product.reset_to_home()
#
# def test_no_vrn_and_fastag(other_services_buy_now):
#     page_one = other_services_buy_now
#     print("Redirected to other services page")
#     assert page_one.is_displayed(page_one.continue_button), "Other services page is not loaded"
#     page_two = page_one.click_on_no_vehicle_number_rightnow()
#     assert page_two.is_displayed(page_two.no_fastag_button), "select your current fastag bank page is ont loaded"
#     page_three = page_two.click_no_fastag_button()
#     assert page_three.is_displayed(page_three.add_to_cart_icon), "fastag product page is not loaded"
#     time.sleep(5)
#     page_three.reset_to_home()
#
# def test_recharge_vehicle(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     assert pageone.is_displayed(pageone.recharge_now_button), "Fastag home page is not loaded"
#     pageone.recharge_new_vehicle("HR12AV8196")
#     pageone.driver.hide_keyboard()
#     page_two = pageone.go_to_recharge_now_button()
#     # assert page_two.is_displayed(page_two.refresh_fastag_balance_button), "Fastag recharge page is not loaded"
#     print("Navigate to recharge page")
#     time.sleep(5)
#     page_two.click_amount_two()
#     print("choosing amount")
#     page_two.click_refresh_fastag_balance()
#     print("refreshing balance")
#     time.sleep(3)
#     page_two.click_pay_amount()
#     time.sleep(3)
#     page_two.reset_to_home()
#
# def test_no_vehicle_bank_fastag(other_services_buy_now):
#     page1 = other_services_buy_now
#     print("Redirected to other services page")
#     assert page1.is_displayed(page1.continue_button), "Other services page is not loaded"
#     page2 = page1.click_on_no_vehicle_number_rightnow()
#     assert page2.is_displayed(page2.no_fastag_button), "select bank page is not loaded"
#     page3 = page2.click_fastag_bank()
#     assert page3.is_displayed(page3.add_to_cart_icon), "Fastag product page is not loaded"
#     page3.reset_to_home()
#
# def test_vehicle_card_other_services(other_services_buy_now):
#     page1 = other_services_buy_now
#     print("Redirected to other services page")
#     page1.click_on_vehicle_card()
#     print("clicked on vehicle card, redirected to another page")
#     page2 = page1.click_on_replace_fastag()
#


#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#
# def test_recharge_flow(fastag_home_pagee):
#     pageone = fastag_home_pagee
#
#     pageone.scroll_to_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@hint, "fastag_recharge_now_input")]')
#
#     logging.info("Entering a valid input...")
#     recharge_vehicle = "HR12AV8196"
#     pageone.recharge_new_vehicle(recharge_vehicle)
#     pagetwo = pageone.go_to_recharge_now_button()
#     logging.info("Navigating to recharge page")
#     pagetwo.wait_for_visibility(pagetwo.recharge_page)
#     assert pagetwo.is_displayed(pagetwo.recharge_page), "Fastag recharge page not loaded"
#
#     logging.info("Redirected to Fastag recharge page")
#
#     pagetwo.click_amount_two()
#     logging.info("selecting another amount")
#     pagetwo.click_refresh_fastag_balance()
#     logging.info("refreshing balance")
#     time.sleep(2)
#     pagetwo.click_pay_amount()
#     logging.info("Proceeding to complete payment")
#
# def test_buy_now_with_vrn(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_buy_now")
#     pagetwo = pageone.go_to_buynow_fastag_page()
#     logging.info("Navigating to Buy now page")
#
#     pagetwo.scroll_to_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@hint, "fastag_vehicle_number_enter")]')
#     logging.info("Entering an invlaid input")
#     invalid_vrn = "HR12"
#     pagetwo.enter_vehicle_number(invalid_vrn)
#     pagetwo.driver.hide_keyboard()
#     pagetwo.click_continue_button()
#     logging.info("Clicking continue with an invalid input")
#     assert pagetwo.is_displayed(pagetwo.no_vrn_incorrect_vrn), "error message is not displayed"
#
#     logging.info("entering valid VRN")
#     valid_vrn = "HR12AV8196"
#     pagetwo.enter_vehicle_number(valid_vrn)
#     pagetwo.driver.hide_keyboard()
#     pagethree = pagetwo.click_continue_button()
#     logging.info("Clicked continue with a Valid VRN, Redirecting to store page")
#
#     pagethree.wait_for_visibility(pagethree.delivery_avail)
#     assert pagethree.is_displayed(pagethree.delivery_avail), "Store page is not loaded"
#
# @pytest.mark.reset_app
# def test_buy_now_without_vrn(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_buy_now")
#     pagetwo = pageone.go_to_buynow_fastag_page()
#     logging.info("Navigating to Buy now page")
#     pagetwo.wait_for_visibility(pagetwo.continue_button)
#     assert pagetwo.is_displayed(pagetwo.continue_button), "Buy now page is not loaded"
#
#     pagethree = pagetwo.click_on_no_vehicle_number_rightnow()
#     logging.info("Clicked on no VRN right now and Navigating to bank list page")
#     pagethree.wait_for_visibility(pagethree.no_fastag_button)
#     assert pagethree.is_displayed(pagethree.no_fastag_button), "Bank list page is not loaded"
#
#     pagefour = pagethree.click_no_fastag_button()
#     logging.info("Clicked on No FASTag right now, and Navigating to the store page")
#     pagefour.wait_for_visibility(pagefour.delivery_avail)
#     assert pagefour.is_displayed(pagefour.delivery_avail), "Store page is not loaded"
#
# @pytest.mark.reset_app
# def test_buy_now_with_bank(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_buy_now")
#     pagetwo = pageone.go_to_buynow_fastag_page()
#     logging.info("Navigating to buy now page")
#     pagetwo.wait_for_visibility(pagetwo.continue_button)
#     assert pagetwo.is_displayed(pagetwo.continue_button), "Buy now page is not loaded"
#
#     pagethree = pagetwo.click_on_no_vehicle_number_rightnow()
#     logging.info("Clicked on No VRN right now and Navigating to bank list page")
#     pagethree.wait_for_visibility(pagethree.no_fastag_button)
#     assert pagethree.is_displayed(pagethree.no_fastag_button), "Bank list page is not loaded"
#
#     pagefour = pagethree.click_fastag_bank(2)
#     logging.info("Selected a bank and Navigating to the store page")
#     pagefour.wait_for_visibility(pagefour.delivery_avail)
#     assert pagefour.is_displayed(pagefour.delivery_avail), "Store page is not loaded"
#
# """discuss for this test as it might opens a web page"""
# @pytest.mark.reset_app
# def test_buy_new_tag_vehicle_card(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_closed_tag")
#     if pageone.is_displayed(pageone.tag_closed):
#         # pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Buy new FASTag")
#         pagetwo = pageone.click_why_is_tag_closed()
#         logging.info("clicked on why is my tag close button, and navigating to the page")
#         pagetwo.wait_for_visibility(pagetwo.tag_closed_heading)
#         assert pagetwo.is_displayed(pagetwo.tag_closed_heading), "page is not displayed"
#         logging.info("Redirected to tag closed page")
#         # pagethree = pagetwo.click_buy_new_closed_tag()
#         # pagethree.wait_for_visibility(pagethree.fastag_text)
#         # assert pagethree.is_displayed(pagethree.fastag_text), "fastag home page is not displayed"
#     else:
#         logging.info("There are no vehicle cards currenlty where the tag is closed") ################3
#
# @pytest.mark.reset_app
# def test_buy_now_with_vehicle_card(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_buy_now")
#     pagetwo = pageone.go_to_buynow_fastag_page()
#     logging.info("Navigating to buy now page")
#
#     pagetwo.wait_for_visibility(pagetwo.continue_button)
#     pagethree = pagetwo.vehicle_card_by_index(1)
#     time.sleep(2)
#
#     if pagethree.wish_to_replace_buy_bottom_sheet():
#         logging.info("Bottom sheet is displayed and clicking on to replace fastag")
#         pagefour = pagethree.click_on_replace_fastag()
#     else:
#         logging.info("No bottom sheet displayed")
#         pagefour = FastagProductStorePage(pagetwo.driver)
#         # return FastagProductStorePage(pagetwo.driver)
#
#     pagefour.wait_for_visibility(pagefour.delivery_avail)
#     assert pagefour.is_displayed(pagefour.delivery_avail), "Store page is not loaded"
#     logging.info("Landed on to store page")
#
#
# @pytest.mark.reset_app
# def test_alerts(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     if pageone.is_displayed(pageone.fastag_alerts):
#         pageone.click_on_alerts()
#         assert pageone.is_displayed(pageone.your_alerts_sheet), "Alert sheet is not displayed"
#
#         pageone.click_on_got_alerts()
#         logging.info("Alerts bottom sheet closed, reopening it.")
#
#         pageone.click_on_alerts()
#         pageone.click_on_pending_activation_cta()
#
#     else:
#         pytest.skip("User do not have any alerts")
#
# @pytest.mark.reset_app
# def test_refresh_balance(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.click_refresh_balance()
#     logging.info("Refreshed the balance")
#     bottom_sheet = pageone.wait_for_visibility(pageone.currnt_balance_bottom_sheet)
#     assert bottom_sheet.is_displayed(), "Bottom sheet is not displayed"
#     logging.info("Balance bottom sheet displayed")
#     # pageone.click_check_money_offer()
#     # pageone.wait_for_visibility(pageone.check_money_offer)
#     # assert pageone.is_displayed(pageone.check_money_offer), "Money page is not loaded" #here we do not have a locator for money
#
#
# """ensure to change the id of last toll debit, as it is hard-coded"""
# @pytest.mark.reset_app
# def test_last_toll_debit(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pagetwo = pageone.click_last_toll_debit()
#     assert pagetwo.wait_for_visibility(pagetwo.passbook_page), "Passbook page is not loaded"
#     logging.info("Navigated to passbook page")
#     pagetwo.tap_check_balance()
#     pagetwo.wait_for_visibility(pagetwo.refresh_bottom_sheet_button)
#     assert pagetwo.is_displayed(pagetwo.refresh_bottom_sheet_button), "Bottom sheet is not displayed"
#     pagetwo.tap_refresh_balance()
#     pagetwo.close_balance_bottom_sheet()
#     pagetwo.tap_change_fastag_pass()
#     logging.info("selecting another vehicle...")
#     pagetwo.selecting_another_vehicle_fastag_card()
#     assert pagetwo.is_displayed(pagetwo.check_balance), "coulnt change the vehicle"
#
# @pytest.mark.reset_app
# def test_card_buy_new_tag(fastag_home_pagee):
#     pageone = fastag_home_pagee
#     pageone.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_recharge")
#     pagetwo = pageone.click_buy_new_fastag()
#     assert pagetwo.is_displayed(pagetwo.continue_button), "other services page is not loaded"


"""smoke fastag"""

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

def test_buy_fastag_with_vrn_smoke(other_services_buy_now):
    """this flow buys fastag with VRN"""
    other_services_page = other_services_buy_now
    assert other_services_page.wait_for_visibility(other_services_page.no_vehicle_number_right_now), "Did not landed on other servies page"
    vehicle_num = "HR12AV8196"
    other_services_page.enter_vehicle_number(vehicle_num)
    assert other_services_page.get_text(other_services_page.vehicle_number_input) == vehicle_num, "Vehicle number did not matched"
    fastag_store = other_services_page.click_continue_button()
    assert fastag_store.wait_for_visibility(fastag_store.delivery_avail), "Did not navigated to store"

def test_buy_fastag_bank_smoke(other_services_buy_now):
    """this flow buys fastag with bank"""
    other_servies_page = other_services_buy_now
    assert other_servies_page.wait_for_visibility(other_servies_page.no_vehicle_number_right_now), "Did not landed on other servies page"
    no_vrn = other_servies_page.click_on_no_vehicle_number_rightnow()
    assert no_vrn.wait_for_visibility(no_vrn.no_fastag_button), "did not landed on current fastag bank page"
    choose_bank = no_vrn.click_fastag_bank()
    assert choose_bank.wait_for_visibility(choose_bank.delivery_avail), "Did not navigated to bank page"

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

"""other services end to end flows"""

# def test_buy_now_replace(other_services_buy_now):
#     other_services = other_services_buy_now
#     assert other_services.wait_for_visibility(other_services.no_vehicle_number_right_now), "Other serivces page has not loaded"
#     selecting_vehicle = other_services.vehicle_card_by_index()
#     if selecting_vehicle.wish_to_replace_buy_bottom_sheet():
#         logging.info("Bottom sheet is displayed and clicking on to replace fastag")
#         store = selecting_vehicle.click_on_replace_fastag()
#     else:
#         logging.info("No bottom sheet displayed")
#         store = FastagProductStorePage(other_services.driver)
#         # return FastagProductStorePage(pagetwo.driver)
#         store.wait_for_visibility(store.delivery_avail)
        #     assert pagefour.is_displayed(pagefour.delivery_avail), "Store page is not loaded"
        #     logging.info("Landed on to store page")

        #     sv = os.vehicle_card_by_index(1)
        #     time.sleep(2)
        #
        #     if sv.wish_to_replace_buy_bottom_sheet():
        #         logging.info("Bottom sheet is displayed and clicking on to replace fastag")
        #         pagefour = sv.click_on_replace_fastag()
        #     else:
        #         logging.info("No bottom sheet displayed")
        #         pagefour = FastagProductStorePage(pagetwo.driver)
        #         # return FastagProductStorePage(pagetwo.driver)
        #
        #     pagefour.wait_for_visibility(pagefour.delivery_avail)
        #     assert pagefour.is_displayed(pagefour.delivery_avail), "Store page is not loaded"
        #     logging.info("Landed on to store page")
