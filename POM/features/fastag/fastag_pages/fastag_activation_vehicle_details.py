from selenium.webdriver.common.by import By
import time
from common.base_page import BasePage
from features.fastag.fastag_pages.fastag_activation_personal import FastagActivatePersonal


class FastagActivateVehicle(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.private_vehicle = (By.XPATH, "//div[@class='Radio_radio_wrapper__hsK9i'][.//p[normalize-space()='Private vehicle']]")
        self.commercial_vehicle = (By.XPATH, "//div[@class='Radio_radio_wrapper__hsK9i'][.//p[normalize-space()='Commercial vehicle']]")
        self.vrn_activate_number = (By.CSS_SELECTOR, "input[placeholder='XXXXXXXXXX']")
        self.submit_button = (By.XPATH, "//button[.//p[normalize-space()='Submit']]")
        # self.rc_front_img = (By.ID, "")
        # self.rc_back_image = (By.ID, "input-image")

    def go_to_private_vehicle(self):
        self.click(self.private_vehicle)
        return self

    def go_to_commercial_vehicle(self):
        self.click(self.commercial_vehicle)
        return self

    def go_to_vrn_activation_number(self, vehicle_number):
        self.send_keys(self.vrn_activate_number, vehicle_number)

    def go_to_submit_button(self):
        self.click(self.submit_button)
        return FastagActivatePersonal(self.driver)