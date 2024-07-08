from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    TIME_BETWEEN_RECEIVING_BOXES: list[int] = [3600, 7200]
    REF_ID: str = ''

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


