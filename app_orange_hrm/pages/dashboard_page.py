import allure
from selenium.webdriver.remote.webdriver import WebDriver

from app_orange_hrm.locators.dashboard_page import DashboardPageLocators, Widgets
from base_ui.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.click(self.main_menu.DASHBOARD_PAGE)
        self.locators = DashboardPageLocators()

    @allure.step('Assert Attendance widget is on the page')
    def is_attendance_widget_present(self):
        self.find_element(self.locators.WIDGETS[Widgets.ATTENDANCE])
