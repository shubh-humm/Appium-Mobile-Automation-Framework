from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time


def test_challan_web(chrome_driver):
    pageone = chrome_driver
    url = "https://sandbox-5.parkplus.io/app/services/challan"
    chrome_driver.get(url)
    time.sleep(5)
    print("Available ", chrome_driver.contexts)
    for ctx in chrome_driver.contexts:
        if "WEBVIEW" in ctx:
            chrome_driver.switch_to.context(ctx)
            print("Switched to:", ctx)
            break
    else:
        raise Exception("❌ No WEBVIEW context found! Page not loaded or hybrid view not active")

    # el = chrome_driver.find_element(By.XPATH, "//p[text()='Enter your vehicle number']")
    # el.click()
    element = chrome_driver.find_element(By.XPATH, "//*[@data-testid='challan_search_bar']")
    element.click()
    time.sleep(5)
    print(chrome_driver.page_source)
    # chrome_driver.switch_to.context('WEBVIEW_chrome')
    # print("Swtiched to : ", chrome_driver.current_context)
    # time.sleep(12)
    # print(chrome_driver.page_source)
    # element = chrome_driver.find_element(By.CSS_SELECTOR, "challan_search_bar")
    # element.click()


