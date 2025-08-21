import os

import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    browser = os.getenv('BROWSER')
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-search-engine-screen')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--disable-search-engine-screen')
        driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(20)
    request.cls.driver = driver

    yield

    driver.quit()