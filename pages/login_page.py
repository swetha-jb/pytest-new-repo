from locators import login_loc
import time
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Entering the Username")
    def enter_the_username(self, username):
        self.driver.find_element(*login_loc.email_input_loc).send_keys(username)

    @allure.step("Entering the Password")
    def enter_the_password(self, password):
        self.driver.find_element(*login_loc.password_input_loc).send_keys(password)

    @allure.step("Clicking on Sign In Button")
    def click_on_sign_in_button(self):
        self.driver.find_element(*login_loc.signIn_button_loc).click()
        time.sleep(10)

