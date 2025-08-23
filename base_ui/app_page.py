from selenium.webdriver.remote.webdriver import WebDriver

from app_orange_hrm.pages.dashboard_page import DashboardPage
from app_orange_hrm.pages.login_page import LoginPage
from app_orange_hrm.pages.recruitment_page import RecruitmentPage
from base_ui.base_page import BasePage


class AppPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.dashboard_page = DashboardPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.recruitment_page = RecruitmentPage(self.driver)
