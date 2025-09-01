from helpers.base_page import *
import login.locators as loc


class Login(CommonClass):
    bp= Base()
    def add_username(self, text):
        self.send_keys_to_element('CSS_SELECTOR', loc.email, text)

    def add_password(self, text):
        self.send_keys_to_element('CSS_SELECTOR', loc.password, text)

    def click_signin(self):
        self.click_element('CSS_SELECTOR', loc.sign_in_button)

    def wait_to_verify_user_is_on_dashboard(self):
        self.wait_for_visibility('CSS_SELECTOR', loc.dashboard)
