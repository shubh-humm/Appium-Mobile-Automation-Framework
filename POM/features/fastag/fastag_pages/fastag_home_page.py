from appium.webdriver.common.appiumby import AppiumBy
from common.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

from features.Money.money_home_page import MoneyHomePage
from features.fastag.fastag_pages.fastag_activation import ActivateFastagPages
from features.fastag.fastag_pages.fastag_activation_details import FastagActivationDetails

from features.fastag.fastag_pages.fastag_other_services_buy_now import OtherServices
from features.fastag.fastag_pages.fastag_passbook import FastagPassbook
from features.fastag.fastag_pages.fastag_recharge_page import FastagRechargePage
from features.fastag.fastag_pages.fastag_tag_closed import FastagTagClosed
from features.store.store_pages import fastag_product_store_page
from features.store.store_pages.fastag_product_store_page import FastagProductStorePage


class FastagHomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        self.fastag_text = (AppiumBy.ACCESSIBILITY_ID, "FASTag")
        self.buynow_fastag_button = (AppiumBy.ACCESSIBILITY_ID,  "fastag_buy_now")
        self.activate_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.recharge_input_field = (AppiumBy.XPATH, '//android.widget.EditText[contains(@hint, "fastag_recharge_now_input")]')
        self.recharge_now_button = (AppiumBy.ACCESSIBILITY_ID, "Recharge now")
        self.hns_icon_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.back_button = (AppiumBy.ACCESSIBILITY_ID, "")
        self.activate_fastag = (AppiumBy.ACCESSIBILITY_ID, "Activate FASTag\nActivate your FASTag within 60 seconds")
        self.FASTag_page = (AppiumBy.ACCESSIBILITY_ID, "FASTag")
        self.fastag_alerts = (AppiumBy.ACCESSIBILITY_ID, "+1 alert")
        self.your_alerts_sheet = (AppiumBy.ACCESSIBILITY_ID, "Your Alerts")
        self.pending_activation_alert = (AppiumBy.ACCESSIBILITY_ID, "Complete Now")
        self.raised_ticket_alert = (AppiumBy.ACCESSIBILITY_ID, "Check status")
        self.got_it_alert_cta = (AppiumBy.ACCESSIBILITY_ID, "Got It")
        self.tag_closed = (AppiumBy.ACCESSIBILITY_ID, "fastag_closed_tag") #CTA on closed tags
        self.refresh_balance = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_balance_refresh")
        self.card_rechargs = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Recharge"])[1]') #recharge CTA on vehicle card
        self.last_toll_debit = (AppiumBy.ACCESSIBILITY_ID, "Last toll debit\nDebited on: 9th October, 2025 | 05:29PM\n-₹20\nfastag_card_toll_click")
        self.currnt_balance_bottom_sheet = (AppiumBy.ACCESSIBILITY_ID, "CURRENT FASTAG BALANCE") #bs which appears which comes on refreshing the balance of vehicle cards
        self.check_money_offer = (AppiumBy.ACCESSIBILITY_ID, "Check your offer now")
        self.buy_new_fastag = (AppiumBy.ACCESSIBILITY_ID, "fastag_card_list_recharge") #CTA on closed tags
        self.recharge_refreshed_card = (AppiumBy.ACCESSIBILITY_ID, "") #CTA appers on refresh balance BS on cards, method for this has still to be added yet.

    def go_to_buynow_fastag_page(self):
        if not self.is_displayed(self.buynow_fastag_button):
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_buy_now")
        self.click(self.buynow_fastag_button)
        self.logger.info("Navigating to buy now page")
        return OtherServices(self.driver)

    def go_to_activate_flow(self):
        self.click(self.activate_button)
        return self

    def go_to_recharge_input(self):
        if not self.is_displayed(self.recharge_input_field):
            self.scroll_to_element(AppiumBy.XPATH, '//android.widget.EditText[contains(@hint, "fastag_recharge_now_input")]')
        self.click(self.recharge_input_field)
        return self

    # def recharge_existing_vehicle(self):
    #     vehicle_xpath = "to be added"
    #     vehicle_locator = (AppiumBy.XPATH, vehicle_xpath)
    #     self.click(vehicle_locator)
    #     return self

    def recharge_new_vehicle(self, vehicle_number):
        self.type_text(self.recharge_input_field, vehicle_number)
        self.logger.warning(f"Recharge value : {vehicle_number}")

    def go_to_recharge_now_button(self):
        self.click(self.recharge_now_button)
        self.logger.info("Clicked recharge now button")
        return FastagRechargePage(self.driver)

    def home_hns_icon(self):
        self.click(self.hns_icon_button)
        self.logger.info("Clicked on Hns Button")

    def go_to_main_landing_page(self):
        self.click(self.back_button)

    def go_to_activate_fastag(self):
        self.click(self.activate_fastag)
        return ActivateFastagPages(self.driver)

    def FASTag_landing_page(self):
        self.is_displayed(self.FASTag_page)

    def click_on_alerts(self):
        self.click(self.fastag_alerts)
        self.logger.info("Looking for alerts")
        return self

    def click_on_pending_activation_cta(self):
        self.click(self.pending_activation_alert)
        return FastagActivationDetails(self.driver)

    def click_on_raised_ticket_alert(self):
        self.click(self.raised_ticket_alert)

    def click_on_got_alerts(self):
        self.click(self.got_it_alert_cta)
        return self

    def click_refresh_balance(self):
        self.click(self.refresh_balance)
        self.logger.info("Refreshing balance...")
        return self

    def click_recharge_refreshed_vehicle_bs(self):
        """this is a recharge CTA which appears on refresh balance bs"""
        self.click(self.recharge_refreshed_card)
        self.logger.info("Clicked on Recharge button on the BS")
        return FastagRechargePage(self.driver)

    def click_last_toll_debit(self):
        self.click(self.last_toll_debit)
        self.logger.info("Clicked on last toll debit")
        return FastagPassbook(self.driver)

    def click_on_recharge_card(self):
        self.click(self.card_rechargs)
        return FastagRechargePage(self.driver)

    def click_why_is_tag_closed(self):
        if not self.is_displayed(self.tag_closed):
            self.scroll_to_element(AppiumBy.ACCESSIBILITY_ID, "fastag_closed_tag")
        self.click(self.tag_closed)
        self.logger.info("Clicked on 'Why is tag closed' button")
        return FastagTagClosed(self.driver)

    def click_check_money_offer(self):
        self.click(self.check_money_offer)
        return MoneyHomePage(self.driver)

    def click_buy_new_fastag(self):
        self.click(self.buy_new_fastag)
        self.logger.info("Clicked on Buy new fastag (Other Services)")
        return OtherServices(self.driver)
