import pickle
from collections.abc import Sequence
from pathlib import Path

import allure
from faker import Faker
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base_ui.element import Element, By
from base_ui.main_menu_locators import MainMenuLocators
from data.credentials import Credentials


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver,
            timeout=20,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        )
        self.actions = ActionChains(self.driver)
        self.main_menu = MainMenuLocators()

        self.url = 'https://opensource-demo.orangehrmlive.com'
        self.credentials = Credentials()

    def open(self):
        with allure.step(f'Open url {self.url}'):
            self.driver.get(self.url)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.url))

    def find_element(self, locator: Element):
        return self.wait.until(EC.visibility_of_element_located((locator.by, locator.value)))

    def find_all_elements(self, locator: Element, wait=False):
        if wait:
            return self.wait.until(EC.visibility_of_all_elements_located((locator.by, locator.value)))
        else:
            return self.driver.find_elements(locator.by, locator.value)

    def fill_out(self, locator: Element, text: str | Sequence):
        element = self.find_element(locator)
        element.send_keys(text)

    def click(self, locator: Element, element_name: str = None):
        return self.wait.until(
            EC.element_to_be_clickable((locator.by, locator.value)),
            message=f'{element_name} is not clickable'
        ).click()

    def screenshot(self, filename: str | Path):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=filename,
            attachment_type=allure.attachment_type.PNG
        )

    def wait_for_visibility(self, locator: Element):
        try:
            self.wait.until(EC.visibility_of_element_located((locator.by, locator.value)))
            return True
        except TimeoutException:
            return False

    def wait_for_invisibility(self, locator: Element, message: str = None):
        return self.wait.until(EC.invisibility_of_element((locator.by, locator.value)), message=message)

    def save_cookies(self, cookies_name='temp-cookies'):
        pickle.dump(self.driver.get_cookies(), open(f'cookies/{cookies_name}.txt', 'wb'))

    def load_cookies(self, cookies_name='temp-cookies'):
        cookies = pickle.load(open(f'cookies/{cookies_name}.txt', 'rb'))
        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def scroll_by(self, x, y):
        self.driver.execute_script(f'window.scrollTo({x}, {y})')

    def scroll_to_bottom(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def scroll_to_top(self):
        self.driver.execute_script('window.scrollTo(0, 0)')

    def scroll_to_element(self, locator: Element | WebElement):
        element = self.find_element(locator) if isinstance(locator, Element) else locator
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        return element

    def select_element_by_text(self, selector_element: Element | WebElement, text):
        selector = self.find_element(selector_element) if isinstance(selector_element, Element) else selector_element
        selector.click()
        target_locator = selector.find_element(By.XPATH, f'//span[contains(text(), "{text}")]')
        self.actions.move_to_element(target_locator).perform()
        target_locator.click()

    def refresh_page(self):
        self.driver.refresh()
