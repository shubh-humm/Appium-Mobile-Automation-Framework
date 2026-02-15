from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.recommended_vouchers import RecommendedVouchers
from features.Buy_Petrol.petrol_pages.petrol_order_detail import PetrolOrderDetailPage


class UsedVouchersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.vouchers_marked_used = (AppiumBy.ACCESSIBILITY_ID, "") #this is for the text in a container, which states, voucher is marked used but couldnt use at the pump
        self.download_receipt = (AppiumBy.ACCESSIBILITY_ID, "download_receipt_button") #cta on card
        self.used_order_detail = (AppiumBy.ACCESSIBILITY_ID, "[<'used_voucher_card_0'>]") #navigate to order detail
        self.download_receipt_cta_bs = (AppiumBy.ACCESSIBILITY_ID, "Download receipt") #to actually download
        self.recepipt_close_bs_button = (AppiumBy.ACCESSIBILITY_ID, "close_bottomsheet_global")
        self.fuel_voucher_receipt = (AppiumBy.ACCESSIBILITY_ID, "Fuel voucher receipt") #text on bottom sheet to validate it.
        self.complete_car_profile = (AppiumBy.ACCESSIBILITY_ID, "")
        self.recommended_voucher_comp = RecommendedVouchers(driver) # recommended vouchers component, use this to access the methods of the component.

    def click_download_receipt(self):
        self.click(self.download_receipt)
        self.logger.info("Navigating to the receipt page")
        return self
        """it opens a BS"""

    def click_complete_car_profile(self):
        self.click(self.complete_car_profile)
        self.logger.info("Navigating to the complete car profile page")

    def click_download_receipt_cta_bs(self):
        self.click(self.download_receipt_cta_bs)
        self.logger.warning("Downloading the receipt")
        """it downloads the receipt from the bs"""

    def click_close_receipt_bs(self):
        self.click(self.recepipt_close_bs_button)
        """closes the bs"""

    def click_used_order_detail(self):
        self.click(self.used_order_detail)
        self.logger.info("Navigating to the used order detail page")
        return PetrolOrderDetailPage(self.driver)

