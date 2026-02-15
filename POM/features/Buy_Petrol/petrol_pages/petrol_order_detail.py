import logging

from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PetrolOrderDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """Common for Used, Active and Expired"""
        self.order_details = (AppiumBy.XPATH, "//android.widget.TextView[@text='Order details']") #text along with share button
        self.payment_details = (AppiumBy.XPATH, '//android.widget.TextView[@text="Payment details"]')
        self.payment_details_summary_bs = (AppiumBy.XPATH, '//android.widget.TextView[@text="Payment summary"]') #opens when tapped on payment details
        self.payment_details_summary_cs_close = (AppiumBy.ACCESSIBILITY_ID, "")

        """for expired"""
        self.refund_status = (AppiumBy.XPATH, '//android.widget.TextView[@text="Refund Status"]')
        self.refund_tracking_details_bs = (AppiumBy.ACCESSIBILITY_ID, "") #this appears when tapped on to track refund status
        self.refund_track_bs_close = (AppiumBy.ACCESSIBILITY_ID, "")

        """for used"""
        self.voucher_marked_used = (AppiumBy.XPATH, '//android.widget.TextView[@text="Voucher has been used"]') #text to validate used or detail page

        """for active to be written"""
        self.voucher_generated = (AppiumBy.XPATH, '//android.widget.TextView[@text="Voucher has been generated"]')
        self.get_refund = (AppiumBy.ACCESSIBILITY_ID, "") #opens a bs
        self.how_to_use = (AppiumBy.ACCESSIBILITY_ID, "") #opens how to use page
        self.report_pp = (AppiumBy.ACCESSIBILITY_ID, "") #opens hns bs
        self.find_another_pp = (AppiumBy.ACCESSIBILITY_ID, "") #opens nearby iocl pp pages
        self.open_active_voucher = (AppiumBy.ACCESSIBILITY_ID, "") #poens the voucher
        self.keep_voucher = (AppiumBy.ACCESSIBILITY_ID, "") #cta on the refund cta bs
        self.cancel_voucher = (AppiumBy.ACCESSIBILITY_ID, "") #cta on the refund cta bs


    def click_payment_details(self):
        if not self.is_displayed(self.payment_details):
            logging.info("Scrolling to Payment Details")
            self.scroll_to_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Payment details']")
        self.click(self.payment_details)
        self.logger.info("Tapped on payment details")
        return