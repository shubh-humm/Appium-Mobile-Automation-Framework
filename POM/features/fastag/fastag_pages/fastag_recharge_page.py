import logging

from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

class FastagRechargePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.recharge_amount_input = (AppiumBy.XPATH, '//android.widget.EditText[@text="₹500"]') #field to edit text amount        self.pay_amount_button = (AppiumBy.ACCESSIBILITY_ID, "Proceed to pay")
        self.change_bank_button = (AppiumBy.ACCESSIBILITY_ID, "Change bank") #CTA to change bank
        self.check_coupons_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.amount_value_one = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_recharge_amount_select_0")
        self.amount_value_two = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_recharge_amount_select_1")
        self.amount_value_three = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_recharge_amount_select_2")
        self.refresh_fastag_balance_button = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_recharge_refresh")
        self.recharge_page = (AppiumBy.ACCESSIBILITY_ID, "Enter recharge amount") #text to validate that we have landed onto the right page
        self.remove_coupon = (AppiumBy.ACCESSIBILITY_ID, "Remove")
        self.proceed_to_pay = (AppiumBy.ACCESSIBILITY_ID, "Proceed to pay")

    def enter_recharge_amount(self, recharge_amount):
        logging.info(f"entering amount: '{recharge_amount}'")
        self.send_keys(self.recharge_amount_input, recharge_amount)

    def click_refresh_fastag_balance(self):
        self.click(self.refresh_fastag_balance_button)
        return self

    def click_amount_one(self):
        self.click(self.amount_value_one)
        return self

    def click_amount_two(self):
        self.click(self.amount_value_two)
        return self

    def click_amount_three(self):
        self.click(self.amount_value_three)
        return self

    def click_pay_amount(self):
        self.click(self.proceed_to_pay)
        logging.info("clicked on proceed to pay")
        return self

    def click_change_bank(self):
        self.click(self.change_bank_button)

    def click_check_coupons(self):
        self.click(self.check_coupons_button)

    def check_recharge_page(self):
        self.is_displayed(self.recharge_page)

    def remove_coupon_button(self):
        self.click(self.remove_coupon)