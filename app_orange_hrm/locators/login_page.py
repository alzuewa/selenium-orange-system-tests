from base_ui.app_common_locators import AppCommonLocators
from base_ui.element import By, Element


class LoginPageLocators(AppCommonLocators):
    LOGIN_FIELD = Element(By.XPATH, '//input[@name="username"]', 'Login field')
    PASSWORD_FIELD = Element(By.XPATH, '//input[@name="password"]', 'Password field')
    SUBMIT_BUTTON = Element(By.XPATH, '//button[@type="submit"]', 'Submit button')
