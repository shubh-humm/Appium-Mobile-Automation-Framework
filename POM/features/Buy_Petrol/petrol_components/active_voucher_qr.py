from common.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ActiveVoucherQr(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.close_qr = (AppiumBy.ACCESSIBILITY_ID, "close_voucher_qr") #closes the qr
        self.voucher_code = (AppiumBy.ACCESSIBILITY_ID, "Voucher Code") #"voucher code" is the text on qr page

    def click_close_qr(self):
        self.click(self.close_qr)
        self.logger.info("Closing QR code")