from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage


class ExitVoucherBs(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.close_sheet_btn = (AppiumBy.ACCESSIBILITY_ID, "")
        self.buy_voucher_btn = (AppiumBy.ACCESSIBILITY_ID, "Buy Voucher") #closes the bs, and remains at the same page
        self.exit_btn = (AppiumBy.ACCESSIBILITY_ID, "Exit")

    def click_close_sheet_btn(self):
        self.click(self.close_sheet_btn)
        """put the return statement here"""

    def click_buy_voucher_btn(self):
        self.click(self.buy_voucher_btn)
        self.logger.info("clicked buy voucher button")
        return

    def click_exit_btn(self):
        self.click(self.exit_btn)
        self.logger.info("Moving to the previous Page")
        return FuelHomePage(self.driver)