import allure
import pytest

from base.base_test import BaseTest


@allure.epic('Users')
@allure.feature('Trial accounts')
@allure.story('New accounts')
class TestLoginPage(BaseTest):

    @allure.title('Log into trial account')
    def test_login_example(self):
        self.login_page.open()
        self.login_page.enter_login('Admin')
        self.login_page.enter_password('admin123')
        self.login_page.click_submit()

        self.dashboard_page.click_help()

