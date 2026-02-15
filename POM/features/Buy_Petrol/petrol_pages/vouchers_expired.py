from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.recommended_vouchers import RecommendedVouchers
from features.Buy_Petrol.petrol_pages.petrol_order_detail import PetrolOrderDetailPage


class ExpiredVouchersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.refunded_tag = (AppiumBy.ACCESSIBILITY_ID, "") #tag on the expired card to validate the correct page
        self.expired_order_detail = (AppiumBy.ACCESSIBILITY_ID, "[<'expired_voucher_card_0'>]") #to navigate to expired order detail
        self.recommended_voucher_comp = RecommendedVouchers(driver)  # recommended vouchers component, use this to access the methods of the component.

    def click_expired_order_detail(self):
        self.click(self.expired_order_detail)
        self.logger.info("Navigating to expired order detail page")
        return PetrolOrderDetailPage(self.driver)

    """add the methods for this page IF ANY"""