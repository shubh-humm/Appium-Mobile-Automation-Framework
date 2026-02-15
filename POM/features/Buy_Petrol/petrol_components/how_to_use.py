from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

""""""
class HowToUsePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.steps_to_use = (AppiumBy.ACCESSIBILITY_ID, "Steps to use voucher\nThis voucher can be used at any IndianOil petrol pump.")
        self.terms_and_conditions = (AppiumBy.ACCESSIBILITY_ID, "")
        self.back_button = (AppiumBy.ACCESSIBILITY_ID, "")

    def click_steps_to_use(self):
        self.click(self.steps_to_use)
        """put the returns statement here"""

    def click_terms_and_conditions(self):
        self.click(self.terms_and_conditions)
        """put the return statement here"""

    def click_back_button(self):
        self.click(self.back_button)
        """put the return statement here"""