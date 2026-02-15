from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
# from features.fastag.fastag_pages.fastag_home_page import FastagHomePage
from features.fastag.fastag_pages.fastag_other_services_buy_now import OtherServices


class FastagTagClosed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.tag_closed_heading = (AppiumBy.XPATH, '//android.widget.TextView[@text="Why is your FASTag Closed"]')
        self.closed_buy_new_tag = (AppiumBy.XPATH, '//android.widget.Button[@text="Buy New FASTag"]')

    def click_buy_new_closed_tag(self):
        self.click(self.closed_buy_new_tag)
        return
