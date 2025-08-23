import os

from dotenv import load_dotenv

load_dotenv()


class Credentials:
    LOGIN = os.getenv('QA_LOGIN')
    PASSWORD = os.getenv('QA_PASSWORD')
