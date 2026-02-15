import logging
import sys
import os
import pytest
import time

from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage

logger = logging.getLogger('')

from appium.webdriver.common.appiumby import AppiumBy
from conftest import appium_driver
from POM.features.Buy_Petrol.petrol_fixtures import petrol_voucher_page_fixture
from POM.features.Buy_Petrol.petrol_components import leave_voucher_page

# add pom directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)

class TestPetrolPaymentPage:

    @pytest.mark.parametrize(
        "t_amount , expected",
        [
            ("99", "fail"),
            ("100", "pass"),
            ("5999", "pass"),
            ("6000", "fail"),
            ("3000", "pass"),
            ("", "fail"),
            ("abc", "fail")
        ]
    )

    def test_amount_ddt(self, petrol_voucher_page_fixture, t_amount, expected):
        voucher_page = petrol_voucher_page_fixture
        time.sleep(4)
        voucher_page.enter_amount(t_amount)

        try:
            payment_amount = int(t_amount)

            if payment_amount < 100:
                assert not voucher_page.is_cta_enabled(voucher_page.proceed_to_pay), "Proceed to pay should be disabled"
                assert voucher_page.is_displayed(voucher_page.less_amount_error), "Minium amount message not displayed"

            elif payment_amount > 5999:
                assert not voucher_page.is_cta_enabled(voucher_page.proceed_to_pay), "Proceed to pay should be disabled"
                assert voucher_page.is_displayed(voucher_page.more_amount_error), "Max amount message not displayed"

            elif 100 <= payment_amount <= 5999:
                assert voucher_page.is_cta_enabled(voucher_page.proceed_to_pay), "Proceed to pay should be Enabled"
                voucher_page.click_proceed_to_pay()
                assert voucher_page.wait_for_visibility(voucher_page.processing_payment), "Page did not loaded"

        except ValueError:
            assert not voucher_page.is_cta_enabled(voucher_page.confirm_btn), "Proceed to pay CTA should be disabled for non numeric value"

    def test_total_savings(self, petrol_voucher_page_fixture):
        voucher_page = petrol_voucher_page_fixture
        savings = voucher_page.click_savings_bs()
        assert savings.wait_for_visibility(savings.total_savings_text), "Total savings BS did not appeared"
        assert savings.wait_for_visibility(savings.got_it_btn), "Got it btn is not displayed"
        savings.click_got_it()
        assert voucher_page.wait_for_visibility(voucher_page.savings_bs), "BS did not got closed"
        logging.info("Tota savings BS got closed successfully")

    def test_driver_checkbox(self, petrol_voucher_page_fixture):
        voucher_page = petrol_voucher_page_fixture
        assert voucher_page.wait_for_visibility(voucher_page.buy_petrol_voucher_text), "Buy voucher page has not apperad"

        if voucher_page.is_displayed(voucher_page.driver_number_input_field):
            logging.info("Driver checkbox is already true")
        else:
            logging.info("Driver checkbox is not true")
            voucher_page.click_driver_checkbox()

        voucher_page.clear_input(voucher_page.driver_number_input_field)
        driver_no = 5555555555
        voucher_page.enter_driver_number(driver_no)
        assert voucher_page.get_text(voucher_page.driver_number_input_field) == str(driver_no), "Driver number is not entered correctly"
        voucher_page.click_driver_checkbox()
        assert not voucher_page.is_displayed(voucher_page.driver_number_input_field), "Driver number is displayed even after unchecking the checkbox"

    def test_see_how_to_use(self, petrol_voucher_page_fixture):
        voucher_page = petrol_voucher_page_fixture
        howtouse = voucher_page.click_how_to_use()
        assert howtouse.wait_for_visibility(howtouse.steps_to_use), "Didn't navigated to how to use page"
        logging.info("Navigated to how to use page")

    def test_no_leave_page_bs(self, petrol_voucher_page_fixture):
        voucher_page = petrol_voucher_page_fixture
        leave_bs = voucher_page.click_back_btn()
        assert leave_bs.wait_for_visibility(leave_bs.remain_buy_voucher), "Page leaving confirmation BS did not appeard"
        leave_bs.click_buy_voucher()
        assert leave_bs.wait_for_invisibility(leave_bs.remain_buy_voucher), "Page leaving confirmation BS did not closed"
        logging.info("User is on the petrol payment page only")

    def test_leave_page_bs(self, petrol_voucher_page_fixture):
        voucher_page = petrol_voucher_page_fixture
        leave_bs = voucher_page.click_back_btn()
        assert leave_bs.wait_for_visibility(leave_bs.remain_buy_voucher), "Page leaving confirmation BS did not appeard"
        home_page = leave_bs.click_exit_btn()




