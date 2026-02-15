from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_pages.petrol_voucher_payment import PetrolVoucherPayment


class BusinessEmailSheet(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.business_account = (AppiumBy.ACCESSIBILITY_ID, "Introducing business account") #bs heading text to validate bs sheet
        self.close_button = (AppiumBy.ACCESSIBILITY_ID, "close_bottomsheet_global")
        self.email_input = (AppiumBy.XPATH, "//android.widget.EditText[@hint='email_input_field']") #inpput field to be entered
        self.registered_text = (AppiumBy.ACCESSIBILITY_ID, "Successfully registered!") #text appears when first time email is submitted
        self.submit_email_button = (AppiumBy.ACCESSIBILITY_ID, "Submit")
        self.cancel_email_button = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
        self.edit_email_cta = (AppiumBy.ACCESSIBILITY_ID, "Edit email ID")
        self.buy_voucher_cta = (AppiumBy.ACCESSIBILITY_ID, "Buy voucher now") #redirects to my voucher page

    def enter_email(self, email):
        self.type_text(self.email_input, email)
        self.logger.info(f"Entered email: {email}")

    def click_submit_email(self):
        self.click(self.submit_email_button)
        self.logger.info("Submitting  email")
        return self

    def click_cancel_email(self):
        self.click(self.cancel_email_button)
        self.logger.info("Cancelling email changes")

    def validate_email_registered(self):
        self.is_displayed(self.registered_text)

    def click_edit_email(self):
        self.click(self.edit_email_cta)
        self.logger.info("Clicked on Edit email")

    def click_buy_voucher_cta(self):
        self.click(self.buy_voucher_cta)
        self.logger.info("Clicked on Buy Voucher")
        return PetrolVoucherPayment(self.driver)
