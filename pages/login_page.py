import allure

from base.base_page import BasePage


class LoginPage(BasePage):

    _PAGE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    _LOGIN_FIELD = '//input[@name="username"]'
    _PASSWORD_FIELD = '//input[@name="password"]'
    _SUBMIT_BUTTON = '//button[@type="submit"]'

    @allure.step('Enter login')
    def enter_login(self, login: str):
        login_field = self.driver.find_element(*self._LOGIN_FIELD)
        login_field.send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password: str):
        password_field = self.driver.find_element(*self._PASSWORD_FIELD)
        password_field.send_keys(password)

    @allure.step('Click submit button')
    def click_submit(self):
        submit_button = self.driver.find_element(*self._SUBMIT_BUTTON)
        submit_button.click()
        