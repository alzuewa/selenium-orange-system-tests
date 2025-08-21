import allure

from base.base_test import BaseTest


@allure.epic('Users')
@allure.feature('Trial accounts')
@allure.story('New accounts')
class TestLoginPage(BaseTest):

    @allure.title('Log into trial account')
    def test_login_example_imperative(self):
        self.login_page.open()
        self.login_page.login_as(login=self.credentials.LOGIN, password=self.credentials.PASSWORD)

        self.dashboard_page.click_help()
