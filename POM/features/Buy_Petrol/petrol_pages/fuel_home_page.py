import logging

import pytest

from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.accepting_pp_nearby import AcceptingPpNearby
from features.Buy_Petrol.petrol_components.active_voucher_qr import ActiveVoucherQr
from features.Buy_Petrol.petrol_components.fuel_location_access import FuelLocationAccessBs
from features.Buy_Petrol.petrol_components.how_to_use import HowToUsePage
from features.Buy_Petrol.petrol_components.petrol_hns_bottom_sheet import HelpPage
from features.Buy_Petrol.petrol_components.total_savings_bs import TotalFuelSavingsBs
from features.Buy_Petrol.petrol_pages.business_email_sheet import BusinessEmailSheet
from features.Buy_Petrol.petrol_pages.iocl_onboarding import IoclOnboardingPage
from features.Buy_Petrol.petrol_pages.my_vouchers import MyVouchers
from features.Buy_Petrol.petrol_pages.nearby_iocl_pump_page import NearbyIoclPumpPage
from features.Buy_Petrol.petrol_pages.petrol_home_faq import AskedQues
from features.Buy_Petrol.petrol_pages.petrol_home_tandc import TandCPage
from features.Buy_Petrol.petrol_pages.petrol_voucher_payment import PetrolVoucherPayment


class FuelHomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.buy_petrol = (AppiumBy.ACCESSIBILITY_ID, "Buy Petrol") #text to validate we have landed on the correct page
        self.my_vouchers = (AppiumBy.ACCESSIBILITY_ID, "My Vouchers") #redirect to my voucher page
        self.fuel_hns = (AppiumBy.ACCESSIBILITY_ID, "help_and_support_button") #opens hns bs
        self.personal_user = (AppiumBy.ACCESSIBILITY_ID, "Personal")
        self.business_user = (AppiumBy.ACCESSIBILITY_ID, "Business")
        self.edit_id = (AppiumBy.ACCESSIBILITY_ID, "Edit email ID") #EDIT EMAIL ID IN BUSINESS TAB
        self.buy_petrol_button = (AppiumBy.ACCESSIBILITY_ID, "buy_petrol_button") #this is the CTA with an animation effect, and fixed
        self.total_savings = (AppiumBy.ACCESSIBILITY_ID, "savings_widget")  #total savings in green bar
        self.buy_xp95 = (AppiumBy.ACCESSIBILITY_ID, "Buy XP95")
        self.buy_xtragreen = (AppiumBy.ACCESSIBILITY_ID, "Buy XtraGreen")
        self.see_how_to_use = (AppiumBy.ACCESSIBILITY_ID, "See how to use?") #how to use text on the home page under Active vouchers
        self.active_vouchers_home = (AppiumBy.ACCESSIBILITY_ID, "Active Voucher") #active vouchers text on home page, when the user have some active vouchers
        self.active_qr_code = (AppiumBy.ACCESSIBILITY_ID, "view_qr") #View QR code popup CTA
        self.close_qr_code = (AppiumBy.ACCESSIBILITY_ID, "close_voucher_qr") #to close the QR pop up
        self.redeem_cashback = (AppiumBy.ACCESSIBILITY_ID, "Redeem now") #50 rs gift for the first time users.
        self.nearby_fuel_cta = (AppiumBy.ACCESSIBILITY_ID, "View all") #view all CTA that redirects to nearby iocl pp page
        self.home_faq = (AppiumBy.ACCESSIBILITY_ID, "Frequently asked questions")
        self.home_tandc = (AppiumBy.ACCESSIBILITY_ID, "Terms and conditions")
        self.petrol_prices = (AppiumBy.ACCESSIBILITY_ID, "Petrol")
        self.diesel_prices = (AppiumBy.ACCESSIBILITY_ID, "Diesel")
        self.buy_petrol_floating_button = (AppiumBy.ACCESSIBILITY_ID, "buy_petrol_floating_button") #CTA which appears on scrolling.
        self.close_active_bs = (AppiumBy.ACCESSIBILITY_ID, "close_bottomsheet_global")
        self.iocl_identifier = (AppiumBy.ACCESSIBILITY_ID, "Cashback Program") #identifer of IOCL page
        self.nearby_accepting_bs = AcceptingPpNearby(self.driver) #bs which appears when user have an active voucher card
        self.location_access = FuelLocationAccessBs(self.driver) #bs for granting location access

    def click_hns(self):
        self.click(self.fuel_hns)
        self.logger.info("Clicked on HnS Icon")
        return HelpPage(self.driver)

    def click_edit_business_email(self):
        self.click(self.edit_id)
        self.logger.info("Clicked on edit email ID")
        return BusinessEmailSheet(self.driver)

    def click_home_total_savings(self):
        self.click(self.total_savings)
        self.logger.info("Clicked on total savings")
        return TotalFuelSavingsBs(self.driver)

    def click_personal_acc(self):
        self.click(self.personal_user)
        self.logger.info("Switched to personal account")
        """put the return statement here"""

    def click_business_acc(self):
        self.click(self.business_user)
        self.logger.info("Switched to business account")
        """enter business logic, put naviational condition for the first and exisitng user"""

    def click_buy_petrol_button_home(self):
        if not self.is_displayed(self.buy_petrol_button):
            logging.info("Scrolling to Buy Petrol Button")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "buy_petrol_button")
        self.click(self.buy_petrol_button)
        self.logger.info("Clicked on the buy petrol button")
        return PetrolVoucherPayment(self.driver)

    def click_buy_petrol_floating_button(self):
        if not self.is_displayed(self.buy_petrol_floating_button):
            logging.info("Scrolling to Buy Petrol Floating Button")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "buy_petrol_floating_button")
        self.click(self.buy_petrol_floating_button)
        self.logger.info("clicked on petrol floating button")
        return PetrolVoucherPayment(self.driver)

    def click_xp_95(self):
        if not self.is_displayed(self.buy_xp95):
            logging.info("Scrolling to XP95")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Buy XP95")
        self.click(self.buy_xp95)
        self.logger.info("Clicked on XP95")
        return PetrolVoucherPayment(self.driver)

    def click_xtragreen(self):
        if not self.is_displayed(self.buy_xtragreen):
            logging.info("Scrolling to XTRAGreen")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Buy XtraGreen")
        self.click(self.buy_xtragreen)
        self.logger.info("Clicked on XtraGreen")
        return PetrolVoucherPayment(self.driver)

    def click_redeem_cashback(self):
        if not self.is_displayed(self.redeem_cashback):
            logging.info("Scrolling to Redeem Cashback CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Redeem now")
        self.click(self.redeem_cashback)
        self.logger.info("Clicked on Redeem Cashback")
        return IoclOnboardingPage(self.driver)

    def click_recent_faq(self):
        if not self.is_displayed(self.home_faq):
            logging.info("Scrolling to FAQ CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Frequently asked questions")
        self.click(self.home_faq)
        self.logger.info("Clicked on FAQ")
        return AskedQues(self.driver)

    def click_tandc(self):
        if not self.is_displayed(self.home_tandc):
            logging.info("Scrolling to TandC CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Terms and conditions")
        self.click(self.home_tandc)
        self.logger.info("clicked on Terms & Conditions")
        return TandCPage(self.driver)

    def click_home_qr(self):
        self.click(self.active_qr_code)
        self.logger.info("Viewing QR...")
        return ActiveVoucherQr(self.driver)

    def click_close_qr(self):
        self.click(self.close_qr_code)
        self.logger.info("CLosing QR pop-up")
        """put the return statement here if required"""

    def click_view_nearby_pp(self):
        if not self.is_displayed(self.nearby_fuel_cta):
            logging.info("Scrolling to Nearby Fuel CTA")
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "View all")
        self.click(self.nearby_fuel_cta)
        self.logger.info("Clicked on View all nearby Petrol Pump")
        return NearbyIoclPumpPage(self.driver)

    def click_close_global_bs(self):
        self.click(self.close_active_bs)

    def click_how_to_use(self):
        self.click(self.see_how_to_use)
        self.logger.info("Clicked on how to use")
        return HowToUsePage(self.driver)

    def click_my_vouchers(self):
        self.click(self.my_vouchers)
        self.logger.info("Clicked My vouchers")
        return MyVouchers(self.driver)
