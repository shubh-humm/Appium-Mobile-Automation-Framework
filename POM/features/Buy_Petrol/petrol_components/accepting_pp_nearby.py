from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class AcceptingPpNearby(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.nearyou_pp = (AppiumBy.ACCESSIBILITY_ID, "Petrol pumps near you")
        self.currently_accepting = (AppiumBy.ACCESSIBILITY_ID, "Currently accepting fuel vouchers")
        self.close_bs = (AppiumBy.ACCESSIBILITY_ID, "close_bottomsheet_global")

    def click_close_bs(self):
        if self.wait_for_visibility_optional(self.nearyou_pp):
            self.logger.info("Nearby petrol pump bs appeard")
            self.click(self.close_bs)
            self.logger.info("Closing nearby pp bs")
        else:
            self.logger.info("Nearby petrol pump bs did not appeard -- it appears for users with active vouchers only")

    def select_nearby_accepting_pp(self,index):
        fuel_id = f"nearby_fuel_pump_card_{index}"
        self.click(AppiumBy.ACCESSIBILITY_ID, fuel_id)
        self.logger.info(f"selected fuel id with index : {index}")
        # return