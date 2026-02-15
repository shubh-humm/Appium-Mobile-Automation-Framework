from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import logging

class IoclOnboardingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.cashback_program = (AppiumBy.ACCESSIBILITY_ID, "Redeem now") #text to validate that we have landed onto the right page
        self.vehicle_number = (AppiumBy.ACCESSIBILITY_ID, "dropdown_selector_Select vehicle number") #opens a bs, select your car field
        self.vehicle_card_id = (AppiumBy.ACCESSIBILITY_ID, "vehicle_card_{}") #for the list of vehicles in the bs
        self.full_name = (AppiumBy.XPATH, "//android.widget.EditText[@hint='full_name_input_field']") #input field to be added
        self.gender_m = (AppiumBy.ACCESSIBILITY_ID, "Male")
        self.gender_f = (AppiumBy.ACCESSIBILITY_ID, "Female")
        self.gender_o = (AppiumBy.ACCESSIBILITY_ID, "Others")
        self.close_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.petrol_cashback = (AppiumBy.ACCESSIBILITY_ID, "Cashback Program") #heading of iocl onboarding to verify that we have landed on the right page.
        self.tandc = (AppiumBy.ACCESSIBILITY_ID, "tnc_clickable_text")
        self.terms_conditions = (AppiumBy.ACCESSIBILITY_ID, "Terms & Conditions")
        self.close_tandc = (AppiumBy.ACCESSIBILITY_ID, "close_bottomsheet_global")
        self.next_button = (AppiumBy.ACCESSIBILITY_ID, "Next")
        self.your_vehicles = (AppiumBy.ACCESSIBILITY_ID, "Your vehicles") #text on the bs, when clicked on select your car field
        self.choose_vehicle = (AppiumBy.ACCESSIBILITY_ID, "")
        """enter HR12AV8196"""
        self.select_button = (AppiumBy.ACCESSIBILITY_ID, "Select") #CTA on your vehicles bs, when selected a vehicle.
        self.add_new_vehicle = (AppiumBy.ACCESSIBILITY_ID, "Add new vehicle") #cta present when the vehicle bs is not displayed
        self.enter_vehicle = (AppiumBy.ACCESSIBILITY_ID, "")
        self.vehicle_input = (AppiumBy.ACCESSIBILITY_ID, "") #input field to be added
        self.add_now_vehicle = (AppiumBy.ACCESSIBILITY_ID, "Add now")
        self.verify_pin = (AppiumBy.XPATH, "//*[@class='android.widget.EditText' and contains(@hint,'Your PIN code')]") #text to validate that we have landed onto the right page
        self.enter_pin = (AppiumBy.XPATH, "//*[@class='android.widget.EditText' and contains(@hint,'Eg.')]") #input field
        self.select_date = (AppiumBy.XPATH, "//*[@class='android.widget.ImageView' and @hint='DD/MM/YYYY']") #create for the calendar
        self.ok_btn_calendar = (AppiumBy.ACCESSIBILITY_ID, "OK")
        self.cancel_btn_calendar = (AppiumBy.ACCESSIBILITY_ID, "Cancel")
        self.submit_button = (AppiumBy.ACCESSIBILITY_ID, "Submit")
        self.cant_create_account = (AppiumBy.ACCESSIBILITY_ID, "")
        self.understood_button = (AppiumBy.ACCESSIBILITY_ID, "")

    def validate_iocl_onboarding(self):
        self.is_displayed(self.cashback_program)

    def click_select_car(self):
        self.click(self.vehicle_number)
        self.logger.info("Selecting car...")

    def select_vehicle_card_by_index(self, index):
        card_id = f"vehicle_card_{{{index}}}"
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, card_id).click()
        self.logger.warning(f"Clicked vehicle card at index : {index}")
        return self

    def click_car_selected(self):
        self.click(self.select_button)

    def enter_name(self, name):
        self.send_keys(self.full_name, name)
        self.logger.warning(f"Entered name : {name}")

    def click_male_gender(self):
        self.logger.ino("Selected Male Gender")
        self.click(self.gender_m)

    def click_female_gender(self):
        self.click(self.gender_f)
        self.logger.info("Clicked Female Gender")

    def click_others_gender(self):
        self.click(self.gender_o)
        self.logger.info("Clicked Other's Gender")

    def click_next_vehicle_details(self):
        self.click(self.next_button)
        self.logger.info("Submitting vehicle details")

    def enter_pincode(self, pincode):
        self.wait_for_clickable(self.enter_pin, pincode)
        self.send_keys(self.enter_pin, pincode)
        self.logger.warning(f"entering PIN Code: {pincode}")

    def click_dob(self):
        self.click(self.select_date)
        logging.info("clicked dob")

    def click_confirm_date(self):
        self.click(self.ok_btn_calendar)
        logging.info("Clicked ok and confirmed the date")

    def click_terms_conditions(self):
        self.click(self.terms_conditions)
        logging.info("Clicked on Terms and Conditions")

    def click_close_tandc(self):
        self.click(self.close_tandc)
        logging.info("Clicked close tandc BS")




