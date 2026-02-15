import logging

from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from common.os_handlers import OsHandler

"""nearby IOCL pump page"""
class NearbyIoclPumpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.nearby_iocl_pp = (AppiumBy.ACCESSIBILITY_ID, "Nearby IndianOil petrol pumps") #page heading to validate that we have landed on the correct page
        self.enable_location = (AppiumBy.ACCESSIBILITY_ID, "Enable Location") #opens location access bs
        self.back_btn = (AppiumBy.ACCESSIBILITY_ID, "back_button_appbar_global")


    def choose_a_pump_card(self, index):
        self.pump_card = (AppiumBy.ACCESSIBILITY_ID, f"nearby_fuel_pump_card_{index}")
        if not self.is_displayed(self.pump_card):
            logging.info("cant see the nearby pump cards")
            if self.is_displayed(self.enable_location):
                logging.info("Enabling location access")
                self.click(self.enable_location)
                self.click(self.allow_google_location())
                self.wait_for_visibility(self.pump_card)
                self.click(self.pump_card)
                return
