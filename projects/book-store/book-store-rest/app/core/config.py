import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
APP_NAME = os.getenv("APP_NAME")

