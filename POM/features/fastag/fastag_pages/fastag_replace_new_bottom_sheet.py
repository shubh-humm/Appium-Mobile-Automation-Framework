from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from features.store.store_pages.fastag_product_store_page import FastagProductStorePage


class ReplaceNewBottomSheet(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.replace_fastag = (AppiumBy.ACCESSIBILITY_ID, "fastag_options_Replace FASTag\nReplace FASTag\nIDBI Bank will deduct Rs 100 from your existing balance")
        self.buy_new_fastag = (AppiumBy.ACCESSIBILITY_ID, "fastag_options_Buy new FASTag\nBuy new FASTag\nYour existing fastag balance will be transferred to your bank account")
        self.wish_for_fastag = (AppiumBy.ACCESSIBILITY_ID, "Do you wish to replace it or buy a new FASTag")

    def click_on_replace_fastag(self):
        self.click(self.replace_fastag)
        return FastagProductStorePage(self.driver)

    def click_on_buy_new_fastag(self):
        self.click(self.buy_new_fastag)
        return FastagProductStorePage(self.driver)

    def is_bottom_sheet_loaded(self):
        return self.is_displayed(self.wish_for_fastag)
