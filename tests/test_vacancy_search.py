import string
from random import choices

import allure
import pytest

from app_orange_hrm.pages.pages_strings.recruitment_vacancies import JobTitles
from app_orange_hrm.pages.recruitment_page import NewVacancyData


@allure.epic('Vacancies')
@allure.feature('Search vacancy')
@allure.story('Vacancy search filters')
class TestRecruitmentPage:

    @allure.title('Search vacancy by job title')
    @pytest.mark.parametrize(
        'job_title, vacancy_name', [
            # TODO Replace with Faker
            (JobTitles.SOFTWARE_ENGINEER, ''.join(choices(string.ascii_letters, k=50))),
            (JobTitles.HR_MANAGER, ''.join(choices(string.digits, k=1))),
            (JobTitles.CUSTOMER_SUCCESS_MANAGER, ''.join(choices(string.ascii_letters, k=15)))
        ]
    )
    def test_vacancy_search(self, app, job_title, vacancy_name):
        vacancies_page = app.recruitment_page.vacancies
        vacancies_page.add_new_vacancy(
            NewVacancyData(
                vacancy_name=vacancy_name,
                job_title=job_title,
                hiring_manager='A'
            )
        )
        vacancies_page.vacancies.search_vacancy_by_job_title(job_title)
        results = vacancies_page.get_job_titles_in_table()
        assert all(item.text.strip() == job_title for item in results)
