from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from features.fastag.fastag_pages.fastag_activation_details import FastagActivationDetails


class ActivateFastagPages(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.next_activate_button = (By.XPATH, "//button[.//p[normalize-space()='Next']]")
        self.how_it_works = (AppiumBy.XPATH, '//android.widget.Button[@text="How it works?"]')

    def click_next_button(self):
        self.click(self.next_activate_button)
        print("Clicked on next, waiting for next page to load")
        return FastagActivationDetails(self.driver)