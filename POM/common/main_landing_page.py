import logging

from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from features.fastag.fastag_pages.fastag_home_page import FastagHomePage
from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage

class MainLandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.fastag_section = (AppiumBy.ACCESSIBILITY_ID, "FASTag")
        self.buy_petrol_section = (AppiumBy.ACCESSIBILITY_ID, "Buy Petrol")

    def navigate_to_fastag(self):
        logging.info("Navigation on Fastag page")
        """Navigate to FASTag section"""
        self.click(self.fastag_section)
        return FastagHomePage(self.driver)

    def navigate_to_buy_petrol(self):
        """Navigate to Buy Petrol section"""
        self.click(self.buy_petrol_section)
        return FuelHomePage(self.driver)


