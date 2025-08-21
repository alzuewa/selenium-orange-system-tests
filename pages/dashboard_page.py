from base.base_page import BasePage
from data.links import Links


class DashboardPage(BasePage):
    _PAGE_URL = Links.DASHBOARD_PAGE

    _HELP_BUTTON = '//button[@title="Help"]'

    def click_help(self):
        self.driver.find_element(*self._HELP_BUTTON).click()
