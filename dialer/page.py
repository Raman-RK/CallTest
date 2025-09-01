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

    def dial_number(self):
        self.click_element('CSS_SELECTOR', dloc.dial_icon)

    def disconnect_call(self):
        self.click_element('CSS_SELECTOR', dloc.disconnect_icon)

    def mute_call(self):
        self.click_element('XPATH', dloc.mute_icon_xpath)

    def unmute_call(self):
        self.click_element('XPATH', dloc.unmute_icon_xpath)

    def hold_call(self):
        self.click_element('XPATH', dloc.hold_icon_xpath)

    def open_keypad(self):
        self.click_element('XPATH', dloc.keypd_icon_xpath)

    def start_stop_recording(self):
        self.click_element('XPATH', dloc.record_icon_xpath)

    def click_speaker_icon(self):
        self.click_element('XPATH', dloc.speaker_icon_xpath)

    def open_notes_main_dialer(self):
        self.click_element('XPATH', dloc.notes_icon_xpath)

    def schedule_call_back(self):
        self.click_element('XPATH', dloc.schedule_call_back)

    def call_again(self):
        self.click_element('XPATH', dloc.call_again)

    def transfer_call(self):
        self.click_element('XPATH', dloc.transfer_icon_xpath)

    def open_notes_after_call(self):
        self.click_element('XPATH', dloc.notes_after_call)

