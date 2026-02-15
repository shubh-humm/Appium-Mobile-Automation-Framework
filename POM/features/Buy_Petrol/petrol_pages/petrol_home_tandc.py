from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

# from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage


class TandCPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """put the elements here"""

        self.back_btn = (AppiumBy.ACCESSIBILITY_ID, "back_button_appbar_global")
        self.terms_conditions = (AppiumBy.ACCESSIBILITY_ID, "Terms and conditions")

    def click_back_btn(self):
        self.click(self.back_btn)
        # return FuelHomePage(self.driver)