from common.base_page import BasePage
from selenium.webdriver.common.by import By

class FastagActivationGovtDetails(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.vehicle_front = (By.ID, "input-image")
        self.vehicle_side = (By.ID, "input-image")
        self.barcode_image = (By.ID, "input-image")
        self.govt_docs = (By.XPATH, "//p[normalize-space()='Government documents']")
        self.submit_final = (By.XPATH, "//button[.//p[text()='Submit']]")

    def click_submit_final_button(self):
        self.click(self.submit_final)
        return self

