from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DocuSense"
    environment: str = "development"
    database_url: str = "postgresql://user:password@localhost:5432/docusense"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()