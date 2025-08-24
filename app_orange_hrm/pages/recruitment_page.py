import time
from dataclasses import dataclass
from typing import Sequence

import allure
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from app_orange_hrm.locators.recruitment_page import RecruitmentPageLocators, Tabs
from app_orange_hrm.pages.pages_strings.recruitment_vacancies import JobTitles
from base_ui.base_page import BasePage
from base_ui.exceptions import ElementAbsentException


@dataclass
class NewVacancyData:
    vacancy_name: Sequence[str]
    job_title: JobTitles
    hiring_manager: str
    description: str | None = None
    number_of_positions: int | None = None


class RecruitmentPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.click(self.main_menu.RECRUITMENT_PAGE)
        self.locators = RecruitmentPageLocators()

    @property
    def vacancies(self):
        self.find_element(self.locators.TABS[Tabs.VACANCIES]).click()
        return VacanciesPage(self.driver)


class VacanciesPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = RecruitmentPageLocators()

    @property
    def vacancies(self):
        self.find_element(self.locators.TABS[Tabs.VACANCIES]).click()
        return self

    @allure.step('Search vacancy')
    def search_vacancy_by_job_title(self, title: str):
        job_title_selector = self.find_element(self.locators.Vacancies.Search.JOB_TITLE_SELECTOR)
        self.select_element_by_text(job_title_selector, text=title)
        self.find_element(self.locators.Vacancies.Search.SEARCH_BUTTON).click()

    @allure.step('Get all job titles shown in the table')
    def get_job_titles_in_table(self):
        return self.find_all_elements(self.locators.Vacancies.VacanciesList.TABLE_JOB_TITLES, wait=True)

    @allure.step('Add new vacancy')
    def add_new_vacancy(self, data: NewVacancyData, active: bool = False, rss: bool = False):
        self.find_element(self.locators.Vacancies.VacanciesList.ADD_VACANCY_BUTTON).click()

        self.fill_out(
            self.locators.Vacancies.NewVacancyForm.VACANCY_TITLE,
            text=data.vacancy_name
        )
        self.select_element_by_text(self.locators.Vacancies.NewVacancyForm.JOB_TITLE, text=data.job_title)

        if not data.description is None:
            self.fill_out(self.locators.Vacancies.NewVacancyForm.DESCRIPTION_FIELD, text=data.description)

        self.fill_out(self.locators.Vacancies.NewVacancyForm.MANAGER_FIELD, text=data.hiring_manager)
        time.sleep(5)  # Otherwise even wait does not work
        autocomplete_visible = self.wait_for_visibility(
            self.locators.Vacancies.NewVacancyForm.MANAGERS_DROPDOWN_FIRST
        )
        if autocomplete_visible:
            self.fill_out(self.locators.Vacancies.NewVacancyForm.MANAGER_FIELD, Keys.ARROW_DOWN)
            self.fill_out(self.locators.Vacancies.NewVacancyForm.MANAGER_FIELD, Keys.ENTER)
        else:
            raise ElementAbsentException('Autocomplete is not visible')
        assert self.wait_for_invisibility(self.locators.Vacancies.NewVacancyForm.INVALID_NAME_INDICATOR)

        if not data.number_of_positions is None:
            self.fill_out(
                self.locators.Vacancies.NewVacancyForm.POSITIONS_COUNT_FIELD,
                text=str(data.number_of_positions)
            )
        if not active:
            self.click(self.locators.Vacancies.NewVacancyForm.ACTIVE_CHECKBOX)
        if not rss:
            self.click(self.locators.Vacancies.NewVacancyForm.RSS_CHECKBOX)
        self.click(self.locators.Vacancies.NewVacancyForm.SAVE_BUTTON)
        self.wait_element_in_dom(self.locators.SPINNER_LOADER)
        self.wait_for_invisibility(self.locators.SPINNER_LOADER)
