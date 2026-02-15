from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

from features.Buy_Petrol.petrol_components.no_petrol_accept_bs import NoPetrolAccept

"""comes from the help icon"""
class HelpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.issues_faced = (AppiumBy.ACCESSIBILITY_ID, "What issue are you facing?") #text to validate bs
        self.petrol_not_accepting = (AppiumBy.ACCESSIBILITY_ID, "Petrol pump not accepting voucher")
        self.machine_issues = (AppiumBy.ACCESSIBILITY_ID, "ITPS machine not working")
        self.operator_issues = (AppiumBy.ACCESSIBILITY_ID, "Operator does not know how to operate ITPS machines")
        self.used_voucher = (AppiumBy.ACCESSIBILITY_ID, "My voucher is Marked used, but I didn't get petrol")
        self.new_voucher_sheet = (AppiumBy.ACCESSIBILITY_ID, "You'll get a new voucher") #BS opens when tapped on, voucher marked used
        self.got_it_cta = (AppiumBy.ACCESSIBILITY_ID, "Got it") #CTA on the above BS

    def click_petrol_not_accepting(self):
        self.click(self.petrol_not_accepting)
        self.logger.info("Clicked PP not accepting voucher")
        return NoPetrolAccept(self.driver)

    def click_machine_issues(self):
        self.click(self.machine_issues)
        self.logger.info("Clicked Machine Issues")
        return NoPetrolAccept(self.driver)

    def click_operator_issues(self):
        self.click(self.operator_issues)
        self.logger.info("Clicked operator Issues")
        return NoPetrolAccept(self.driver)

    def click_voucher_marked_used(self):
        self.click(self.used_voucher)
        self.logger.info("Clicked voucher marked used")
        return self

    def click_got_it(self):
        """CTA on the bottom sheet which appears when tapped on voucher marked used"""
        self.click(self.got_it_cta)
        return self



