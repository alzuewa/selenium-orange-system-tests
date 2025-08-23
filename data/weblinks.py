from enum import StrEnum


class WebLinks(StrEnum):
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php'

    DASHBOARD_PAGE = f'{BASE_URL}/dashboard/index'
    LOGIN_PAGE = f'{BASE_URL}/auth/login'
    RECRUITMENT_PAGE = f'{BASE_URL}/recruitment/viewCandidates'
