from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from features.fastag.fastag_pages.fastag_replace_new_bottom_sheet import ReplaceNewBottomSheet
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from features.fastag.fastag_pages.fastag_other_services_buy_now_select_bank import FastagBankPage
from features.store.store_pages.fastag_product_store_page import FastagProductStorePage


class OtherServices(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.vehicle_number_input = (AppiumBy.XPATH, '//android.widget.EditText[@hint, "fastag_vehicle_number_enter"]')
        self.continue_button = (AppiumBy.ACCESSIBILITY_ID, "Continue")
        self.vehicle_card = (AppiumBy.ACCESSIBILITY_ID, "fastag_select_vehicle_continue_3\nMaruti Swift\nHR26AV8888")
        self.no_vehicle_number_right_now = (AppiumBy.ACCESSIBILITY_ID, "fastag_continue_without_vehicle_number\nI dont't have a vehicle number right now")
        self.no_vrn_incorrect_vrn = (AppiumBy.ACCESSIBILITY_ID, "Make sure the entered car number is correct")
        self.wish_to_buy_replace = (AppiumBy.ACCESSIBILITY_ID, "Do you wish to replace it or buy a new FASTag")
        self.replace_fastag = (AppiumBy.ACCESSIBILITY_ID, "fastag_options_Replace FASTag")
        self.buy_new_fastag = (AppiumBy.ACCESSIBILITY_ID, "fastag_options_Buy new FASTag")

    def enter_vehicle_number(self,vehicle_number):
        if not self.is_displayed(self.vehicle_number_input):
            self.scroll_to_element(AppiumBy.XPATH, '//android.widget.EditText[@hint, "fastag_vehicle_number_enter"]')
        self.type_text(self.vehicle_number_input, vehicle_number)
        self.logger.warning(f"Entering Vehicle number : {vehicle_number}")

    def click_continue_button(self):
        self.click(self.continue_button)
        self.logger.info("Clicked continue button")
        return FastagProductStorePage(self.driver)

    def click_on_no_vehicle_number_rightnow(self):
        self.click(self.no_vehicle_number_right_now)
        self.logger.warning("Clicked no VRN right now")
        return FastagBankPage(self.driver)

    def is_incorrect_no_vrn_message_displayed(self):
        return self.is_displayed(self.no_vrn_incorrect_vrn)

    def click_on_vehicle_card(self):
        self.click(self.vehicle_card)
        self.logger.info("Clicked vehicle card")
        return FastagProductStorePage(self.driver)

    def click_on_replace_fastag(self):
        self.click(self.replace_fastag)
        return FastagProductStorePage(self.driver)

    def vehicle_card_by_index(self, index):
        card_id = f"fastag_select_vehicle_continue_{index}"
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, card_id).click()
        self.logger.warning(f"Clicked vehicle card at index : {index}")
        return self

    def wish_to_replace_buy_bottom_sheet(self):
        # self.is_displayed(self.wish_to_buy_replace)
        # return self
        try:
            self.logger.info("Buy replace bottom sheet displayed")
            return self.is_displayed(self.wish_to_buy_replace)
        except Exception:
            self.logger.warning("Buy replace bottom sheet not displayed")
            return False

    def click_on_replace_fastag(self):
        self.click(self.replace_fastag)
        self.logger.info("Clicked replace fastag")
        return FastagProductStorePage(self.driver)

    def click_on_buy_new_fastag(self):
        self.click(self.buy_new_fastag)
        self.logger.info("clicked on buy new fastag button")
        return FastagProductStorePage(self.driver)









