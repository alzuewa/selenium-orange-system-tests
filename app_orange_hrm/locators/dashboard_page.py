from enum import StrEnum

from base_ui.app_common_locators import AppCommonLocators
from base_ui.element import By, Element


class Widgets(StrEnum):
    ATTENDANCE = 'Attendance'
    TODO_LIST = 'TODO list'


class DashboardPageLocators(AppCommonLocators):
    WIDGETS = {
        Widgets.ATTENDANCE: Element(By.XPATH, '//*[@class="orangehrm-attendance-card"]', 'Attendance widget'),
        Widgets.TODO_LIST: Element(By.XPATH, '//*[@class="orangehrm-todo-list"]', 'TODO list widget')
    }
