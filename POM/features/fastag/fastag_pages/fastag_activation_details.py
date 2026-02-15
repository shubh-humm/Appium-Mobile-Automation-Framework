# from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from features.fastag.fastag_pages.fastag_activation_vehicle_details import FastagActivateVehicle


class FastagActivationDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.barcode_input = (By.XPATH, "(//div[@class='Input_input__Nyguv']/input)[1]")
        self.confirm_barcode_input = (By.XPATH, "(//div[@class='Input_input__Nyguv']/input)[2]")
        self.submit_button = (By.CSS_SELECTOR, "button[class*='Button_primary']")
        self.upload_fastag = (By.ID, '#input-image')
        self.fastag_details_page = (By.CSS_SELECTOR, '//android.widget.TextView[@text="FASTag details"]')

    def go_to_submit_fastag(self):
        self.click(self.submit_button)
        return FastagActivateVehicle(self.driver)

    def verify_fastag_details_page(self):
        self.is_displayed(self.fastag_details_page)

    def upload_image(self, imagee):
        self.send_keys(self.upload_fastag, imagee)
        return self

    def enter_bar_code_input(self,value):
        self.send_keys(self.barcode_input, value)
        return self

    def confirm_bar_code_input(self,value):
        self.send_keys(self.confirm_barcode_input, value)
        return self
