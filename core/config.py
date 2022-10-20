import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "local"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"
    READER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"

    SENTRY_SDN: str = None
    CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class ProductionConfig(Config):
    ENV: str = "prod"
    DEBUG: str = False
    WRITER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"
    READER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"


class DevelopmentConfig(Config):
    ENV: str = "dev"
    WRITER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"
    READER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    ENV: str = "local"
    WRITER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"
    READER_DB_URL: str = f"mysql+aiomysql://db_user:db_password@localhost:3306/schema"


def get_config() -> Config:
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }

    return config_type[env]


config: Config = get_config()
