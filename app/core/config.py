import os
class Settings:
    APP_NAME = 'VetCare+'
    ENV = os.getenv('VETCARE_ENV','dev')
    DB_URL = os.getenv('DB_URL','sqlite:///./vetcare.db')
settings = Settings()
