import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import login_loc


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Entering the Username")
    def enter_the_username(self, username):
        email_field = self.wait.until(
            EC.presence_of_element_located(login_loc.email_input_loc)
        )
        email_field.send_keys(username)

    @allure.step("Entering the Password")
    def enter_the_password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located(login_loc.password_input_loc)
        )
        password_field.send_keys(password)

    @allure.step("Clicking on Sign In Button")
    def click_on_sign_in_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(login_loc.signIn_button_loc)
        )
        button.click()

