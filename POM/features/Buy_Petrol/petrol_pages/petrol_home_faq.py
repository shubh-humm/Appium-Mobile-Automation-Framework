from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

# from features.Buy_Petrol.petrol_pages.fuel_home_page import FuelHomePage


class AskedQues(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        """put the elements here"""

        self.recent_faq_ques = (AppiumBy.ACCESSIBILITY_ID, "Frequently asked questions")
        self.back_btn = (AppiumBy.ACCESSIBILITY_ID, "back_button_appbar_global")

    def click_back_btn(self):
        self.click(self.back_btn)
        # return FuelHomePage(self.driver)
