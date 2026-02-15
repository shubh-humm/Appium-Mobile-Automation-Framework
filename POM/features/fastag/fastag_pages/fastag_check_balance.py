from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from features.fastag.fastag_pages.fastag_passbook import FastagPassbook


class FastagCheckBalance(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.refresh_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.close_button = (AppiumBy.ACCESSIBILITY_ID, "")

    def refresh_balance(self):
        self.click(self.refresh_button)
        return self

    def close_balance(self):
        self.click(self.close_button)
        return FastagPassbook(self)


