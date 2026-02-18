import logging
import time
# from typing import Optional

import pytest
import sys
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from common.base_page import BasePage
# from appium.webdriver.webdriver import WebDriver as AppiumWebDriver

from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.options import Options

# Add POM to Python path so fixtures can import page objects
pom_path = os.path.join(os.path.dirname(__file__), 'POM')
sys.path.insert(0, pom_path)


@pytest.fixture(scope="function")
def appium_driver(request):
    """
    Creates Appium driver for Android testing.
    Scope='session' means one driver for all tests.
    """
    appium_server_url = "http://127.0.0.1:4723"

    # Android device capabilities
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "KZY9SW4DDQ5DJ7JN",  # connected device ID (adb devices - run in terminal)
        "appPackage": "com.ovunque.parkwheels",  # app package name
        "appActivity": ".activities.SplashActivity",
        "autoGrantPermissions": True,
        "noReset": True,
        "disableWindowAnimation": True,
        "ignoreHiddenApiPolicyError": True,
        "skipDeviceInitialization": True,
        "chromedriverAutodownload": True,
        # "chromedriverChromeMappingFile": r"C:\chromedriver\mapping.json"
    })

    print(f"Connecting to Appium server at {appium_server_url}")
    print(f"Target app: {options.app_package}")

    driver = None
    #
    try:
        # Create driver
        driver = webdriver.Remote(appium_server_url, options=options)
        print("Appium driver created successfully")
        yield driver

    except Exception as e:
        print(f"Failed to create Appium driver: {e}")
        print("Make sure:")
        print("1. Appium server is running on localhost:4723")
        print("2. Android device/emulator is connected")
        print("3. Your app is installed on the device")
        raise

    finally:
        # Cleanup - quit driver after all tests
        if driver is not None:
            try:
                reached_home = navigate_back_to_home(driver)

                if not reached_home:
                    print("Failed to move back, resetting the app...")
                    ## noinspection PyUnresolvedReferences
                    BasePage(driver).reset_to_home()
                    print("app reset successfully")

            except Exception as e:
                print(f"Cleanup error: {e}")

            try:
                driver.quit()
                print("driver closed")
            except:
                pass

def navigate_back_to_home(driver, max_attempts = 5):
    from appium.webdriver.common.appiumby import AppiumBy
    import time

    home_page_id = (AppiumBy.ACCESSIBILITY_ID, "Home")

    for attempt in range(max_attempts):
        try:
            element = driver.find_element(*home_page_id)
            if element.is_displayed():
                print("Reached home page")
                return True
        except:
            pass

        try:
            driver.back()
            time.sleep(0.5)
        except:
            print("Back button error")
            return False

    print("Back button error")
    return False

        # try:
        #     driver.quit()
        #     print("Appium driver closed successfully")
        # except:
        #     pass



# @pytest.fixture(scope="function", autouse=True)
# def conditional_reset_app(request, appium_driver):
#     """
#     Resets the app only for tests marked with @pytest.mark.reset_app
#     """
#     # yield  # Test runs here
#
#     if 'reset_app' in request.keywords:
#         try:
#             print("🔄 Resetting app to home screen (via BasePage)...")
#             base_page = BasePage(appium_driver)
#             base_page.reset_to_home()
#             time.sleep(5)
#         except Exception as e:
#             print(f"⚠️ Failed to reset app: {e}")
#     yield

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to get the report
    outcome = yield
    rep = outcome.get_result()

    # only for test call phase and failures
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("appium_driver")  # your driver fixture
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = int(time.time())
            file_name = f"{item.name}_{timestamp}.png"
            path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(path)
            logging.error(f"\nScreenshot saved to {path}")


