import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    request.cls.driver = driver  # creates driver field in test class (because of referring to request.cls)
    yield
    driver.quit()