import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from meta_classes.meta_locators import MetaLocator


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        with allure.step(f'Open url {self._PAGE_URL}'):
            self.driver.get(self._PAGE_URL)
