import allure
from selenium.webdriver.remote.webdriver import WebDriver

from app_orange_hrm.locators.admin_page import AdminPageLocators
from base_ui.base_page import BasePage


class AdminPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.click(self.main_menu.ADMIN_PAGE)
        self.locators = AdminPageLocators()

    @property
    def new_user(self):
        return self.add_new_user()

    @allure.step('Open "Add new user form"')
    def add_new_user(self):
        self.find_element(self.locators.ADD_USER_BUTTON).click()
        return NewUserForm(self.driver)


class NewUserForm(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = AdminPageLocators()

    @allure.step('Close "New user" form')
    def close_new_user_form(self):
        self.find_element(self.locators.NewUserLocators.CANCEL_BUTTON).click()
