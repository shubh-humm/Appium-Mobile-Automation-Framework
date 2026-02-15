from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage


class FastagProductStorePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver #appium driver instance
        self.pincode_input = (AppiumBy.ACCESSIBILITY_ID, "")
        self.check_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.buy_now_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Buy Now"]')
        self.add_to_cart_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Add to cart"]')
        self.add_to_cart_icon = (AppiumBy.XPATH, '//android.view.View[@resource-id="__next"]/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.widget.Image')
        self.product_back_button = (AppiumBy.XPATH, '//android.widget.Button[@text="back-button"]')
        self.delivery_avail = (AppiumBy.ACCESSIBILITY_ID, "Check delivery availability")


    def click_on_pincode_input_field(self):
        enter_pincode = ""
        self.driver.find_element(*self.pincode_input).send_keys(enter_pincode)

    def click_on_check_button_field(self):
        self.driver.find_element(*self.check_button).click()

    def click_on_buy_now_button(self):
        from features.fastag.fastag_pages.fastag_other_services_buy_now_select_bank import FastagBankPage
        self.driver.find_element(*self.buy_now_button).click()

    def click_on_add_to_cart_button(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        return self

    def click_on_add_to_cart_icon(self):
        self.driver.find_element(*self.add_to_cart_icon).click()
