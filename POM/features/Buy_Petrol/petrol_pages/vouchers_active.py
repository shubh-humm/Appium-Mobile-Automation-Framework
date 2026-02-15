from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.how_to_use import HowToUsePage
from features.Buy_Petrol.petrol_components.petrol_hns_bottom_sheet import HelpPage
from features.Buy_Petrol.petrol_components.recommended_vouchers import RecommendedVouchers
from features.Buy_Petrol.petrol_pages.nearby_iocl_pump_page import NearbyIoclPumpPage
from features.Buy_Petrol.petrol_pages.petrol_order_detail import PetrolOrderDetailPage


class ActiveVoucherPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """Add for active vouchers card"""

        self.no_active_voucher = (AppiumBy.ACCESSIBILITY_ID, "No voucher available") #text if theres no active voucher at the moment
        self.enable_location = (AppiumBy.ACCESSIBILITY_ID, "Allow location access") #allow location CTA on active vouchers when the location is off
        self.view_all = (AppiumBy.ACCESSIBILITY_ID, "View all") #opens nearby iocl pp page
        self.active_order_detail = (AppiumBy.ACCESSIBILITY_ID, "[<'active_voucher_{0}'>]") #active vouchers order detail
        self.active_qr_code = (AppiumBy.ACCESSIBILITY_ID, "view_qr")
        self.voucher_code = (AppiumBy.ACCESSIBILITY_ID, "Voucher Code")
        self.close_active_qr = (AppiumBy.ACCESSIBILITY_ID, "close_voucher_qr")
        self.car_profile = (AppiumBy.ACCESSIBILITY_ID, "Complete your car profile\nEarn upto 5 Ltr Park+ Petrol") #cta opens web car profile page
        self.not_redeemable_voucher = (AppiumBy.ACCESSIBILITY_ID, "Unable to redeem a voucher?") #cta opens hns BS
        self.find_nearby_petrol_pump = (AppiumBy.ACCESSIBILITY_ID, "Find another nearby\npetrol pump") #cta opens nearby IOCL pages
        self.report_petrol_pump = (AppiumBy.ACCESSIBILITY_ID, "Report a petrol pump") #cta opens hns BS
        self.know_more_fuel = (AppiumBy.ACCESSIBILITY_ID, "Know more") #cta opens "How to use" page
        self.recommended_voucher_comp = RecommendedVouchers(driver)  # recommended vouchers component, use this to access the methods of the component.


        """put the locators for active vouchers CTA"""

    def click_enable_location(self):
        self.click(self.enable_location)
        """put the return statement here if required"""

    def click_active_order_detail(self):
        self.click(self.active_order_detail)
        self.logger.info("Clicked active order detail")
        return PetrolOrderDetailPage(self.driver)

    def click_view_qr(self):
        self.click(self.active_qr_code)
        self.logger.info("opened QR code")

    def click_close_qr(self):
        self.click(self.close_active_qr)
        self.logger.info("closing QR code")

    def click_unable_to_redeem_voucher(self):
        if not self.is_displayed(self.not_redeemable_voucher):
            self.logger.info("Scrolling to 'unable to redeem voucher' CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Unable to redeem a voucher?")
        self.click(self.not_redeemable_voucher)
        self.logger.info("Clicked on unable to redeem voucher")
        return HelpPage(self.driver)

    def click_report_petrol_pump(self):
        if not self.is_displayed(self.report_petrol_pump):
            self.logger.info("Scrolling to 'reporting petrol pump' CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Report a petrol pump")
        self.click(self.report_petrol_pump)
        self.logger.info("clicked on report petrol pump")
        return HelpPage(self.driver)

    def click_know_more_active(self):
        if not self.is_displayed(self.know_more_fuel):
            self.logger.info("Scrolling to 'Know more' CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Know more")
        self.click(self.know_more_fuel)
        self.logger.info("clicked on know more CTA")
        return HowToUsePage(self.driver)

    def click_find_nearby_petrol_pump(self):
        if not self.is_displayed(self.find_nearby_petrol_pump):
            self.logger.info("Scrolling to 'Find nearby petrol pump' CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Find another nearby\npetrol pump")
        self.click(self.find_nearby_petrol_pump)
        self.logger.info("redirecting to nearby IOCL pumps page")
        return NearbyIoclPumpPage(self.driver)

    def click_active_view_iocl_pump(self):
        self.click(self.view_all)
        self.logger.info("clicked on View all CTA")
        return NearbyIoclPumpPage(self.driver)