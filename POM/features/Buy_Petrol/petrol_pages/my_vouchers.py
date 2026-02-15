from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.recommended_vouchers import RecommendedVouchers
from features.Buy_Petrol.petrol_pages.vouchers_active import ActiveVoucherPage
from features.Buy_Petrol.petrol_pages.vouchers_expired import ExpiredVouchersPage
from features.Buy_Petrol.petrol_pages.vouchers_used import UsedVouchersPage


class MyVouchers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.my_vouchers_heading_text = (AppiumBy.ACCESSIBILITY_ID, "Buy Petrol")
        self.active_tab = (AppiumBy.ACCESSIBILITY_ID, "active_tab\nTab 1 of 3")
        self.used_tab = (AppiumBy.ACCESSIBILITY_ID, "used_tab\nTab 2 of 3")
        self.expired_tab = (AppiumBy.ACCESSIBILITY_ID, "expired_tab\nTab 3 of 3")

        """Sections in my vouchers page"""

    def click_active_tab(self):
        self.click(self.active_tab)
        return ActiveVoucherPage(self.driver)

    def click_used_tab(self):
        self.click(self.used_tab)
        return UsedVouchersPage(self.driver)

    def click_expired_tab(self):
        self.click(self.expired_tab)
        return ExpiredVouchersPage(self.driver)

