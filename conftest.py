import pytest
from selenium import webdriver

from app_orange_hrm.pages.login_page import LoginPage
from base_ui.app_page import AppPage
from data.weblinks import WebLinks


@pytest.fixture(autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-search-engine-screen')
    driver = webdriver.Chrome(options=options)
    driver.get(WebLinks.BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def app_driver(driver):
    login_page = LoginPage(driver)
    login_page.login_as(login_page.credentials.LOGIN, login_page.credentials.PASSWORD)
    return driver


@pytest.fixture
def app(app_driver):
    return AppPage(app_driver)
