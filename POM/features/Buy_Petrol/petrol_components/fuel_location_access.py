from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class FuelLocationAccessBs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.allow_location_text_access = (AppiumBy.ACCESSIBILITY_ID, "") #text to validate the BS
        self.share_my_location = (AppiumBy.ACCESSIBILITY_ID, "Share my location") #cta to allow locatin
        self.dismiss_location = (AppiumBy.ACCESSIBILITY_ID, "Dismiss") #Cta to deny access

    def click_allow_location(self):
        self.click(self.share_my_location)
        self.logger.warning("Allowing location access")
        """do not retun anything, allow seperately the googel consent dialog box."""

    def click_dismiss_location(self):
        self.click(self.dismiss_location)
        self.logger.warning("Location access dismissed")
        """no need for return"""