import logging

from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.how_to_use import HowToUsePage
from features.Buy_Petrol.petrol_components.leave_voucher_page import LeaveVoucher
from features.Buy_Petrol.petrol_components.total_savings_bs import TotalFuelSavingsBs
from features.Buy_Petrol.petrol_pages.petrol_home_tandc import TandCPage


class PetrolVoucherPayment(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.back_btn = (AppiumBy.ACCESSIBILITY_ID, "back_button_appbar_global") #displays exit bs
        self.less_amount_error = (AppiumBy.ACCESSIBILITY_ID, "Minimum voucher amount should be ₹100") #message displayed when the amount is less than 100 rs
        self.more_amount_error = (AppiumBy.ACCESSIBILITY_ID, "Maximum limit per voucher is ₹5999") #message displayed when the amount is more than 100 rs
        self.buy_petrol_voucher_text = (AppiumBy.ACCESSIBILITY_ID, "Buy Petrol Voucher") #text to validate that we have landed onto the right page
        self.xp_95_banner = (AppiumBy.ACCESSIBILITY_ID, "fuel_sku_info_card_info") #opens t and c page
        self.xtra_green_banner = (AppiumBy.ACCESSIBILITY_ID, "fuel_sku_info_card_info") #opens t and c page
        self.payment_input_field = (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, '₹')]")
        self.choose_payment_voucher = (AppiumBy.ACCESSIBILITY_ID, "voucher_amount_selector_4") #payment voucher cards on the buy petrol voucher page
        self.driver_checkbox = (AppiumBy.ACCESSIBILITY_ID, "Share this voucher with my driver")
        self.driver_number_input_field = (AppiumBy.XPATH, "//*[contains(@hint, '+91') or contains(@hint, \"Enter driver's WhatsApp number\")]")
        self.wallet_balance_checkbox = (AppiumBy.ACCESSIBILITY_ID, "")
        self.see_how_to_use = (AppiumBy.ACCESSIBILITY_ID, "See how to use") #redirects to how to use page
        self.savings_bs = (AppiumBy.ACCESSIBILITY_ID, "voucher_savings_bar") #total savings bottom sheet.
        self.proceed_to_pay = (AppiumBy.ACCESSIBILITY_ID, "Proceed to pay") #click proceed to pay
        self.processing_payment = (AppiumBy.ACCESSIBILITY_ID, "We are processing your transaction") #page appears when tapped on proceed to pay
        self.failed_payment = (AppiumBy.ACCESSIBILITY_ID, "Payment failed") #faliled payment bs
        self.retry_payment = (AppiumBy.ACCESSIBILITY_ID, "Retry payment") #retry payment on failed payment Bs
        self.confirm_btn = (AppiumBy.ACCESSIBILITY_ID, "Confirm") #proceed to pay becomes "confirm" when theres no input in it.
        self.recommended_payment_options = (AppiumBy.ACCESSIBILITY_ID, "Recommended") #it comes on next page when tapped on proceed to pay
        self.total_savings_widget_bs = TotalFuelSavingsBs(driver) #called the total savings component

    def click_back_btn(self):
        self.click(self.back_btn)
        self.logger.info("Cliked back button")
        return LeaveVoucher(self.driver)

    def click_choose_payment_voucher(self):
        self.click(self.choose_payment_voucher)
        self.logger.info("Selecting a payment voucher")
        """put the return statement here"""

    def click_xp95_banner(self):
        self.click(self.xp_95_banner)
        self.logger.info("Clicked on XP95 Banner")
        return TandCPage(self.driver)

    def click_xtra_green_banner(self):
        self.click(self.xtra_green_banner)
        self.logger.info("Clicked on XTRAgreen Banner")
        return TandCPage(self.driver)

    def click_savings_bs(self):
        self.click(self.savings_bs)
        self.logger.info("clicked total savings Bottom sheet")
        return TotalFuelSavingsBs(self.driver)

    def enter_amount(self,amount):
        self.click(self.payment_input_field)
        self.send_keys(self.payment_input_field, amount)
        self.logger.warning(f"Entered amount {amount}")

    def click_driver_checkbox(self):
        self.click(self.driver_checkbox)
        self.logger.info("clicked on driver checkbox")

    def enter_driver_number(self,driver_number):
        self.send_keys(self.driver_number_input_field, driver_number)
        self.logger.warning(f"entering driver number : {driver_number}")#enter the number during test

    def click_how_to_use(self):
        if not self.is_displayed(self.see_how_to_use):
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "See how to use")
            logging.info("Scrolling to See how to use CTA")
        self.click(self.see_how_to_use)
        self.logger.info("Clicked on How to use ")
        return HowToUsePage(self.driver)

    def click_proceed_to_pay(self):
        self.click(self.proceed_to_pay)
        self.logger.info("Proceeding with the payment")
        """put the return statement here if required"""

    def click_retry_failed_payment(self):
        self.click(self.failed_payment)
        self.logger.info("Clicked on retry payment")





