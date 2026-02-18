import logging
import sys
import os
import time
import pytest

from features.fastag.fastag_fixtures import fastag_recharge_payment_page


# Add POM directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)

def test_recharge_amount_input(fastag_recharge_payment_page):
    fastag_recharge_page = fastag_recharge_payment_page
    assert fastag_recharge_page.wait_for_visibility(fastag_recharge_page.refresh_fastag_balance_button), "refresh CTA did not apperad"
    fastag_recharge_page.click_refresh_fastag_balance()
    assert fastag_recharge_page.wait_for_clickable(fastag_recharge_page.refresh_fastag_balance_button), "refresh button is not clickable"

def test_recharge_amount_input_field(fastag_recharge_payment_page):
    fastag_recharge = fastag_recharge_payment_page
    assert fastag_recharge.wait_for_visibility(fastag_recharge.recharge_amount_input), "Input field did not appeaard"
    recharge_amount = 999
    fastag_recharge.enter_recharge_amount(recharge_amount)

def test_preset_values(fastag_recharge_payment_page):
    fastag_recharge_page = fastag_recharge_payment_page
    assert fastag_recharge_page.wait_for_clickable(fastag_recharge_page.amount_value_two), "preset cards are not clickable"
    fastag_recharge_page.click_amount_two()
    logging.info("preset card selected")



