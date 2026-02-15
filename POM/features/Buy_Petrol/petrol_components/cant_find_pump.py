from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_pages.nearby_iocl_pump_page import NearbyIoclPumpPage

"""couldnt find nearby petrol pump bottom sheet"""
class CantFindPP(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.add_pump_details = (AppiumBy.ACCESSIBILITY_ID, "Add petrol pump details and we'll do the rest.") #this is text on reporting bs
        self.name_input = (AppiumBy.XPATH,  '//android.widget.EditText[contains(@hint, "pump_name_input_field\nName\n *\nName of the petrol pump")]')
        self.pp_address_input = (AppiumBy.XPATH,  '//android.widget.EditText[contains(@hint, "Address of the petrol pump")]')
        self.upload_btn = (AppiumBy.ACCESSIBILITY_ID, "Upload")
        self.submit_button = (AppiumBy.ACCESSIBILITY_ID, "Submit")
        self.field_required_error_msg = (AppiumBy.ACCESSIBILITY_ID, "") #appears when clicked on submit without inout
        self.find_iocl_pumps = (AppiumBy.ACCESSIBILITY_ID, "Find IndianOil pumps near me") #CTA on Bs which appears after reporting pump
        self.pump_reported = (AppiumBy.ACCESSIBILITY_ID, "Petrol pump reported!") #text on bs to assert pump is reported

    def enter_name(self, name):
        self.send_keys_without_keyboard(self.name_input, name)
        self.logger.info(f"Entered name: {name}")
        """put details if any"""

    def enter_pump_address(self, pp_address):
        self.send_keys_without_keyboard(self.pp_address_input, pp_address)
        self.logger.warning(f"entering Petrol Pump Address: {pp_address}")
        """"""

    def click_submit_button(self):
        self.click(self.submit_button)
        self.logger.warning("Clicked on submit button")
        """put navigation here"""

    def click_upload_docs(self):
        self.click(self.upload_btn)
        self.logger.info("Clicked on upload button")

    def click_find_iocl_pumps(self):
        self.click(self.find_iocl_pumps)
        self.logger.info("Clicked on nearby IOCL pumps")
        return NearbyIoclPumpPage(self.driver)


