from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_pages.petrol_voucher_payment import PetrolVoucherPayment

"""voucher cards in My vouchers page"""
class RecommendedVouchers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.voucher_cards = (AppiumBy.ACCESSIBILITY_ID, f"buy_voucher_card_{{{0}}}")

    def click_voucher_buy_now(self, index):
        locator = (AppiumBy.ACCESSIBILITY_ID, f"buy_voucher_card_{{{index}}}")
        self.click(locator)
        return PetrolVoucherPayment(self.driver)
        """add the return statement here"""
