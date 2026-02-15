import logging

from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.cant_find_pump import CantFindPP
from features.Buy_Petrol.petrol_components.fuel_location_access import FuelLocationAccessBs

# from features.Buy_Petrol.petrol_pages.nearby_pp import NearbyPetrol

"""petrol pump not accepting voucher BS"""
class NoPetrolAccept(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.not_accepting_voucher = (AppiumBy.ACCESSIBILITY_ID, "Petrol pump not accepting voucher?") #text on the bottom sheet to validate it opened or not
        self.enable_location = (AppiumBy.ACCESSIBILITY_ID, "Allow location access") #allow locatoin CTA displayed when the location is off
        self.choose_petrol_pump = (AppiumBy.ACCESSIBILITY_ID, "Couldn’t find your pump?") #list of petrol pumps displayed when the location is on
        self.report_pp = (AppiumBy.ACCESSIBILITY_ID, "Report a petrol pump")  # report petrol pump CTA, opens another BS to report a pp
        self.pumpwithin_3km = (AppiumBy.ACCESSIBILITY_ID, "Pumps within radius of 3km")
        self.pumps_within_radius = (AppiumBy.ACCESSIBILITY_ID, "") #list of petrol pumps displayed when tapped on report a petrol pump
        self.cant_find_nearby_pp = (AppiumBy.ACCESSIBILITY_ID, "Couldn’t find your pump?")  #"couldnt find your pump"
        self.location_access = FuelLocationAccessBs(self.driver)

    def click_enable_location(self):
        self.click(self.enable_location)
        return FuelLocationAccessBs(self.driver)

    def click_report_pp(self):
        self.click(self.report_pp)
        return

    def click_couldnt_find_pp(self):
        if not self.is_displayed(self.cant_find_nearby_pp):
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "Couldn’t find your pump?")
            logging.info("Scrolling to Couldn't find your pump?")
        self.click(self.choose_petrol_pump)
        self.logger.info("Clicked on couldnt find Petrol Pump")
        return CantFindPP(self.driver)




