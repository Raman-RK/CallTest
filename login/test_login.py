import time

from dialer.page import Dialer
from utilities.read_properties import ConfigManager
from utilities.read_credentials import CredentialManager
from helpers.conf_test import *
from login.page import Login

class TestLogin:
    config = ConfigManager()
    url = config.get_url('WEBSITE')
    credentials_manager = CredentialManager()

    @pytest.fixture
    def login(self, setup, request):
        role = request.param
        s_email = self.credentials_manager.get_email(role)
        s_password = self.credentials_manager.get_password(role)
        if not s_email or not s_password:
            print(f"Checking credentials for {role}: {s_email}, {s_password}")
            pytest.fail(f"Missing credentials for role: {role}")

        driver = setup
        lp = Login(driver)

        print(f"URL is: {self.url}")
        driver.get(self.url)
        driver.maximize_window()

        with allure.step(f"Logging in as {role}"):
            lp.add_username(s_email)
            lp.add_password(s_password)
            lp.click_signin()

        return driver

    @pytest.mark.parametrize("login", ["admin"], indirect=True)
    def test_login(self, login):
        driver = login
        lp = Login(driver)
        dp = Dialer(driver)
        lp.wait_for_visibility_of_element()
        dp.accept_welcome()
        dp.click_dialer_icon()
        time.sleep(20)



