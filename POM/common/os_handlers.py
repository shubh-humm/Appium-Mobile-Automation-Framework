import time
import subprocess
import re
from turtledemo.penrose import start

from appium.webdriver.common.appiumby import AppiumBy
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class OsHandler:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def allow_google_location(self):
        """for allowing google location consent dialog box"""
        try:
            allow_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))
            )
            allow_btn.click()
            logging.info("google consent location allowed")
        except TimeoutException:
            logging.info("Google consent dialog box did not appeared")

    def handle_media_permission(self):
        permission_btns = [
            "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
            ""
        ]

        for permissions in range(2):
            for btn_id in permission_btns:
                try:
                    btn = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable(AppiumBy.ACCESSIBILITY_ID, btn_id)
                    )
                    btn.click()
                    logging.info("OS permission allowed allowed")
                    time.sleep(1)
                    break
                except TimeoutException:
                    pass


    def select_gallery_chooser(self):
        try:
            gallery = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Media picker")'))
            )
            gallery.click()
            logging.info("OS gallery selected")
        except TimeoutException:
            logging.info("OS chooser did not appeard")


    def select_gallery_image(self):
        try:
            gallery_img = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.providers.media.module:id/icon_thumbnail"])[1]'))
            )
            gallery_img.click()
            logging.info("Image selected")
        except TimeoutException:
            logging.info("Cannot find the image")

    def crop_image(self):
        try:
            crop_img = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, "com.ovunque.parkwheels:id/crop_image_menu_crop"))
            )
            crop_img.click()
            logging.info("Image cropped")
        except TimeoutException:
            logging.info("Cannot crop the image")


    def handle_image_flow(self):
        # self.handle_media_permission()
        self.select_gallery_chooser()
        self.select_gallery_image()
        self.crop_image()
        logging.info("Handled OS pop-ups successfully")



"""HANDLE DOWNLOADED PDF"""

download_dir = "/sdcard/Download"
file_name_pattern = r"fuel_invoice_\d+\.pdf"

def list_invoices():
    cmd = f"adb shell ls {download_dir}"
    output = subprocess.check_output(cmd, shell=True).decode(errors="ignore")

    return set(
        file for file in output.split()
        if re.match(file_name_pattern, file)
    )

def wait_for_new_invoice(before_files, timeout = 15, poll_interval = 1):

    start = time.time()

    while time.time() - start < timeout:
        after_files = list_invoices()
        new_files = after_files - before_files

        if new_files:
            return new_files

        time.sleep(poll_interval)

    return set

def validate_fuel_invoice_downloaded(driver, app_package):

    before_files = list_invoices()

    current_package = driver.current_package
    if current_package == app_package:
        raise AssertionError("Browser did not open after clicking download")

    new_files = wait_for_new_invoice(before_files)

    if not new_files:
        raise AssertionError("Fuel invoice pdf was not downloaded")

    return new_files

