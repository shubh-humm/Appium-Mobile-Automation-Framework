import sys
import os
import time
from binascii import b2a_uu

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from POM.features.Buy_Petrol.petrol_fixtures import buy_petrol_home_pagee


# Add POM directory
test_dir = os.path.dirname(os.path.abspath(__file__))
pom_dir = os.path.join(test_dir, '../../..')
pom_abs = os.path.abspath(pom_dir)
sys.path.insert(0, pom_abs)

"""""""""""""""""""""""""""""""""IOCL TEST CASES"""""""""""""""""""""""""""""""""""""""""""""""

class TestIOCLOnboarding:

    @pytest.mark.smoke
    def test_iocl_onboarding(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        assert home_page.wait_for_visibility(home_page.buy_petrol), "Buy petrol home page is not loaded"
        iocl = home_page.click_redeem_cashback()
        assert iocl.wait_for_visibility(iocl.petrol_cashback), "IOCL onboarding page 1 has not loaded"
        iocl.click_select_car()
        assert iocl.wait_for_visibility(iocl.your_vehicles), "Vehicles BS has not loaded"
        iocl.select_vehicle_card_by_index(0) #add the index value here
        iocl.click_car_selected()
        assert iocl.wait_for_invisibility(iocl.your_vehicles), "Vehicles BS has not closed"
        iocl.click_next_vehicle_details()
        assert iocl.wait_for_visibility(iocl.enter_pin), "IOCL onboarding page 2 has not loaded"
        pincode = "110089"
        iocl.enter_pincode(pincode)
        assert iocl.get_text(iocl.enter_pin) == str(pincode), "PIN code is not entered correctly"
        iocl.click_dob()
        assert iocl.wait_for_visibility(iocl.ok_btn_calendar), "Calendar pop has not displayed"
        iocl.click_confirm_date()
        assert iocl.wait_for_invisibility(iocl.ok_btn_calendar), "Calendar pop has not closed"

    @pytest.mark.regression
    def test_tandc(self, buy_petrol_home_pagee):
        home_page = buy_petrol_home_pagee
        iocl = home_page.click_redeem_cashback()
        iocl.click_terms_conditions()
        assert iocl.wait_for_visibility(iocl.terms_conditions), "Terms and conditions BS has not displayed"
        iocl.click_close_tandc()
        assert iocl.wait_for_invisibility(iocl.terms_conditions), "Terms and conditions BS has not closed"

