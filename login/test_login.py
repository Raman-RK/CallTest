import time
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dialer.page import Dialer
from utilities.read_properties import ConfigManager
from utilities.read_credentials import CredentialManager
from helpers.conf_test import *
from login.page import Login


config = ConfigManager()
credentials_manager = CredentialManager()


@pytest.fixture
def login(setup, request):
    role = request.param
    s_email = credentials_manager.get_email(role)
    s_password = credentials_manager.get_password(role)

    if not s_email or not s_password:
        print(f"Checking credentials for {role}: {s_email}, {s_password}")
        pytest.fail(f"Missing credentials for role: {role}")

    driver = setup
    lp = Login(driver)

    url = config.get_url('WEBSITE')
    print(f"URL is: {url}")
    driver.get(url)
    driver.maximize_window()

    with allure.step(f"Logging in as {role}"):
        lp.add_username(s_email)
        lp.add_password(s_password)
        lp.click_signin()

    return driver, role


@pytest.mark.parametrize("login", ["admin"], indirect=True)
def test_login(login):
    driver, role = login
    lp = Login(driver)
    dp = Dialer(driver)

    lp.wait_to_verify_user_is_on_dashboard()
    dp.accept_welcome()
    dp.click_dialer_icon()
    s_phone = credentials_manager.get_phone(role)
    dp.enter_phone_number(s_phone)
    dp.dial_number()
    time.sleep(20)


