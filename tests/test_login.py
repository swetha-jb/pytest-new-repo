import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.sanity
    def test_login_with_valid_cred(self):
        login_page_driver = LoginPage(self.driver)
        login_page_driver.enter_the_username(username="viku.prod@yopmail.com")
        login_page_driver.enter_the_password(password="Netgear1@")
        login_page_driver.click_on_sign_in_button()
    
