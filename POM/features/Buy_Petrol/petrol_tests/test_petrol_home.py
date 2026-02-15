import logging
import sys
import os
import time
import pytest
import time

#add pom directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)

from common.main_landing_page import MainLandingPage

logger = logging.getLogger('')

from appium.webdriver.common.appiumby import AppiumBy
from conftest import appium_driver
from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage
from POM.common.base_page import BasePage
from features.Buy_Petrol.petrol_fixtures import buy_petrol_home_pagee
from common.os_handlers import OsHandler
from features.Buy_Petrol.petrol_fixtures import petrol_pump_reporting_fixture

class TestHomePageFunctionality:
    @pytest.mark.parametrize(
        "email, expected",
        [
            ("test12@gmail.com", "success"),
            ("test", "error"),
            ("testing@gmail.com", "success"),
            ("test@29gmail.com", "success"),
        ]
    )

    def test_email_field_ddt(self, buy_petrol_home_pagee, email, expected):
        home_page = buy_petrol_home_pagee
        email_bs = home_page.click_edit_business_email()
        assert email_bs.wait_for_visibility(email_bs.business_account), "Email BS did not appeared"
        # email_bs.clear_input(email_bs.email_input)
        time.sleep(0.1)
        email_bs.enter_email(email)
        assert email_bs.get_text(email_bs.email_input) == str(email), "couldnt enter email correctly"
        email_bs.click_submit_email()

        if expected == "success":
            assert email_bs.wait_for_visibility(email_bs.registered_text), "Valid email did not got registered"
            logger.info("Email got registered")
        elif expected == "error":
            assert email_bs.wait_for_visibility(email_bs.business_account), "Invalid email got registered"
            logger.info("Invalid email cannot be registered")

    def test_switching_personal_business_tab(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        assert home_page.wait_for_visibility(home_page.buy_petrol), "Did not landed to petrol home page"
        home_page.click_personal_acc()
        assert home_page.wait_for_invisibility(home_page.edit_id), "Did not switched to personal tab"
        logger.info("Swtiched to personal tab, switching back to business tab")
        home_page.click_business_acc()
        assert home_page.wait_for_visibility(home_page.edit_id), "Did not switched to business tab"

    def test_total_savings_home(self, buy_petrol_home_pagee):
        """home page total savings to be tested"""
        home_page = buy_petrol_home_pagee
        try:
            home_page.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "savings_widget")
        except Exception:
            pytest.skip("Savings widget not found after scrolling")

        if home_page.is_displayed(home_page.total_savings):
            total_savings_wdiget = home_page.click_home_total_savings()
            assert total_savings_wdiget.wait_for_visibility(total_savings_wdiget.total_savings_text), "Total savings bs did not appeard"
            total_savings_wdiget.click_got_it()
            assert home_page.wait_for_visibility(home_page.total_savings), "Total savings bs did not closed"
            logger.info("Total savings BS closed")

    def test_email_id(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        email_bs = home_page.click_edit_business_email()
        assert email_bs.wait_for_visibility(email_bs.business_account), "email bs did not appeared"
        logger.info("Edit Email BS opened")

    def test_edit_email_bs2(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        email_bs1 = home_page.click_edit_business_email()
        email_bs2 = email_bs1.click_submit_email()
        assert email_bs2.wait_for_visibility(email_bs2.registered_text), "submitted email bs did not appeared"
        logger.info("Email Submitted")
        email_bs2.click_edit_email()
        assert email_bs1.wait_for_visibility(email_bs1.business_account), "email bs did not appeared"
        logger.info("Redirected to first email BS")

    def test_my_vouchers(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        vouchers = home_page.click_my_vouchers()
        assert vouchers.wait_for_visibility(vouchers.my_vouchers_heading_text), "My vouchers page did not loaded"
        logging.info("Navigated to my vouchers")

    def test_hns_bs(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        hns_bs = home_page.click_hns()
        assert hns_bs.wait_for_visibility(hns_bs.issues_faced), "Hns BS did not loaded"
        logging.info("HnS BS opened")

    def test_buy_petrol_now(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        petrol_page = home_page.click_buy_petrol_button_home()
        assert petrol_page.wait_for_visibility(petrol_page.buy_petrol_voucher_text), "Petrol voucher page did not loaded"
        logging.info("Navigated to Petrol Voucher Page")

    def test_xp95(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        xp95 = home_page.click_xp_95()
        assert xp95.wait_for_visibility(xp95.buy_petrol_voucher_text), "XP95 page did not loaded"
        logging.info("Navigated to XP95")
        tc = xp95.click_xp95_banner()
        assert tc.wait_for_visibility(tc.terms_conditions), "Terms and conditions page did not loaded"
        logging.info("Navigated to Terms and Conditions Page")

    def test_xtragreen(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        xtragreen = home_page.click_xtragreen()
        assert xtragreen.wait_for_visibility(xtragreen.buy_petrol_voucher_text), "XtraGreen's page did not loaded"
        logging.info("Navigated to XtraGreen")
        tc = xtragreen.click_xtra_green_banner()
        assert tc.wait_for_visibility(tc.terms_conditions), "Terms and conditions page did not loaded"
        logging.info("Navigated to Terms and Conditions Page")

    def test_petrol_floating(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        petrol_page = home_page.click_buy_petrol_floating_button()
        assert petrol_page.is_displayed(petrol_page.buy_petrol_voucher_text), "Petrol voucher page did not loaded"
        logging.info("Navigated to Petrol Voucher Page")

    def test_petrol_tandc(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        tandc = home_page.click_tandc()
        assert tandc.wait_for_visibility(tandc.terms_conditions), "Terms and conditions page did not loaded"
        logging.info("Navigated to Terms and Conditions Page")

    def test_petrol_faq(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        faq = home_page.click_recent_faq()
        assert faq.is_displayed(faq.recent_faq_ques), "FAQ page did not loaded"
        logging.info("Navigated to FAQ Page")

    def test_active_vouhcer_qr(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        try:
            home_page.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "view_qr")
        except Exception:
            pytest.skip("View QR code not found after scrolling")

        if home_page.is_displayed(home_page.active_qr_code):
            active_qr = home_page.click_home_qr()
            assert active_qr.wait_for_visibility(active_qr.voucher_code), "QR page did not loaded"
            active_qr.click_close_qr()
            assert home_page.wait_for_visibility(home_page.active_qr_code), "QR page did not got closed"
            logger.info("QR page closed")

    def test_hns_voucher_marked_used(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        hns_btn = home_page.click_hns()
        assert hns_btn.wait_for_visibility(hns_btn.machine_issues), "Machine issues is not displayed"
        assert hns_btn.is_displayed(hns_btn.operator_issues), "Operator issues is not displayed"
        assert hns_btn.is_displayed(hns_btn.petrol_not_accepting), "PP not accepting is not displayed"
        assert hns_btn.is_displayed(hns_btn.used_voucher), "Voucher marked used is not displayed"

        marked_used_voucher = hns_btn.click_voucher_marked_used()
        assert marked_used_voucher.wait_for_visibility(marked_used_voucher.new_voucher_sheet), "New voucher sheet did not appeard"
        marked_used_voucher.click_got_it()
        assert home_page.wait_for_visibility(home_page.buy_petrol_button), "New voucher bs did not closed"
        logging.info("Hns BS closed, user back to home page")

    def test_nesting_bs_hns_flow(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        hns_btn = home_page.click_hns()
        assert hns_btn.wait_for_visibility(hns_btn.issues_faced), "Hns BS did not appeard"
        pp_issue = hns_btn.click_petrol_not_accepting()
        assert pp_issue.wait_for_visibility(pp_issue.not_accepting_voucher), "PP not accepting voucher BS did not displayed"
        pp_issue.click_report_pp()
        assert pp_issue.wait_for_visibility(pp_issue.pumpwithin_3km), "PP reporting BS not appeard"
        nopp = pp_issue.click_couldnt_find_pp()
        assert nopp.wait_for_visibility(nopp.add_pump_details), "Pump form BS did not appeard"

    def test_pump_form_submission(self, petrol_pump_reporting_fixture):
        reporting_page = petrol_pump_reporting_fixture
        reporting_page.wait_for_visibility(reporting_page.add_pump_details)
        user_name = "shubham"
        reporting_page.click(reporting_page.name_input)
        reporting_page.enter_name(user_name)
        assert reporting_page.get_text(reporting_page.name_input) == user_name, "User name didn't match"
        user_address = "Address"
        reporting_page.click(reporting_page.pp_address_input)
        reporting_page.enter_pump_address(user_address)
        assert reporting_page.get_text(reporting_page.pp_address_input) == user_address, "User address didn't match"
        reporting_page.click_upload_docs()
        upload_image = OsHandler(reporting_page.driver)
        upload_image.handle_image_flow()
        reporting_page.wait_for_visibility(reporting_page.add_pump_details)
        reporting_page.click_submit_button()
        assert reporting_page.wait_for_visibility(reporting_page.pump_reported), "nearby IOCL CTA bs did not appeard"
        nearby_iocl = reporting_page.click_find_iocl_pumps()
        assert nearby_iocl.wait_for_visibility(nearby_iocl.nearby_iocl_pp), "Nearby iocl page did not apperad"
        logging.info("Navigated to Nearby IOCL pump page")