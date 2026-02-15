from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy


def main():
    # ✅ Use UiAutomator2Options explicitly
    options = UiAutomator2Options()
    options.platformName = "Android"
    options.deviceName = "b417d7fb0a20"
    options.automationName = "UiAutomator2"
    options.browserName = "Chrome"
    options.chromedriver_autodownload = True
    options.newCommandTimeout = 300
    options.nativeWebScreenshot = True

    # 🚫 Prevent clearing Chrome data
    options.noReset = True
    options.skipDeviceInitialization = True
    options.skipServerInstallation = True
    options.ignore_hidden_api_policy_error = True

    print("🚀 Launching Chrome in browser automation mode...")

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.get("https://parkplus.io/app/services/fastag/activation/home")
    print("🌐 Opened ParkPlus successfully!")

    time.sleep(5)
    print(driver.contexts)
    print("Current context:", driver.current_context)
    print("Currenlty we are into native...")
    driver.switch_to.context("WEBVIEW_chrome")
    time.sleep(5)
    print("Current context:", driver.current_context)

    time.sleep(5)
    # print(driver.page_source)

    driver.find_element(By.CSS_SELECTOR, "button[class*='Button_primary']").click()
    time.sleep(2)
    # print(driver.page_source)

    # print(driver.page_source)
    barcode = driver.find_element(By.XPATH, "(//div[@class='Input_input__Nyguv']/input)[1]").send_keys("150000000000")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@class='Input_input__Nyguv']/input)[2]").send_keys("15 0000000000")

    # time.sleep(20)
    # driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Upload"]').click()

    # pageone = driver.find_element(AppiumBy.CSS_SELECTOR, "button[class*='Button_primary']").click()

if __name__ == "__main__":
    main()