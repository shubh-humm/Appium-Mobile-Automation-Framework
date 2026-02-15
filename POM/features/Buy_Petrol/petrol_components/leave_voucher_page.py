from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

# from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage

"""bs appears when tapped on back button from the buy petrol voucher"""
"""Exit voucher is the duplicate for this"""
class LeaveVoucher(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.remain_buy_voucher = (AppiumBy.ACCESSIBILITY_ID, "Buy Voucher")
        self.exit_btn = (AppiumBy.ACCESSIBILITY_ID, "Exit")
        self.leave_identifier = (AppiumBy.ACCESSIBILITY_ID, "Are you sure you want to leave this page?")

    def click_buy_voucher(self):
        self.click(self.remain_buy_voucher)
        self.logger.info("Clicked Buy Voucher")
        return

    def click_exit_btn(self):
        self.click(self.exit_btn)
        self.logger.info("Moving back to the previous page")
        return