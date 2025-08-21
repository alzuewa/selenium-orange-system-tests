from enum import StrEnum

class Links(StrEnum):
    BASE_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php'

    DASHBOARD_PAGE = f'{BASE_URL}/dashboard/index'
    LOGIN_PAGE = f'{BASE_URL}/auth/login'
