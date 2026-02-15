from selenium.webdriver.common.by import By
import time
from common.base_page import BasePage
from features.fastag.fastag_pages.fastag_activation_govt_upload import FastagActivationGovtDetails


class FastagActivatePersonal(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.pan_number = (By.CSS_SELECTOR, "input[placeholder='OJTPK1212M']")
        self.submit_button_next_personal = (By.XPATH, "//button[p[text()='Submit']]")
        self.renter_pan = (By.XPATH, "")
        self.continuepan = (By.XPATH, "")
        self.mobile_num = (By.XPATH, "//input[@type='number']")
        self.paname = (By.XPATH, "")
        self.engine_number = (By.XPATH, "//input[@inputmode='text' and @placeholder='']") #BS74B30658
        self.dob = (By.XPATH, "")
        self.submit_button = (By.XPATH, "//button[.//p[normalize-space()='Submit']]")
        self.email = (By.XPATH, "(//input[@inputmode='text'])[1]")
        self.aadhar = (By.XPATH, "(//input[@inputmode='text'])[2]")  #532014464160
        self.bank_error = (By.XPATH, "//p[text()='Retry']/parent::button")

    def enter_pan(self,value):
        self.send_keys(self.pan_number, value)
        self.driver.hide_keyboard()
        return self

    def submit_personal_details_button_next_personal(self):
        self.click(self.submit_button_next_personal)
        return self
        # return FastagActivatePersonal(self.driver)

    def re_enter_pan_bottom_sheet(self):
        self.click(self.renter_pan)
        return self

    def continue_pan_bottom_sheet(self):
        self.click(self.continuepan)
        return self

    def enter_mobile_num(self,value):
        self.send_keys(self.mobile_num, value)
        return self

    def enter_pan_name(self,value):
        self.send_keys(self.paname, value)
        return self

    def enter_engine_number(self,value):
        self.send_keys(self.engine_number, value)
        self.driver.hide_keyboard()
        return self

    def enter_dob(self,value):
        self.send_keys(self.dob, value)
        return self

    def enter_email(self, email):
        self.send_keys(self.email, email)
        return self

    def enter_aadhar(self,value):
        self.send_keys(self.aadhar, value)
        return self

    def submit_button_next_page(self):
        self.click(self.submit_button)
        return FastagActivationGovtDetails(self.driver)

    def fetch_details_error(self):
        self.click(self.bank_error)
        time.sleep(1)
        self.click(self.submit_button_next_page())
        return self


