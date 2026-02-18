from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    filename= "automation.log",
    filemode="w"
)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 30)
        self.logger = logging.getLogger(self.__class__.__name__)

    def click(self,locator, timeout = 10):
        # element = WebDriverWait(self.driver, timeout).until(
        #     EC.element_to_be_clickable(locator)
        # )
        # element.click()
        for attempt in range(3):
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                return element
            except StaleElementReferenceException:
                if attempt == 2:  # Last attempt
                    raise
                self.logger.error("Could not click on the button")
                # time.sleep(1)

    def send_keys(self, locator, text, timeout = 10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        self.driver.hide_keyboard()

    def send_keys_without_keyboard(self, locator, text, timeout = 10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        """this method prevents hide_keyboard from taking to previous page"""

    def get_text(self, locator, timeout = 5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def is_displayed(self,locator, timeout = 5):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False

    def type_text(self, locator, text, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        # time.sleep(0.2)
        element.clear()
        WebDriverWait(self.driver, 5).until(lambda x: element.text == "")
        element.send_keys(text)

    def reset_to_home(self):
        logging.info("Resetting app to home screen...")

        self.driver.terminate_app("com.ovunque.parkwheels")
        # time.sleep(1.2)
        self.driver.activate_app("com.ovunque.parkwheels")

        # Wait for app to fully load (adjust time based on your device speed)
        logging.info("Waiting for app to fully load...")

    def wait_for_visibility(self, locator, timeout=20):
        self.logger.info("waiting for the element / page to load")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_visibility_optional(self, locator, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_invisibility(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def wait_for_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )


    def scroll_to_element(self, by, locator, max_swipes=10):
        """Scroll until the element is visible or max_swipes is reached."""
        for _ in range(max_swipes):
            try:
                element = self.driver.find_element(by, locator)
                if element.is_displayed():
                    return element
            except:
                # Swipe up to scroll
                size = self.driver.get_window_size()
                start_x = size['width'] * 0.5
                start_y = size['height'] * 0.8
                end_y = size['height'] * 0.2
                self.driver.swipe(start_x, start_y, start_x, end_y, duration=800)
                time.sleep(1)
        raise Exception(f"Element with locator {locator} not found after {max_swipes} swipes")

    def clear_input(self, locator, timeout = 10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

        element.click()
        # time.sleep(0.2)

        try:
            element.clear()
        except:
            pass

    def is_cta_enabled(self, locator, timeout = 5):

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            # enabled_att = element.get_attribute("enabled") """this is the verify if the cta is truly displaying its current state.
            # print(f"enabled at {enabled_att}")
            return element.get_attribute("enabled") == "true"
        except TimeoutException:
            return False



