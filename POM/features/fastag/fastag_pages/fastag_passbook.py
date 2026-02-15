from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

class FastagPassbook(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.instant_cash_banner = (AppiumBy.ACCESSIBILITY_ID, "")
        self.passbook_page = (AppiumBy.ACCESSIBILITY_ID, "FASTag Passbook")
        self.check_balance = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_check_balance\nCheck balance")
        self.change_fastag_pass = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_change\nChange")
        self.bottom_sheet_close = (AppiumBy.ACCESSIBILITY_ID, "bottomsheet_close_btn")
        self.refresh_bottom_sheet_button = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_check_balance_bs_refresh\nRefresh")
        self.another_vehicle_pass = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_change_bs_item_2")

    def tap_instant_cash(self):
        self.click(self.instant_cash_banner)

    def tap_check_balance(self):
        self.click(self.check_balance)
        self.logger.info("Checking balance...")
        return self

    def tap_refresh_balance(self):
        self.click(self.refresh_bottom_sheet_button)
        self.logger.info("Refreshing balance...")
        return self

    def tap_change_fastag_pass(self):
        self.logger.info("Tapped to change fastag")
        self.click(self.change_fastag_pass)
        return self

    def close_balance_bottom_sheet(self):
        self.logger.info("Closing balance Bottom Sheet")
        self.click(self.bottom_sheet_close)
        return self

    def selecting_another_vehicle_fastag_card(self):
        self.logger.info("selecting another vehicle")
        self.click(self.another_vehicle_pass)
        return self

