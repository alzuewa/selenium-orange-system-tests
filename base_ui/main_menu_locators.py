from base_ui.app_common_locators import AppCommonLocators
from base_ui.element import By, Element


class MainMenuLocators(AppCommonLocators):
    SIDEBAR_LOCATOR = '//*[@class="oxd-main-menu"]'
    ADMIN_PAGE = Element(By.XPATH, f'{SIDEBAR_LOCATOR}//*[text()="Admin"]', 'Admin page')
    PIM_PAGE = Element(By.XPATH, f'{SIDEBAR_LOCATOR}//*[text()="PIM"]', 'PIM page')
    LEAVE_PAGE = Element(By.XPATH, f'{SIDEBAR_LOCATOR}//*[text()="Leave"]', 'Leave page')
    TIME_PAGE = Element(By.XPATH, f'{SIDEBAR_LOCATOR}//*[text()="Time"]', 'Time page')
    DASHBOARD_PAGE = Element(By.XPATH, f'{SIDEBAR_LOCATOR}//*[text()="Dashboard"]', 'Dashboard page')
    RECRUITMENT_PAGE = Element(By.XPATH, f'{SIDEBAR_LOCATOR}//*[text()="Recruitment"]', 'Recruitment page')
