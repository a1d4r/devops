from zoneinfo import ZoneInfo

from pydantic import BaseSettings


class Settings(BaseSettings):
    datetime_format: str = '%H:%M:%S'
    timezone: ZoneInfo = ZoneInfo('Europe/Moscow')


settings = Settings()
