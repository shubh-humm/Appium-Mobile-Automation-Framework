from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from features.store.store_pages.fastag_product_store_page import FastagProductStorePage


class FastagBankPage(BasePage): #THIS PAGE -> : FASTag > OTHER SERIVCES > bUY NOW > i DONT HAVE A VRN
    def __init__(self, driver):
        super().__init__(driver)

        self.bank_input_field = (AppiumBy.ACCESSIBILITY_ID, "")
        self.no_fastag_button = (AppiumBy.ACCESSIBILITY_ID, "I don't have a FASTag")
        self.select_bank_button = "fastag_enter_bank_name_select_{}"

    def click_bank_input_field(self):
        self.click(self.bank_input_field)

    def click_no_fastag_button(self):
        self.click(self.no_fastag_button)
        return FastagProductStorePage(self.driver)

    def click_fastag_bank(self, index = 0):
        accessibility_id = self.select_bank_button.format(index)
        self.click((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
        return FastagProductStorePage(self.driver)

