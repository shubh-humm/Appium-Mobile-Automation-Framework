from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from features.fastag.fastag_pages.fastag_activation import ActivateFastagPages
from selenium.webdriver.support import expected_conditions as EC

def test_open_web(chrome_driver):
    url = "https://parkplus.io/app/services/fastag/activation/home"
    chrome_driver.get(url)
    print(f"opened {url}")

    print("Available ", chrome_driver.contexts)
    for ctx in chrome_driver.contexts:
        if "WEBVIEW" in ctx:
            chrome_driver.switch_to.context(ctx)
            print("Switched to:", ctx)
            break
    else:
        raise Exception("❌ No WEBVIEW context found! Page not loaded or hybrid view not active")


    pageone = ActivateFastagPages(chrome_driver)
    pagetwo = pageone.click_next_button()
    print("Clicked on next button")
    pagetwo.wait_for_visibility(pagetwo.barcode_input)
    print("going to enter bar code number...")
    pagetwo.enter_bar_code_input("TEST15-000-0000000")
    pagetwo.confirm_bar_code_input("TEST15-000-0000000")
    time.sleep(8)
    pagethree = pagetwo.go_to_submit_fastag()
    print("Submited fastag details")
    pagethree.wait_for_visibility(pagethree.private_vehicle)
    pagethree.go_to_private_vehicle()
    pagethree.go_to_vrn_activation_number("HR12AV8196")
    time.sleep(15)
    pagefour = pagethree.go_to_submit_button()
    time.sleep(3)
    pagefour.wait_for_visibility(pagefour.pan_number)
    print("entering personal details...")
    pagefour.enter_pan("LFCPK4475H")
    pagefour.wait_for_visibility(pagefour.mobile_num)
    pagefour.enter_mobile_num("9315229016")
    pagefour.enter_engine_number("BS74B30658")
    time.sleep(3)
    pagefive = pagefour.submit_personal_details_button_next_personal()
    print("redirecting to the next page")
    time.sleep(20)
    pagefive.wait_for_visibility(pagefive.email)
    print("entering email...")
    pagefive.enter_email("shubhamkhaneja29@gmail.com")
    pagefive.wait_for_visibility(pagefive.aadhar)
    print("entering aadhar number...")
    pagefive.enter_aadhar("532014464160")
    pagesix = pagefive.submit_button_next_page()
    print("upload the images...")

    # pagefive.wait_for_visibility(pagefive)












    # barcode.send_keys("TEST15-000-0000000")
    # confirm_code = chrome_driver.find_element(By.XPATH, "(//div[@class='Input_input__Nyguv']/input)[2]")
    # confirm_code.send_keys("TEST15-000-0000000")
    #
    # time.sleep(10)
    #
    # submit_cta = chrome_driver.find_element(By.CSS_SELECTOR, "button[class*='Button_primary']")
    # submit_cta.click()
    # print("clicked on the submit button")
    #
    # time.sleep(8)
    #
    # # choose_vehicle_type = chrome_driver.find_element((By.XPATH, "//div[@class='Radio_radio_wrapper__hsK9i'][.//p[normalize-space()='Private vehicle']]"))
    # # choose_vehicle_type = chrome_driver.find_element(By.XPATH, "//label[.//p[normalize-space()='Private vehicle']]//input")
    # choose_vehicle_type = chrome_driver.find_element(
    #     By.XPATH,
    #     "//p[normalize-space()='Private vehicle']/ancestor::label//div[contains(@class,'Radio_radio')]"
    # )
    # choose_vehicle_type.click()
    # enter_vrn = chrome_driver.find_element(By.CSS_SELECTOR, "input[placeholder='XXXXXXXXXX']")
    # enter_vrn.send_keys("HR12AV8196")
    # print("uploading vehicle images")
    # time.sleep(15)
    # submit_vehicle = chrome_driver.find_element(By.CSS_SELECTOR, "button[class*='Button_primary']")
    # submit_vehicle.click()
    # time.sleep(8)
    # pan_num = chrome_driver.find_element(By.CSS_SELECTOR, "input[placeholder='OJTPK1212M']")
    # pan_num.send_keys("LFCPK4475H")
    # time.sleep(3)











    # pageone = ActivateFastagPages(chrome_driver)
    # time.sleep(20)
    # pageone.wait.until(EC.element_to_be_clickable(pageone.next_activate_button))
    # pagetwo = pageone.click_next_button()
    # time.sleep(5)
    # pagetwo.wait.until(EC.presence_of_element_located(pagetwo.barcode_input))
    #
    # pagetwo.enter_bar_code_input("TEST15-000-0000000")
    # pagetwo.confirm_bar_code_input("TEST15-000-0000000")
    # pagetwo.wait.until(presence_of_element_located(pagetwo.upload_fastag))
    # upload_fastag = chrome_driver.find_element(By.ID, "input-image").send_keys(r"C:\Users\Lenovo\Downloads\barcode.gif")
    # pagethree = pagetwo.go_to_submit_fastag()
    # pagethree.wait.until((EC.presence_of_element_located(pagethree.private_vehicle)))
    # pagethree.go_to_private_vehicle()
    # pagethree.go_to_vrn_activation_number("HR12AV8196")
    # time.sleep(5)
    # upload_rc_front = chrome_driver.find_element(By.ID, "input-image").send_keys(
    #     r"C:\Users\Lenovo\Downloads\barcode.gif")
    # upload_rc_back = chrome_driver.find_element(By.ID, "input-image").send_keys(
    #     r"C:\Users\Lenovo\Downloads\barcode.gif")
    # time.sleep(2)
    # pagefour = pagethree.go_to_submit_button()
    # pagefour.wait.until(EC.presence_of_element_located(pagefour.pan_number))
    # pagefour.enter_pan("LFCPK4475H")
    # pagefour.wait.until(EC.presence_of_element_located(pagefour.mobile_num))
    # pagefour.enter_mobile_num("9315229016")
    #
    # time.sleep(2)
    # pagefour.enter_engine_number("BS74B30658")
    # time.sleep(1)
    # pagefive = pagefour.submit_personal_details_button_next_personal()
    #
    # if pagefive.is_displayed(pagefive.bank_error):
    #     pagefive.fetch_details_error()
    #
    # time.sleep(15)
    # pagefive.wait.until(EC.visibility_of_element_located(pagefive.email))
    #
    # pagefive.enter_email("shubhamkhaneja29@gmail.com")
    # pagefive.enter_aadhar("532014464160")
    # print("Entered aadhar number, redirecting to the next page")
    # # pagefive.wait.until(EC.element_to_be_clickable(pagefive.submit_button()))
    # pagesix = pagefive.submit_button_next_page()
    # time.sleep(5)
    # pagesix.wait.until(EC.presence_of_element_located(pagesix.vehicle_front))
    # images = chrome_driver.find_element(By.ID, "input-image")
    #
    # front_image = chrome_driver.find_element(By.ID, "input-image").send_keys(
    #     r"C:\Users\Lenovo\Downloads\barcode.gif")
    # back_image = chrome_driver.find_element(By.ID, "input-image").send_keys(r"C:\Users\Lenovo\Downloads\barcode.gif")
    # rc_image = chrome_driver.find_element(By.ID, "input-image").send_keys(r"C:\Users\Lenovo\Downloads\barcode.gif")
    #
    # time.sleep(10)
    # print("Success")
    # # pagesix.click_submit_final_button()








