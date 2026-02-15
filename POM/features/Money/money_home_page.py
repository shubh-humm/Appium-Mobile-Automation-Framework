from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage

class MoneyHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.money_page = (AppiumBy.XPATH, "//android.widget.TextView[@text='INSTANT CASH']")

    def money_page_displayed(self):
        self.is_displayed(self.money_page)

