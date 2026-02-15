import logging

from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class TotalFuelSavingsBs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.close_sheet_btn = (AppiumBy.ACCESSIBILITY_ID, "")
        self.got_it_btn = (AppiumBy.ACCESSIBILITY_ID, "Got it") #closes the BS
        self.total_savings_text = (AppiumBy.ACCESSIBILITY_ID, "Your total savings") #use the one at the top of the BS

    def click_close_sheet_btn(self):
        self.click(self.close_sheet_btn)
        """put the return statement here"""

    def click_got_it(self):
        self.click(self.got_it_btn)
        self.logger.info("Clicked on got it.")
        """put the return statement here"""

    def handle_savings_bs(self):
        try:
            if self.wait_for_visibility(self.total_savings_text, timeout=4):
                logging.info("Total Savings BS appeared")
                self.click(self.got_it_btn)
                return True
            else:
                logging.info("Total Savings BS did not appear or disappeared too fast")
                return False
        except:
            logging.info("Total Savings BS already closed")
            return False