from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 10100


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = 5432
    database: str = ''
    user: str = ''
    password: str = ''
    echo: bool = False,
    echo_pool: bool = False,
    pool_size: int = 5,
    max_overflow: int = 10,

    @property
    def url(self) -> PostgresDsn:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),  # порядо підвантаження мержа змінинних
        case_sensitive=False,  # не важливий регістр
        env_nested_delimiter="__",  # розділювач
        env_prefix="APP__",  # префікс змінних, які будуть автоматично парситись
        env_ignore_empty=True,
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()

print(settings.db)
