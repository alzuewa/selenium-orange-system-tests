from base.base_page import BasePage


class DashboardPage(BasePage):
    _PAGE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    _HELP_BUTTON = '//button[@title="Help"]'

    def click_help(self):
        self.driver.find_element(*self._HELP_BUTTON).click()
