import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        print("[ConfigManager] Loading .env file...")
        load_dotenv()
        self.environment = os.getenv("ENVIRONMENT", "DEV").upper()
        print(f"[ConfigManager] Environment set to: {self.environment}")

    @staticmethod
    def get_url(key: str) -> str:
        print(f"[ConfigManager] Attempting to fetch key: {key.upper()}")
        value = os.getenv(key.upper())
        if not value:
            raise KeyError(f"Missing environment variable: {key.upper()}")
        print(f"[ConfigManager] Fetched {key.upper()} = {value}")
        return value
