from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage
from features.Buy_Petrol.petrol_pages.nearby_iocl_pump_page import NearbyIoclPumpPage


class ReportedPetrolPumpBs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.find_iocl_pp = (AppiumBy.ACCESSIBILITY_ID, "")
        self.close_btn = (AppiumBy.ACCESSIBILITY_ID, "")
        self.pp_reported = (AppiumBy.ACCESSIBILITY_ID, "") #text to validate the opening of the bs

    def click_find_iocl_pp(self):
        self.click(self.find_iocl_pp)
        return NearbyIoclPumpPage(self.driver)

    def click_close_btn(self):
        self.click(self.close_btn)
        return FuelHomePage(self.driver)