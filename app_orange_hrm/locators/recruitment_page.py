from enum import StrEnum

from base_ui.app_common_locators import AppCommonLocators
from base_ui.element import By, Element


class Tabs(StrEnum):
    CANDIDATES = 'Candidates'
    VACANCIES = 'Vacancies'


class RecruitmentPageLocators(AppCommonLocators):
    TABS = {
        Tabs.CANDIDATES: Element(By.XPATH, '//*[@class="oxd-topbar-body-nav-tab-item" and text()="Candidates"]',
                                 'Candidates widget'),
        Tabs.VACANCIES: Element(By.XPATH, '//*[@class="oxd-topbar-body-nav-tab-item" and text()="Vacancies"]',
                                'Vacancies widget')
    }

    class Vacancies:
        class VacanciesList:
            ADD_VACANCY_BUTTON = Element(By.XPATH, '//button[text()=" Add "]', 'Add vacancy button')
            VACANCY_ROW = '.oxd-table-row '
            TABLE_VACANCIES_TITLES = Element(By.CSS_SELECTOR, f'{VACANCY_ROW} .oxd-table-cell:nth-child(2)',
                                             'Vacancies list')
            TABLE_JOB_TITLES = Element(By.CSS_SELECTOR, f'{VACANCY_ROW} .oxd-table-cell:nth-child(3)',
                                       'Job Titles list')

        class NewVacancyForm:
            VACANCY_TITLE = Element(By.CSS_SELECTOR, '.oxd-form .oxd-grid-3:nth-child(1) .oxd-input',
                                    'Vacancy title field')
            JOB_TITLE = Element(By.CSS_SELECTOR, '.oxd-form .oxd-grid-3:nth-child(1) .oxd-select-wrapper',
                                'Job title field')
            DESCRIPTION_FIELD = Element(By.CSS_SELECTOR, '.oxd-form .oxd-grid-3:nth-child(2) .oxd-textarea',
                                        'Description field')
            MANAGER_FIELD = Element(By.CSS_SELECTOR,
                                    '.oxd-form .oxd-grid-3:nth-child(3) .oxd-autocomplete-text-input input',
                                    'Manager field')
            MANAGERS_DROPDOWN_FIRST = Element(By.CSS_SELECTOR,
                                              '.oxd-autocomplete-dropdown .oxd-autocomplete-option:nth-child(1)',
                                              'Managers dropdown')
            POSITIONS_COUNT_FIELD = Element(By.CSS_SELECTOR,
                                            '.oxd-form .oxd-grid-3:nth-child(3) .oxd-grid-item:nth-child(2) input',
                                            'Count field')

            ACTIVE_CHECKBOX = Element(By.XPATH, '//p[text()="Active"]/..//label', 'Active checkbox')
            RSS_CHECKBOX = Element(By.XPATH, '//p[text()="Publish in RSS Feed and Web Page"]/..//label', 'RSS checkbox')
            SAVE_BUTTON = Element(By.XPATH, '//button[@type="submit"]', 'Save button')

            INVALID_NAME_INDICATOR = Element(By.XPATH, '//span[text()="Invalid"]', 'Invalid Name indicator')


        class Search:
            JOB_TITLE_SELECTOR = Element(
                By.CSS_SELECTOR,
                '.oxd-grid-4 .oxd-grid-item--gutters:nth-child(1) .oxd-select-wrapper',
                'Job title selector'
            )
            VACANCY_SELECTOR = Element(
                By.CSS_SELECTOR,
                '.oxd-grid-4 .oxd-grid-item--gutters:nth-child(2) .oxd-select-wrapper',
                'Vacancy selector'
            )
            HIRING_MANAGER_SELECTOR = Element(
                By.CSS_SELECTOR,
                '.oxd-grid-4 .oxd-grid-item--gutters:nth-child(3) .oxd-select-wrapper',
                'Hiring manager selector'
            )
            STATUS_SELECTOR = Element(
                By.CSS_SELECTOR,
                '.oxd-grid-4 .oxd-grid-item--gutters:nth-child(4) .oxd-select-wrapper',
                'Status selector'
            )
            SEARCH_BUTTON = Element(By.XPATH, '//button[text()=" Search "]', 'Search button')
