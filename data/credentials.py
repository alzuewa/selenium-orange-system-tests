import os
from dotenv import load_dotenv

load_dotenv()


class Credentials:
    if os.getenv('STAND') == 'prod':
        LOGIN = os.getenv('PROD_LOGIN')
        PASSWORD = os.getenv('PROD_PASSWORD')
    elif os.getenv('STAND') == 'qa':
        LOGIN = os.getenv('QA_LOGIN')
        PASSWORD = os.getenv('QA_PASSWORD')