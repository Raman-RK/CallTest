from helpers.base_page import *
import dialer.locators as dloc

class Dialer(CommonClass):
    bp= Base()

    def click_dialer_icon(self):
        self.click_element('XPATH', dloc.dialer_icon)

    def accept_welcome(self):
        self.click_element('CSS_SELECTOR', dloc.welcome_msg)

    def enter_phone_number(self, text):
        self.send_keys_to_element('CSS_SELECTOR', dloc.phone_input, text)
