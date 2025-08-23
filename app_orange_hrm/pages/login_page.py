import allure
from selenium.webdriver.remote.webdriver import WebDriver

from app_orange_hrm.locators.login_page import LoginPageLocators
from base_ui.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    @allure.step('Enter login')
    def enter_login(self, login: str):
        login_field = self.find_element(self.locators.LOGIN_FIELD)
        login_field.send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password: str):
        password_field = self.find_element(self.locators.PASSWORD_FIELD)
        password_field.send_keys(password)

    @allure.step('Click submit button')
    def click_submit(self):
        submit_button = self.find_element(self.locators.SUBMIT_BUTTON)
        submit_button.click()

    def login_as(self, login: str, password: str):
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit()
